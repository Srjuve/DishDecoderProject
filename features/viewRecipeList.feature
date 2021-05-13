Feature: View list of recipes
    In order to see a list of recipes,
    As user,
    I want to see a list of recipes.

Scenario: User search recipes
    Given A recipe with id "1" created by the user "user1" and a recipe id "2" created by user "user2"
    When I click recipe and i search recipe and i click search
    Then I see a list

Scenario: User search for an inexistent recipe
    When I search for a recipe that not exist
    Then I see an error