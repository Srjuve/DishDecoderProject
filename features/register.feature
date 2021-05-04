Feature: Test register
    In order register an account,
    As non registered user,
    I want to register to an account.

Scenario: Register without problems
    Given Exist an username "patata",and a mail "patata@patata.com", and a password "Exemple123"
    When I click the register button
    Then I'm viewing the login page
