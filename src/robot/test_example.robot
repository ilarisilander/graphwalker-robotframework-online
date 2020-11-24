*** Settings ***
Documentation  Example test to showcase the GraphWalker/RobotFramework RESTful system
Library  Selenium2Library
Library  scripts/getNext.py
Library  scripts/restart.py
Library  scripts/communicator.py
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

# This for loop is like a while loop (999999 iterations).
# It ends if ${i} reaches the maximum amount of iterations.
# Calls a function called "get_next()" in the getNext python script and saves the return value in ${next_step}.
# The return value can either be a vertex/edge name from the model or it can be "false".
# If the return value is false (no more steps in the model) then the loop ends.
# If the variable holds the name of a step, then it will run a keyword with the same name if it exists in the keyword file.

*** Test Cases ***
Test Matglad Model On The Actual Website
    Set Selenium Speed  0.1
    FOR  ${i}  IN RANGE  ${RANGE}
        Exit For Loop If  ${i} == ${RANGE}
        ${next_step}=  Get Next
        Run Keyword If  '${next_step}' == 'false'  Exit For Loop
        Run Keyword  ${next_step}
    END
