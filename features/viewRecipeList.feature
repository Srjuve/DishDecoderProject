Feature: View list of recipes
    In order to see a list of recipes,
    As user,
    I want to see a list of recipes.

Scenario: User search recipes
    Given A recipe with id "1" with user "user1" and name "recipe1" and a recipe id "2" with user "user2" and name "recipe2"
    When I click recipe and i search "recipe" and i click search
    Then I see "recipe1" and "recipe2"

Scenario: User search for an inexistent recipe
    When I search for "recipe" that not exist
    Then I see an error "No Data Found"