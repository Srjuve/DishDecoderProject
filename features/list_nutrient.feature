Feature: View list of Nutrients
    In order to see a list of nutrients,
    As user,
    I want to see a list of nutrients.

Scenario: User search nutrients
    Given Exists a nutrient with name "nutrient1"
    And Exists a nutrient with name "nutrient2"
    When I search for a nutrient with name "nutrient"
    Then I can see the nutrient "nutrient1"
    And I can see the nutrient "nutrient2"

Scenario: User search for an inexistent recipe
    When I search for a nutrient with name "nutrient"
    Then It appears error message "No Data Found"