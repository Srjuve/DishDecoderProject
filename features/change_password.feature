Feature: Change Password
    In order to change the password,
    As a user,
    I want to have an option to do it.

Scenario: Changing the password with a logged user
    Given Exists a User "LoggedThahWillChange" but it's not logged
    When I change my password
    Then I'll receive a message showing me that I did it correctly

Scenario: Changing the password with a non-logged user
    Given I, as a non-logged user, will try to change a password in the system
    When I'll try to enter to the site with that functionality
    Then I'll recieve an error, not allowing me to do it

Scenario: Trying to change the password but giving a wrong one
    Given I, as "FailureUser", am logged in the system
    When I'm going to change my password and fail
    Then I'll recieve an error, it will tell me that I failed in something