*** Settings ***
Documentation    RobotSpareBin industries Application
Library          SeleniumLibrary

*** Keywords ***
Login Using Valid Credentials
    Open Browser                     https://robotsparebinindustries.com/        firefox
    Maximize Browser Window
    Input Text                       name:username                                maria
    Input Text                       name=password                                thoushallnotpass
    Click Button                     xpath://button[@type='submit']

    # Validation (login success)
    Wait Until Element Is Visible    id=logout    10s


    Element Should Be Visible        id=logout
    Close Browser

*** Test Cases ***
Verify User Login Successfully
    Login Using Valid Credentials