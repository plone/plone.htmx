describe('HTMX view', () => {
  beforeEach(() => {
    cy.setCookie('__ac', 'NjE2NDZkNjk2ZTo2MTY0NmQ2OTZl')
  })

  it('Edit title and cancel', () => {
    cy.visit('http://localhost:8080/Plone/news/htmx_view')
    cy.contains('Edit title').click()
    cy.get('input[name="title"]').should('have.focus')
    cy.contains('Cancel').click()
    cy.contains('News')
  })

  it('Edit title and save', () => {
    cy.visit('http://localhost:8080/Plone/news/htmx_view')
    cy.contains('Edit title').click()
    cy.get('input[name="title"]').should('have.focus')
    cy.get('input[name="title"]').type('{selectall}Cypress')
    cy.contains('Save').click()
    if (Cypress.env('PLONE_VERSION') == '5.1') {
        cy.get('li.selected').contains('Cypress')
    } else {
        cy.get('li.current').contains('Cypress')
    }
    cy.get('#breadcrumbs-current').contains('Cypress')
    cy.contains('Cypress')
    cy.contains('Edit title').click()
    cy.get('input[name="title"]').should('have.focus')
    cy.get('input[name="title"]').type('{selectall}News')
    cy.contains('Save').click()
  })
})

