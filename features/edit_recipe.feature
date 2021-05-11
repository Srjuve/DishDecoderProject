Feature: View Recipe
    In order to edit a Recipe,
    As a user,
    I want to change the related data and check if the corresponding change has taken effect.

Background: 
    Given Exists a user "username" with password "password"
    And Exists a recipe id "1" created by the User "username" with "1.00" units of the the Ingredient with id "1" that contains "1.00" units of the Nutrient with id "1"
    And Exists a Ingredient with id "2" that contains "1.00" units of the Nutrient ith id "2"
    And I am on main page

Scenario: Logged user edit Recipe name
    Given I click on the login button
    And I login as user "username" with password "password"
    When I click the edit recipe button
    And I fill the recipe name form with the new name "Nom1"
    And I click the button to change the name
    Then I can see that the recipe has the name "Nom1"

Scenario: Logged user edit steps
    Given I click on the login button
    And I login as user "username" with password "password"
    When I click the edit recipe button
    And I fill the steps form with the steps "Pas1"
    And I click the button to change the steps
    Then I can see that the steps are "Pas1"
    

Scenario: Logged user edit Ingredients
    Given I click on the login button
    And I login as user "username" with password "password"
    When I click the edit recipe button
    And I add "1.00" units of the Ingredient with id "2"
    And I click the button to add the Ingredients
    Then I can see the Ingredients data
