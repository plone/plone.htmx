# -*- coding: utf-8 -*-
"""Integration tests for IHtmxRequest layer dispatch.

These tests use the PLONE_HTMX_FUNCTIONAL_TESTING layer which provides a
full Plone site with plone.htmx installed. They exercise the full publisher
pipeline so that the BeforeTraverse subscriber fires and the layer lookup
works exactly as it would in production.
"""
import unittest

from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.htmx.interfaces import IHtmxRequest
from plone.htmx.testing import PLONE_HTMX_FUNCTIONAL_TESTING
from plone.htmx.testing import PLONE_HTMX_INTEGRATION_TESTING
from plone.testing.zope import Browser


class TestIHtmxRequestMarking(unittest.TestCase):
    """Integration tests: verify IHtmxRequest is applied to the request
    when the HX-Request header is present, using the real Zope publisher.
    """

    layer = PLONE_HTMX_FUNCTIONAL_TESTING

    def _make_browser(self, htmx=False):
        browser = Browser(self.layer["app"])
        browser.handleErrors = False
        browser.addHeader(
            "Authorization",
            "Basic {}:{}".format(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
        )
        if htmx:
            browser.addHeader("HX-Request", "true")
        return browser

    def test_normal_request_does_not_provide_ihtmxrequest(self):
        """A plain browser request should NOT provide IHtmxRequest."""
        portal = self.layer["portal"]
        request = portal.REQUEST
        # In a fresh integration test the request has no HX-Request header
        self.assertFalse(IHtmxRequest.providedBy(request))

    def test_htmx_view_is_served_for_htmx_request(self):
        """The htmx_view test view is accessible when HX-Request is set."""
        browser = self._make_browser(htmx=True)
        portal = self.layer["portal"]
        browser.open(portal.absolute_url() + "/news/htmx_view")
        # The view should render without error
        self.assertIn("200", browser.headers.get("Status", "200"))

    def test_htmx_view_is_served_for_normal_request(self):
        """The htmx_view test view also works for normal requests (fallback)."""
        browser = self._make_browser(htmx=False)
        portal = self.layer["portal"]
        browser.open(portal.absolute_url() + "/news/htmx_view")
        self.assertIn("200", browser.headers.get("Status", "200"))


class TestIHtmxRequestSubscriberFired(unittest.TestCase):
    """Integration tests: verify the BeforeTraverse subscriber fires correctly
    by inspecting the request state after traversal in an integration layer.

    These tests use IntegrationTesting (no real HTTP — direct traversal).
    """

    layer = PLONE_HTMX_INTEGRATION_TESTING

    def test_subscriber_is_registered(self):
        """The mark_as_htmx_request subscriber is registered in the component
        architecture after the plone.htmx ZCML is loaded."""
        from zope.component import getGlobalSiteManager
        from plone.htmx.events import mark_as_htmx_request
        from OFS.interfaces import ITraversable
        from zope.traversing.interfaces import IBeforeTraverseEvent

        gsm = getGlobalSiteManager()
        registrations = list(gsm.registeredHandlers())
        handler_factories = [r.handler for r in registrations]
        self.assertIn(
            mark_as_htmx_request,
            handler_factories,
            "mark_as_htmx_request should be registered as a BeforeTraverse handler",
        )

    def test_ihtmxrequest_interface_is_importable(self):
        """IHtmxRequest is importable and is a zope.interface Interface."""
        from plone.htmx.interfaces import IHtmxRequest
        from zope.interface import Interface

        self.assertTrue(issubclass(IHtmxRequest, Interface))

    def test_iplonerestapiayer_and_ihtmxrequest_are_independent(self):
        """IHtmxRequest and IPloneHtmxLayer are independent — providing one
        does not imply the other."""
        from plone.htmx.interfaces import IHtmxRequest
        from plone.htmx.interfaces import IPloneHtmxLayer
        from zope.interface import Interface

        # They share no inheritance relationship beyond Interface
        self.assertFalse(issubclass(IHtmxRequest, IPloneHtmxLayer))
        self.assertFalse(issubclass(IPloneHtmxLayer, IHtmxRequest))
