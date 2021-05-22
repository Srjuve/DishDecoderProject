Feature: Delete Recipe
    In order to delete a recipe,
    As a user,
    I want to delete the information of a recipe.

Background: 
    Given Exists a user "username" with password "password"
    And Exists a recipe "soup" created by "username" with steps "lorem#ipsum#steps"
    And I click on the login button
    And I login as user "username" with password "password"

Scenario: Delete existent recipe
    When I click on erase recipe button
    And I select "soup" for deleting purposes
    Then Recipe "soup" cannot be found in profile


