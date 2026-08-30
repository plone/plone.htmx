# -*- coding: utf-8 -*-
"""plone.testing layers for plone.htmx.

Uses PloneWithPackageLayer — the standard plone.app.testing helper for
single-package add-ons — to avoid boilerplate layer subclassing.

Provides two layers:

PLONE_HTMX_INTEGRATION_TESTING
    Full Plone site with the plone.htmx:default profile installed.
    Use for integration tests that need a real Plone site.

PLONE_HTMX_FUNCTIONAL_TESTING
    Same fixture but with a transaction-isolated functional test client.
    Use for tests that need to make real HTTP requests through the publisher.
"""
import plone.htmx

from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneWithPackageLayer


PLONE_HTMX_FIXTURE = PloneWithPackageLayer(
    bases=(PLONE_FIXTURE,),
    name="PloneHtmxLayer:Fixture",
    module=__name__,
    zcml_filename="testing.zcml",
    zcml_package=plone.htmx,
    gs_profile_id="plone.htmx:default",
)

PLONE_HTMX_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_HTMX_FIXTURE,),
    name="PloneHtmxLayer:Integration",
)

PLONE_HTMX_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_HTMX_FIXTURE,),
    name="PloneHtmxLayer:Functional",
)
