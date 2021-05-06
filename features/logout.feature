Feature: Logout Account
    In order to logout from an account,
    As a logged user,
    I have to logout from my account.

Background: There is a user registered on DB
    Given Exists a user "usr" with password "password"

Scenario: User logout succesfully
    When I login as user "usr" with password "password"
    And I click on logout button
    Then I logout from the account