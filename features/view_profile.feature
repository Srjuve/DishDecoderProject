Feature: View Profile
    In order to view my profile,
    As a user,
    I want to view the information related to my profile.

Background:
    Given Exists a user "UsuariTestBehave" with password "Exemple123"


Scenario: Trying to see my profile without being logged
    When I'll try to see my profile through the url
    Then I'll be redirected to the login page

Scenario: Viewing my profile 
    Given I click on the login button
    And I login as user "UsuariTestBehave" with password "Exemple123"
    When I click on profile button
    Then I'll see the user's profile's information.

Scenario: Viewing the profile of a user who has a recipe
    Given I click on the login button
    And I login as user "UsuariTestBehave" with password "Exemple123"
    And I made the recipe "TestRecipeYummy"
    When I click on profile button
    Then I, as user "UsuariTestBehave", will also see some details about his/her recipe "TestRecipeYummy"

Scenario: Viewing the profile of a user who made a rating
    
    Given I click on the login button
    And I login as user "UsuariTestBehave" with password "Exemple123"
    And Exists a user "ElChefNuestro" with password "CuinerCasaNostra123"
    And Exists a recipe "RatedRecipe" created by "ElChefNuestro"
    And I made a rating "NiceRate" on the recipe "RatedRecipe"
    When I click on profile button
    Then The user "UsuariTestBehave" will also see some details about his/her rating "NiceRate" on the recipe "RatedRecipe" made by the other user "ElChefNuestro"