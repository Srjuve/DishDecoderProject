Feature: Comment a receipe
    In order to comment a receipe,
    As a logged user,
    I want to comment the receipe.

Background: 
    Given Exists a user "username" with password "password" 
    And Exists a user "username2" with password "password" 

Scenario: Leave a comment in a receipe
    Given I click on the login button
    And I login as user "username2" with password "password"
    And Exists a recipe id "1" created by the User "username" with "1.00" units of the the Ingredient with id "1" and name "Ingredient1" that contains "1.00" units of the Nutrient with id "1"
    When I search the recipe id "1"
    And I fill the comment with "bo" with rate "8"
    And I click on summit comment button
    Then I view the recipe "1" with comments by "username2"
Scenario: Not logged user tries to comment
    Given Exists a recipe id "1" created by the User "username" with "1.00" units of the the Ingredient with id "1" and name "Ingredient1" that contains "1.00" units of the Nutrient with id "1"
    When I search the recipe id "1"
    And I fill the comment with "bo" with rate "8"
    And I click on summit comment button
    Then I am redirected to the login page