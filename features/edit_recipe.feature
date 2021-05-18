Feature: Edit Recipe
    In order to edit a Recipe,
    As a user,
    I want to change the related data and check if the corresponding change has taken effect.

Background: 
    Given Exists a user "username" with password "password"
    And Exists a recipe "Recipe1" created by "username"
    And Exists the ingredient "Ingredient1" with description "Lorem ipsum description"
    And Exists the Nutrient "Nutrient1"
    And Recipe "Recipe1" contains "1.00" units of the Ingredient with name "Ingredient1"
    And Ingredient "Ingredient1" that contains "1.00" units of the Nutrient with name "Nutrient1"
    And Exists the ingredient "Ingredient2" with description "Lorem ipsum description"
    And Exists the Nutrient "Nutrient2"
    And Ingredient "Ingredient2" that contains "1.00" units of the Nutrient with name "Nutrient2"
    And I am on main page
    And I click on the login button
    And I login as user "username" with password "password"


Scenario: Not logged user tries to edit a Recipe
    When I click on logout button 
    And I click the edit recipe button
    Then I stay at "/login/?next=/listedit/"

Scenario: Logged user edit Recipe name
    When I click the edit recipe button
    And I fill the recipe name form with the new name "Nom1"
    And I click the button to change the name
    Then I can see that the recipe has the name "Nom1"

Scenario: Logged user edit steps
    When I click the edit recipe button
    And I fill the steps form with the steps "Pas1"
    And I click the button to change the steps
    Then I can see that the steps are "Pas1"
    

Scenario: Logged user edit Ingredients
    When I click the edit recipe button
    And I add "1.00" units of the Ingredient with name "Ingredient2"
    And I click the button to add the Ingredients
    Then I can see the Ingredient with name "Ingredient2" and quantity "1.00" units


Scenario: Logged user edit Ingredients with repeated Ingredient
    When I click the edit recipe button
    And I add "1.00" units of the Ingredient with name "Ingredient1"
    And I click the button to add the Ingredients
    Then I see the repeated ingredient error

Scenario: Logged user edit Ingredients with negative Ingredient quantity
    When I click the edit recipe button
    And I add "-1.00" units of the Ingredient with name "Ingredient1"
    And I click the button to add the Ingredients
    Then I see the invalid ingredient format error

Scenario: Logged user edit Ingredients with too much quantity
    When I click the edit recipe button
    And I add "1000.00" units of the Ingredient with name "Ingredient1"
    And I click the button to add the Ingredients
    Then I see the quantity value too big error

Scenario: Logged user edit Ingredient erase the only Ingredient
    When I click the edit recipe button
    And I click the button to erase Ingredients
    And I click the button to erase Ingredients
    And I click the button to add the Ingredients
    Then I see the incorrect number of Ingredients exceptions


Scenario: Logged user edit Ingredient erase only one Ingredient
    Given Recipe "Recipe1" contains "1.00" units of the Ingredient with name "Ingredient2"
    When I click the edit recipe button
    And I click the button to erase Ingredients
    And I click the button to erase Ingredients
    And I click the button to add the Ingredients
    Then I see that the only ingredient shown is the ingredient with name "Ingredient1" and quantity "1.00"