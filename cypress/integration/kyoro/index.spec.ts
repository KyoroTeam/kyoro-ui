beforeEach(() => {
  cy.visit("http://localhost:5000");
});

describe("kyoro index page", () => {
  it("contains the website header", () => {
    cy.get("main").children("h1").first().should("have.text", "Hello Kyoro!");
  });
});
