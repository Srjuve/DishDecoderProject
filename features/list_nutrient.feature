Feature: View list of Nutrients
    In order to see a list of nutrients,
    As user,
    I want to see a list of nutrients.

Scenario: User search nutrients
    Given A nutrient with id "1" and a nutrient with id "2"
    When I click nutrients and i search nutrient and i click search
    Then I'm seeing a list

Scenario: User search for an inexistent recipe
    When I search for a nutrient that not exist
    Then It appears error message "No Data Found"