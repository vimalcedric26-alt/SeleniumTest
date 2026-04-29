Feature: As a QA,
  I want to Test Login Functionality for Zen portal
  so that I can verify the working of the login and logout functionality

Scenario: Test login functionality with valid username and password
  Given User navigates to url
  When User enters username "vimalcedric26@gmail.com"
  And  User enters password "Cassy@091124"
  And  Click on Login button
  And  Click on profile button
  Then User should be able to click on logout button