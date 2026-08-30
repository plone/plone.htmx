# -*- coding: utf-8 -*-
from zope.interface import Interface


class IPloneHtmxLayer(Interface):
    """Marker interface that defines a ZTK browser layer. We can reference
    this in the 'layer' attribute of ZCML <browser:* /> directives to ensure
    the relevant registration only takes effect when this theme is installed.

    The browser layer is installed via the browserlayer.xml GenericSetup
    import step.
    """


class IHtmxRequest(Interface):
    """Marker interface applied to requests that carry the HX-Request: true header.

    When a browser makes a request via HTMX, this header is set automatically.
    A BeforeTraverse subscriber marks the request with this interface so that
    HTMX-specific fragment views can be registered on this layer and will
    take precedence over full-page views for the same URL.

    This allows HTMX fragment views to coexist with both the Plone REST API
    (IPloneRestapiLayer) and the classic full-page views on the same URLs —
    distinguished purely by the HX-Request request header.
    """
