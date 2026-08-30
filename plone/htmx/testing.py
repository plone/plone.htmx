# -*- coding: utf-8 -*-
"""plone.testing layers for plone.htmx.

Provides two layers:

PLONE_HTMX_INTEGRATION_TESTING
    Full Plone site with the plone.htmx:default profile installed.
    Use for integration tests that need a real Plone site.

PLONE_HTMX_FUNCTIONAL_TESTING
    Same fixture but with a transaction-isolated functional test client.
    Use for tests that need to make real HTTP requests through the publisher.
"""
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
import plone.htmx


class PloneHtmxLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=plone.htmx, name="testing.zcml")

    def setUpPloneSite(self, portal):
        applyProfile(portal, "plone.htmx:default")
        applyProfile(portal, "plone.htmx:testing")


PLONE_HTMX_FIXTURE = PloneHtmxLayer()

PLONE_HTMX_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_HTMX_FIXTURE,),
    name="PloneHtmxLayer:Integration",
)

PLONE_HTMX_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_HTMX_FIXTURE,),
    name="PloneHtmxLayer:Functional",
)
