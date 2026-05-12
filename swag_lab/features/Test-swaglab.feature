Feature: E-commerce application functionality validation
  As an application user
  I want to validate login, product selection, cart, and checkout workflows
  So that core application functionalities work successfully

  Scenario Outline: Successful login with valid username and password
    Given User navigates to url
    When User enters the username "<username>"
    And User enters the password "<password>"
    And I click on login button
    Then User should be able to reach dashboard page
    Examples:
      | username                      |  password      |
      | standard_user                 |  secret_sauce  |
      | performance_glitch_user       |  secret_sauce  |
      | problem_user                  |  secret_sauce  |

    Scenario:  Login with invalid credentials
      Given User navigates to url
      When User enters the username "standard_users"
      And User enters the password "secret_sauce"
      And I click on login button
      Then User should see login error message

     Scenario: Validate logout functionality
      Given User navigates to url
      When User enters the username "standard_user"
      And User enters the password "secret_sauce"
      And I click on login button
      And User clicks on the menu button
      And User clicks on the logout button
      Then User should be redirected to Swag Labs login page

     Scenario: Verify cart icon visibility after successful login
      Given User navigates to url
      When User enters the username "standard_user"
      And User enters the password "secret_sauce"
      And I click on login button
      Then User should be able to view the cart icon

      Scenario: Add selected products to cart and validate
        Given User navigates to url
        When User enters the username "standard_user"
        And User enters the password "secret_sauce"
        And I click on login button
        And User randomly selects four available products
        Then User should be able to view the cart icon

     Scenario: Add selected products to cart and navigate to cart page
       Given User navigates to url
       When User enters the username "standard_user"
       And User enters the password "secret_sauce"
       And I click on login button
       And User randomly selects four available products
       When User clicks on the cart button
       Then Cart page should be displayed successfully


     Scenario: Complete checkout and validate order
       Given User navigates to url
       When User enters the username "standard_user"
       And User enters the password "secret_sauce"
       And I click on login button
       And User randomly selects four available products
       When User clicks on the cart button
       Then Cart page should be displayed successfully
       When User clicks on the checkout button
       And User enters the checkout details and enters the continue button
       Then User should receive a confirmation upon completion

     Scenario: Validate sorting functionality on the products page
      Given User navigates to url
      When User enters the username "standard_user"
      And User enters the password "secret_sauce"
      And I click on login button
      And User should be able to click on sort_container button
      And User selects "Price (low to high)" from dropdown
      Then Products should be sorted by price from low to high

     Scenario: Validate "Reset App State" functionality
      Given User navigates to url
      When User enters the username "standard_user"
      And User enters the password "secret_sauce"
      And I click on login button
      And User clicks on the menu button
      And User click on the Reset app state
      Then Application state should be reset successfully

