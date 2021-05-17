Feature: View Recipe
    In order to view a recipe,
    As a user,
    I want to view the information related to a recipe.

Background: 
    Given Exists a user "username" with password "password"
    And Exists a recipe "soup" created by "username"
    And I click on the login button
    And I login as user "username" with password "password"

Scenario: Delete existent recipe
    When I click on erase recipe button
    And I select "soup" for deleting purposes
    Then Recipe "soup" cannot be found in profile


