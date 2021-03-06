Feature: View Profile
    In order to view my profile,
    As a user,
    I want to view the information related to my profile.

Background:
    Given Exists a user "UsuariTestBehave" with password "Exemple123"


Scenario: Trying to see my profile without being logged
    When I check my profile through the url
    Then I stay at "/login/?next=/profile/"

Scenario: Viewing my profile 
    Given I click on the login button
    And I login as user "UsuariTestBehave" with password "Exemple123"
    When I click on profile button
    Then I can see my username name "UsuariTestBehave"

Scenario: Viewing the profile of a user who has a recipe
    Given I click on the login button
    And I login as user "UsuariTestBehave" with password "Exemple123"
    And Exists a recipe "TestRecipeYummy" created by "UsuariTestBehave" with steps "lorem#ipsum#steps"
    When I click on profile button
    Then I see in my profile that I made the recipe "TestRecipeYummy"

Scenario: Viewing the profile of a user who made a rating
    
    Given I click on the login button
    And I login as user "UsuariTestBehave" with password "Exemple123"
    And Exists a user "ElChefNuestro" with password "CuinerCasaNostra123"
    And Exists a recipe "RatedRecipe" created by "ElChefNuestro" with steps "lorem#ipsum#steps"
    And I, the user "UsuariTestBehave", made a rating "NiceRate" on the recipe "RatedRecipe"
    When I click on profile button
    Then I, the user "UsuariTestBehave", see my rating "NiceRate" on the recipe "RatedRecipe" made by the other user "ElChefNuestro"