# -*- coding: utf-8 -*-
"""Unit tests for mark_as_htmx_request.

These tests do not require a full Plone site — they test the marking logic
in isolation using a minimal fake request and event.
"""
import unittest

from plone.htmx.events import mark_as_htmx_request
from plone.htmx.interfaces import IHtmxRequest
from zope.interface import implementer
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.traversing.interfaces import IBeforeTraverseEvent


@implementer(IBrowserRequest)
class FakeRequest:
    """Minimal request stub for unit testing."""

    def __init__(self, headers=None):
        self._headers = headers or {}

    def getHeader(self, name, default=None):
        return self._headers.get(name, default)


@implementer(IBeforeTraverseEvent)
class FakeBeforeTraverseEvent:
    """Minimal BeforeTraverse event stub."""

    def __init__(self, request):
        self.request = request


class TestMarkAsHtmxRequest(unittest.TestCase):
    """Unit tests for the mark_as_htmx_request subscriber."""

    def _call(self, headers):
        request = FakeRequest(headers)
        event = FakeBeforeTraverseEvent(request)
        mark_as_htmx_request(event)
        return request

    def test_marks_request_when_hx_request_is_true(self):
        """A request with HX-Request: true is marked with IHtmxRequest."""
        request = self._call({"HX-Request": "true"})
        self.assertTrue(IHtmxRequest.providedBy(request))

    def test_does_not_mark_request_without_header(self):
        """A plain browser request without HX-Request is not marked."""
        request = self._call({})
        self.assertFalse(IHtmxRequest.providedBy(request))

    def test_does_not_mark_request_with_false_value(self):
        """HX-Request: false does not trigger marking (non-standard but defensive)."""
        request = self._call({"HX-Request": "false"})
        self.assertFalse(IHtmxRequest.providedBy(request))

    def test_does_not_mark_request_with_unrelated_header(self):
        """An unrelated header like Accept: text/html does not trigger marking."""
        request = self._call({"Accept": "text/html"})
        self.assertFalse(IHtmxRequest.providedBy(request))

    def test_htmx_request_interface_is_idempotent(self):
        """Calling the subscriber twice does not raise — alsoProvides is idempotent."""
        request = FakeRequest({"HX-Request": "true"})
        event = FakeBeforeTraverseEvent(request)
        mark_as_htmx_request(event)
        mark_as_htmx_request(event)  # should not raise
        self.assertTrue(IHtmxRequest.providedBy(request))
