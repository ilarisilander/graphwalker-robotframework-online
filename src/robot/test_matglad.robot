*** Settings ***
Documentation  Example test to showcase the GraphWalker/RobotFramework RESTful system
Library  Selenium2Library
Library  scripts/getNext.py
Library  scripts/restart.py
Resource  keywords/edge_keywords.robot
Resource  keywords/vertex_keywords.robot
Resource  keywords/settings_keywords.robot
Test Setup  Begin Webtest
Test Teardown  End Webtest

*** Variables ***
${BROWSER}  chrome
${URL}  http://app.matglad.nu/#/startview
${RANGE}  999999
${FALSE}  false

*** Test Cases ***
Test Matglad Model On The Actual Website
    Set Selenium Speed  0.1
    FOR  ${i}  IN RANGE  ${RANGE}
        Exit For Loop If  ${i} == ${RANGE}
        ${next_step}=  Get Next
        Run Keyword If  '${next_step}' == 'false'  Exit For Loop
        Run Keyword  ${next_step}
    END
