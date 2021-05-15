Feature: View list of recipes
    In order to see recipes,
    I want to search for a list of recipes.

Background: 
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"

Scenario: User search recipes
    Given Exists a recipe "recipe1" created by "user1"
    And Exists a recipe "recipe2" created by "user2"
    When I search for a recipe with name "recipe"
    Then I can see the recipe "recipe1"
    And I can see the recipe "recipe2"

Scenario: User search for an inexistent recipe
    When I search for a recipe with name "recipe"
    Then It appears error message "No Data Found"
