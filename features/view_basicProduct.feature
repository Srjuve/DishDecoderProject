Feature: View Basic Product
    In order to view a basic product,
    As a user,
    I want to view the information related to a basic product.

Scenario: View Basic Product
    Given Exists a basic product with id "1" that appears in the recipe with id "1"
    When I search the basic product "1"
    Then I'm viewing the details page for the basic product id "1" and appears the recipe with id "1"

Scenario: View Basic Product without recipe
    Given Exists a basic product with id "2" without recipe
    When I search the basic product with id "2" without recipe
    Then I'm viewing the details page for the basic product with id "2" without recipe

Scenario: Trying to view a non existent Basic Product
    When I try to search the basic product with id "3" which doesn't exist
    Then I'm expecting to recive error "Error 404" with message "The page you are trying to reach does not exist"