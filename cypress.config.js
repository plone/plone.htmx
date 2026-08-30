const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // add node event listeners here
    },
    env: {
      PLONE_HOST: "localhost:8080",
    },
  },
});
