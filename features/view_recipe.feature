Feature: View Recipe
    In order to view a recipe,
    As a user,
    I want to view the information related to a recipe.

Scenario: View Recipe
    Given Exists a recipe id "1" created by the User "Usuari1"
    When I search the recipe id "1"
    Then I'm viewing the details page for the recipe id