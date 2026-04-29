*** Settings ***
Documentation    SauceDemo Application
Library          SeleniumLibrary

*** Test Cases ***
Login Add Products And Checkout
    Open Browser            https://www.saucedemo.com/    firefox
    Maximize Browser Window
    Input Text              name:user-name                standard_user
    Input Text              name=password                 secret_sauce
    Click Button            id=login-button
    Page Should Contain    Products

    Click Element    xpath://div[normalize-space()='Sauce Labs Bike Light']/ancestor::div[@class='inventory_item']//button


    Click Element    xpath://div[normalize-space()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button
    Click Element    xpath://div[normalize-space()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item']//button

    #  Verify cart count (3 items)
    Wait Until Element Is Visible    xpath://span[@class='shopping_cart_badge']
    Element Text Should Be           xpath://span[@class='shopping_cart_badge']    3

    #  Open cart
    Click Element    xpath://a[@class='shopping_cart_link']

    # Verify products in cart
    Page Should Contain    Sauce Labs Bike Light
    Page Should Contain    Sauce Labs Backpack
    Page Should Contain    Sauce Labs Bolt T-Shirt

    # Proceed to checkout
    Click Button    id=checkout

    # Validate checkout page
    Wait Until Element Is Visible    id=first-name

    Close Browser