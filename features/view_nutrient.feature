Feature: View Nutrient
    In order to view a nutrient,
    As a user,
    I want to view the information related to a nutrient.

Scenario: View Nutrient
    Given Exists a nutrient id "1"
    When I search the nutrient id "1"
    Then I'm viewing the details page for the nutrient id

Scenario: View Nutrient without Description
    Given Exists a nutrient id "2" without description
    When I search the nutrient id "2" without description
    Then I'm viewing the details page for the nutrient without description

Scenario: Trying to view a nonexistent Nutrient
    When I try to search the nutrient id "3" which doesn't exist
    Then I'm expecting to receive an error

