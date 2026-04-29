*** Settings ***
Documentation    My saucelab Application
Library    SeleniumLibrary

*** Test Cases ***
SauceDemo Login Testcase
    Open Browser          https://www.saucedemo.com/      ff
    Input Text            id:user-name                    standard_user
    Input Text            name=password                   secret_sauce
    Click Button          name=login-button
    Close Browser
*** Keywords ***
Picking items to the cart
     Open Browser          https://www.saucedemo.com/      ff
    Input Text            id:user-name                    standard_user
    Input Text            name=password                   secret_sauce
    Click Button          name=login-button
    Page Should Contain   Products
    @{list_items}         Get Webelements                xpath://div[@class='inventory_item_name ']
    @{Add_item_cart}      Get Webelements                xpath://button[@class='btn btn_primary btn_small btn_inventory ']
    FOR    ${item}    IN    @{list_items}
        ${text}    Get Text    ${item}

    IF    '${text}' == 'Sauce Labs Bike Light'
        Log To Console     ${text}
        BREAK
        END
    END
    Close Browser

*** Test Cases ***
Adding Items to cart
    Open Browser          https://www.saucedemo.com/      ff
    Input Text            id:user-name                    standard_user
    Input Text            name=password                   secret_sauce
    Click Button          name=login-button
    Page Should Contain   Products
    @{list_items}         Get Webelements                xpath://div[@class='inventory_item_name ']

    FOR    ${item}    IN    @{list_items}
        ${text}    Get Text    ${item}
    
    IF    '${text}' == 'Sauce Labs Bike Light'
        Log To Console     ${text}
        BREAK
        END
    END
    Close Browser

*** Test Cases ***
Picking from cart
    Picking Items To The Cart