Feature: Autocomplete search
    In order to view external recipes,
    I want to search with autocomplete function.


Scenario: Incorrect autocomplete search
    When I write at the autocomplete bar "This is not a recipe :("
    And I click at submit autocomplete button
    Then I'm viewing the 404 error page