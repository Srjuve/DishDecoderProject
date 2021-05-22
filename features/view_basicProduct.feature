Feature: View Basic Product
    In order to view a basic product,
    As a user,
    I want to view the information related to a basic product.

Background: 
    Given Exists a user "username" with password "password"
    And Exists a recipe "Recipe1" created by "username" with steps "lorem#ipsum#steps"
    And Exists the ingredient "Ingredient1" with description "Lorem ipsum description"


Scenario: View Basic Product
    Given Recipe "Recipe1" contains "1.00" units of the Ingredient with name "Ingredient1"
    When I search the basic product with name "Ingredient1"
    Then I'm viewing the details page of basic product "Ingredient1" with description "Lorem ipsum description"
    And This basic product details page shows the recipe "Recipe1"

Scenario: View Basic Product without recipe
    When I search the basic product with name "Ingredient1"
    Then I'm viewing the details page of basic product "Ingredient1" with description "Lorem ipsum description"
    And This basic product details page shows no recipe

Scenario: Trying to view a non existent Basic Product
    When I search the basic product with id "666"
    Then I'm expecting to recive error "Error 404" with message "The page you are trying to reach does not exist"