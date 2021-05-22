Feature: View Recipe
    In order to view a recipe,
    As a user,
    I want to view the information related to a recipe.

Background: 
    Given Exists a user "username" with password "password" 

Scenario: View Recipe without comments
    Given Exists a recipe "Recipe1" created by "username" with steps "lorem#ipsum#steps"
    And Exists the ingredient "Ingredient1" with description "Lorem ipsum description"
    And Exists the Nutrient "Nutrient1" with the description "Description1"
    And Recipe "Recipe1" contains "1.00" units of the Ingredient with name "Ingredient1"
    And Ingredient "Ingredient1" that contains "1.00" units of the Nutrient with name "Nutrient1" 
    When I search the recipe with name "Recipe1"
    Then I can see recipe name "Recipe1" with author username "username"
    And I can see recipe steps "lorem#ipsum#steps"
    And I can see recipe ingredient "Ingredient1" with quantity "1.00g"
    And I can see recipe nutrient "Nutrient1" with quantity "0.01g"

Scenario: View non existent Recipe
    When I search the recipe with id "666"
    Then I'm viewing the 404 error page