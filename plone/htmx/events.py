# -*- coding: utf-8 -*-
from plone.htmx.interfaces import IHtmxRequest
from zope.interface import alsoProvides


def mark_as_htmx_request(event):
    """BeforeTraverse subscriber.

    If the request carries the ``HX-Request: true`` header (set automatically
    by the HTMX library on every request it makes), mark the request with
    ``IHtmxRequest`` so that HTMX fragment views are looked up in preference
    to full-page views.

    This mirrors the pattern used by ``plone.rest``'s
    ``subscriber_mark_as_api_request``, but keyed on the HX-Request header
    rather than the Accept header.
    """
    request = event.request
    if request.getHeader("HX-Request") == "true":
        alsoProvides(request, IHtmxRequest)
