Feature: Comment a receipe
    In order to comment a receipe,
    As a logged user,
    I want to comment the receipe.

Background: 
    Given Exists a user "username" with password "password" 
    And Exists a user "username2" with password "password"
    And Exists a recipe "Recipe1" created by "username"
    And Exists the ingredient "Ingredient1"
    And Exists the Nutrient "Nutrient1"
    And Recipe "Recipe1" contains "1.00" units of the Ingredient with name "Ingredient1"
    And Ingredient "Ingredient1" that contains "1.00" units of the Nutrient with name "Nutrient1" 

Scenario: Leave a comment in a receipe
    Given I click on the login button
    And I login as user "username2" with password "password"
    When I search the recipe with name "Recipe1"
    And I fill the comment with "bo" with rate "8"
    And I click on summit comment button
    Then I view the comment in the recipe with name "Recipe1" by "username2"

Scenario: Not logged user tries to comment
    When I search the recipe with name "Recipe1"
    And I fill the comment with "bo" with rate "8"
    And I click on summit comment button
    Then I'll be redirected, requiring me to log in