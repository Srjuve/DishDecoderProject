Feature: Test register
    In order register an account,
    As non registered user,
    I want to register to an account.

Scenario: User register correctly
    When I register as username "patata1" with mail "test@gmail.com" and password "Exemple123"
    Then I see the login page, i log in with my username "patata1" and password "Exemple123"
    Then It appears my username "patata1"

Scenario: User try to register having an existing account
    Given An account
    When I register with username "patata" with mail "patata@patata.com" and password "Exemple123"
    Then It appears error message "Error al registrar-se"

Scenario: User tries to register introducing a username similar to the password
    When I register with username "Exemple" with mail "test@gmail.com" password "Exemple123"
    Then It appears error message "Error al registrar-se"