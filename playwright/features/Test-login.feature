Feature: As a QA,
  I want to test login functionality
  so that I can verify the working of the functionality ( Test Functionality)

#  Scenario: Test login functionality with valid username and password (TestCase)
#    Given User navigates to url
#    When  User enters the username "standard_user"
#    And   User enters the password "secret_sauce"
#    And   I click on login button
#    Then  I should be able to reach dashboard page
#  @positive
#  Scenario Outline: Test login functionality with valid username and password (TestCase)
#    Given User navigates to url
#    When  User enters the username "<username>"
#    And   User enters the password "<password>"
#    And   I click on login button
#    Then  I should be able to reach dashboard page
#    Examples:
#    | username               |  password      |
#    | standard_user          |  secret_sauce |
#    |  locked_out_user       |  secret_sauce |

#   @negative
#   Scenario Outline: Test login functionality with wrong credentials(TestCase)
#    Given User navigates to url
#    When  User enters the username "<username>"
#    And   User enters the password "<password>"
#    And   I click on login button
#    Then  I should be able to reach dashboard page
#    Examples:
#    | username                |  password      |
#    | standard_users          |  secret_sauce |
#    |  locked_out_users       |  secret_sauce |

#   @positive
#  Scenario: Test Adding to cart(TestCase)
#    Given User navigates to url
#    When  User enters the username "standard_user"
#    And   User enters the password "secret_sauce"
#    And   I click on login button
#    And   User is able to pick item "Sauce Labs Bolt T-Shirt" and click on add to cart button
#    Then  User should be able to verify the item added in the cart

#    Scenario: Test login functionality with valid username and password from excel sheet
#    Given User navigates to url
#    When  User enters the username from excel-sheet
#    And   User enters the password from excel-sheet
#    And   I click on login button
#    Then  I should be able to reach dashboard page


  Scenario: Test login functionality with valid username and password from json files
    Given User navigates to url
    When  User enters the username from json files
    And   User enters the password from json files
    And   I click on login button
    Then  I should be able to reach dashboard page

