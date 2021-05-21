Feature: View list of Nutrients
    In order to see a list of nutrients,
    As user,
    I want to see a list of nutrients.

Scenario: User search nutrients
    Given Exists the Nutrient "nutrient1" with the description "Description1"
    And Exists the Nutrient "nutrient2" with the description "Description2"
    When I search for a nutrient with name "nutrient"
    Then I can see the nutrient "nutrient1"
    And I can see the nutrient "nutrient2"

Scenario: User search for an inexistent recipe
    When I search for a nutrient with name "nutrient"
    Then It appears error message "No Data Found"