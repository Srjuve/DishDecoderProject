Feature: Login Account
    In order to login to an account,
    As a non logged user,
    I want to login to an account.

Background: There is user registerd on DB
    Given Exists a user "usr" with password "password" 
    And I click on the login button

Scenario: Users login correctly
    Given I login as user "usr" with password "password"
    Then It appears my username "usr"


Scenario: User tries to login with invalid username
    Given I login as user "foo" with "password"
    Then Login credentials invalid