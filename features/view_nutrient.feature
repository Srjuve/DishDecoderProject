Feature: View Nutrient
    In order to view a nutrient,
    As a user,
    I want to view the information related to a nutrient.

Scenario: View Recipe
    Given Exists a nutrient id "1"
    When I search the nutrient id "1"
    Then I'm viewing the details page for the nutrient id