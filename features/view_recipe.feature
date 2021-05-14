Feature: View Recipe
    In order to view a recipe,
    As a user,
    I want to view the information related to a recipe.

Background: 
    Given Exists a user "username" with password "password" 

Scenario: View Recipe without comments
    Given Exists a recipe id "1" created by the User "username" with "1.00" units of the the Ingredient with id "1" and name "Ingredient1" that contains "1.00" units of the Nutrient with id "1"
    When I search the recipe id "1"
    Then I'm viewing the details page for the recipe id "1" without the comments


Scenario: View non existent Recipe
    When I search the recipe id "101"
    Then I'm viewing the 404 error page