=======
History
=======

0.3.0 (unreleased)
----------------------------------------------

* Add ``IHtmxRequest`` marker interface (step 1).
* Add ``mark_as_htmx_request`` BeforeTraverse subscriber that applies
  ``IHtmxRequest`` to any request carrying ``HX-Request: true`` (step 2).
* Register the subscriber in ``configure.zcml`` (step 3).
* Add ``plone.htmx.testing`` module with ``PLONE_HTMX_INTEGRATION_TESTING``
  and ``PLONE_HTMX_FUNCTIONAL_TESTING`` layers based on ``plone.app.testing``.
* Add unit tests for the subscriber (no Plone needed).
* Add integration tests verifying subscriber registration and
  ``IHtmxRequest`` behaviour under the full Zope publisher.

0.2.0 (unreleased)
----------------------------------------------

* Update for Plone 6.1 compatibility.
* Bump htmx to 4.0.0.
* Port ``setup.py`` to ``pyproject.toml``.
* Fix test view for Dexterity (``context.title`` attribute instead of ``setTitle()``).
* Port ``cypress.json`` to ``cypress.config.js`` (Cypress 10+ format).
* Bump Cypress dependency to ^15.0.0.

0.1.0 (2021-12-11)
----------------------------------------------

* First release on PyPI.

