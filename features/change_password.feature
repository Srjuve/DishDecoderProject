Feature: Change Password
    In order to change the password,
    As a user,
    I want to have an option to do it.

Scenario: Changing the password with a logged user
    Given Exists a User "RegisteredUser" and I'm logged with it
    When I go to my profile and change my password "prova123"
    Then I'll be able to logging with the username "RegisteredUser" and the new password "prova123"

Scenario: Changing the password with a non-logged user
    Given Exists a User "RegisteredUser" but I'm not logged
    When I'll try to enter to the site in which I should be able to change my password
    Then I'll be redirected, requiring me to log in

Scenario: Trying to change the password but giving a wrong one
    Given Exists a User "FailureUser" with which I'm logged in
    When I'm going to change my password and fail
    Then The system will tell me that I entered invalid data