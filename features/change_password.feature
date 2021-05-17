Feature: Change Password
    In order to change the password,
    As a user,
    I want to have an option to do it.

Background:
    Given Exists a user "UsuariTestBehave" with password "Exemple123"

Scenario: Changing the password with a logged user
    Given I click on the login button
    And I login as user "UsuariTestBehave" with password "Exemple123"
    When I click on profile button
    And I change my old password "Exemple123" to a new one "prova123"
    Then I'll be able to logging with the username "UsuariTestBehave" and the new password "prova123"

Scenario: Changing the password with a non-logged user
    When I'll try to enter to the site in which I should be able to change my password directly through the url
    Then I'll be redirected since I'm not logged in, requiring me to do it

Scenario: Trying to change the password but giving a wrong one
    Given I click on the login button
    And I login as user "UsuariTestBehave" with password "Exemple123"
    When I click on profile button
    And I introduce my old password as "{ConstrasenyaEquivocada}" and the password that I want as "{123}"
    Then The system will tell me that I entered invalid data