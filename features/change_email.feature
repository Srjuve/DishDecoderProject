Feature: Change Email
    In order to change the email of an account,
    As a logged user,
    I want to change my email.


Background: 
    Given Exists a user "username" with password "password" 
    And I click on the login button
    And I login as user "username" with password "password"
    And I click on profile button


Scenario: Change old email with valid new email
    When I click on change email button
    And I fill the camps with my new email "dummy@dummy.com"
    Then I click on change email button
    And I fill the camps with my the same email "dummy@dummy.com"
    And It appears error message "Invalid data entered"

Scenario: Change old email with invalid new email
    When I click on change email button
    And I fill the camps with my new email "dummy@com"
    Then It appears error message "Invalid data entered"