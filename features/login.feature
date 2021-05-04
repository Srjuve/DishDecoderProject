Feature: Login Account
    In order to login to an account,
    As a non logged user,
    I want to login to an account.

Background: There is user registerd on DB
    Given Exists a user "username" with password "password" 
    And I click on the login button

Scenario: Users login correctly
    When I login as user "username" with password "password"
    Then It appears my username "username"


Scenario: User tries to login with invalid username
    When I login as user "foo" with password "password"
    Then Login credentials invalid