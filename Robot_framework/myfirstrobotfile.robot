*** Settings ***
Documentation    My first robot Testcase
Library    SeleniumLibrary

*** Test Cases ***
Login User with Password
    Open Browser    https://www.saucedemo.com/
    Input Text    name=user-name  standard_user
    Input Text    name=password   secret_sauce
    Click Button    name=login-button
    Close Browser