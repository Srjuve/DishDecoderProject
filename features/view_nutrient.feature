Feature: View Nutrient
    In order to view a nutrient,
    As a user,
    I want to view the information related to a nutrient.

Scenario: View Nutrient
    Given Exists a nutrient id "1" with the name "Nutrient1" and the description "Nutrient made for the behaviour test"
    When I search the nutrient id "1"
    Then I'm viewing the page for the nutrient "Nutrient1"
    And I can also see the description "Nutrient made for the behaviour test"

Scenario: View Nutrient without Description
    Given Exists a nutrient id "2" with the name "Nutrient2" but without description
    When I search the nutrient id "2"
    Then I'm viewing the page for the nutrient "Nutrient2"
    And I can see that there's no description

Scenario: Trying to view a nonexistent Nutrient
    When I try to search the nutrient id "3" which doesn't exist
    Then I'm expecting to receive an error

