Feature: Create recipe
    In order to create a recipe,
    As a logged user,
    I want to create a recipe.

Background:
    Given Exists a user "username" with password "password"
    And Exists the ingredient "Rice" with description "Lorem ipsum description"
    And Exists the ingredient "Meat" with description "Lorem ipsum description"
    And Exists the Nutrient "Nutrient1"
    And Ingredient "Rice" that contains "1.00" units of the Nutrient with name "Nutrient1"
    And Ingredient "Meat" that contains "1.00" units of the Nutrient with name "Nutrient1"
    And I am on main page

Scenario: Logged user creates recipe
    Given I click on the login button
    And I login as user "username" with password "password"
    When I click on create recipe button
    And I fill the name of the recipe "Paella"
    And I fill the steps of the recipe "#Lorem#Ipsum#Dolor#Sit#Amet"
    And I add the ingredient "Rice" with quantity "250"
    And I add the ingredient "Meat" with quantity "42"
    And I finish recipe
    Then I can see recipe name "Paella" with author username "username"
    And I can see recipe steps "#Lorem#Ipsum#Dolor#Sit#Amet"
    And I can see recipe ingredient "Rice" with quantity "250.00g"
    And I can see recipe ingredient "Meat" with quantity "42.00g"
    And I can see recipe nutrient "Nutrient1" with quantity "2.92g"

Scenario: Unlogged user creates recipe
    When I click on create recipe button
    Then I stay at "/login/?next=/createrecipe/"

Scenario: Logged user creates invalid recipe
    Given I click on the login button
    And I login as user "username" with password "password"
    When I click on create recipe button
    And I finish recipe
    Then I stay at "/createrecipe/"
