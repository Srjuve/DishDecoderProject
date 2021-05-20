Feature: Test register
    In order register an account,
    As non registered user,
    I want to register to an account.

Scenario: User register correctly
    When I register as username "patata1" with mail "test@gmail.com" and password "Exemple123"
    And I login as user "patata1" with password "Exemple124"
    Then It appears my username "patata1"

Scenario: User try to register having an existing account
    Given An account
    When I register as username "patata" with mail "patata@patata.com" and password "Exemple123"
    Then It appears error message "A user with that username already exists."

Scenario: User tries to register introducing a username similar to the password
    When I register as username "Exemple" with mail "test@gmail.com" and password "Exemple123"
    Then It appears error message "The password is too similar to the username."

Scenario: User tries to put a similar password too short and common
    When I register as username "patata" with mail "test@gmail.com" and password "patata" 
    Then It appears error message "This password is too short. It must contain at least 8 characters."
    And It appears error message "This password is too common."