Feature: Create recipe
    In order to create a recipe,
    As a logged user,
    I want to create a recipe.

Background:
    Given Exists a user "username" with password "password"
    And Exists the ingredient "rice"
    And Exists the ingredient "meat"

Scenario: Logged user creates recipe
    Given I click on the login button
    And I login as user "username" with password "password"
    When I click on create recipe button
    And I fill the name of the recipe "Paella"
    And I fill the steps of the recipe "#Lorem#Ipsum#Dolor#Sit#Amet"
    And I add the ingredient "rice" with quantity "250"
    And I add the ingredient "meat" with quantity "42"
    And I finish recipe
    Then I can see recipe name "Paella" with author username "username"
    And I can see recipe steps "#Lorem#Ipsum#Dolor#Sit#Amet"
    And I can see recipe ingredient "rice" with quantity "250.000g"
    And I can see recipe ingredient "meat" with quantity "42.000g"

Scenario: Unlogged user creates recipe
    Then pepito

Scenario: Logged user creates invalid recipe
    Given I click on the login button
    And I login as user "username" with password "password"
