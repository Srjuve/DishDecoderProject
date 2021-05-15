Feature: View Recipe
    In order to view a recipe,
    As a user,
    I want to view the information related to a recipe.

Background: 
    Given Exists a user "username" with password "password" 

Scenario: View Recipe without comments
    Given Exists a recipe "Recipe1" created by "username"
    And Exists the ingredient "Ingredient1"
    And Exists the Nutrient "Nutrient1"
    And Recipe "Recipe1" contains "1.00" units of the Ingredient with name "Ingredient1"
    And Ingredient "Ingredient1" that contains "1.00" units of the Nutrient with name "Nutrient1" 
    When I search the recipe with name "Recipe1"
    Then I'm viewing the details page for the recipe with name "Recipe1" without the comments


Scenario: View non existent Recipe
    When I search a recipe with a not existent id
    Then I'm viewing the 404 error page