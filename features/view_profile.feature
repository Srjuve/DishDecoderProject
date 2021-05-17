Feature: View Profile
    In order to view my profile,
    As a user,
    I want to view the information related to my profile.

Scenario: Trying to see my profile without being logged ###REVISAR###
    Given Exists a User "UsuariTestBehaveNoLoggejat" but it's not logged
    When I'll try to see my profile
    Then I'll receive an error

Scenario: Viewing my profile 
    Given I, as "UsuariTestBehave", am logged in the system
    When I'm going to my profile
    Then I'll bee seeing my profile's information

