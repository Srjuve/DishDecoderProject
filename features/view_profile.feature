Feature: View Profile
    In order to view my profile,
    As a user,
    I want to view the information related to my profile.

Scenario: Trying to see my profile without being logged ###REVISAR###
    Given Exists a User "UsuariTestBehaveNoLoggejat" but it's not logged
    When I,"UsuariTestBehave", try to see my profile
    Then I'll receive an error

Scenario: Viewing my profile ###REVISAR###
    Given Exists a User "UsuariTestBehave" and it's logged 
    When I, "UsuariTestBehave", try to see my profile
    Then I'll bee seeing my profile's information

Scenario: Trying to see my profile while logged but my user is not valid ###NO ENTENC###
    Given Exists a User "NotValidUser" and it's logged 
    When I, "NotValidUser", try to see my profile
    Then I'm expecting to receive an error