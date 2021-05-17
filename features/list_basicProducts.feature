Feature: View list of BasicProducts
    In order to see a list of BasicProducts,
    As user,
    I want to see a list of BasicProducts.

Scenario: User search BasicProducts
    Given Exists the ingredient "Ingredient1" with description "Lorem ipsum description1"
    And Exists the ingredient "Ingredient2" with description "Lorem ipsum description2"
    When I search for a basic product with name "Ingredient"
    Then I see basic product "Ingredient1"
    And I see basic product "Ingredient2"

Scenario: User search for a non existent BasicProduct
    When I search for a basic product with name "Ingredient"
    Then It appears error message "No Data Found"