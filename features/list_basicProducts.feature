Feature: View list of BasicProducts
    In order to see a list of BasicProducts,
    As user,
    I want to see a list of BasicProducts.

Scenario: User search BasicProducts
    Given A BasicProduct with id "1" and a BasicProduct id "2"
    When I click BasicProducts and i search products and i click search
    Then I see ingredients

Scenario: User search for a non existent BasicProduct
    When I search for a basic product that not exist
    Then It appears error message "No Data Found"