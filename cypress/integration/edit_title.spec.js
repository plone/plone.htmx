describe('HTMX view', () => {
  const host = Cypress.env('PLONE_HOST') || 'localhost:8080'

  beforeEach(() => {
    // Set auth cookie for admin:admin (base64 of "admin:admin")
    cy.setCookie('__ac', 'NjE2NDZkNjk2OTNhNjE2NDZkNjk2OQ==')
  })

  it('Edit title and cancel', () => {
    cy.visit(`http://${host}/Plone/news/htmx_view`)
    cy.contains('Edit title').click()
    cy.get('input[name="title"]').should('have.focus')
    cy.contains('Cancel').click()
    cy.contains('News')
  })

  it('Edit title and save', () => {
    cy.visit(`http://${host}/Plone/news/htmx_view`)
    cy.contains('Edit title').click()
    cy.get('input[name="title"]').should('have.focus')
    cy.get('input[name="title"]').type('{selectall}Cypress')
    cy.contains('Save').click()
    cy.get('#breadcrumbs-current').contains('Cypress')
    cy.contains('Cypress')
    // Restore original title
    cy.contains('Edit title').click()
    cy.get('input[name="title"]').should('have.focus')
    cy.get('input[name="title"]').type('{selectall}News')
    cy.contains('Save').click()
  })
})
