*** Keywords ***
v_App_Not_Started
    Log To Console    Application started

v_Home_Page
    Wait Until Page Contains Element  id=about-btn
    ${url}  Get Location
    Should Match  ${url}  http://app.matglad.nu/#/startview

v_Settings_Page
    Wait Until Page Contains Element  id=num-portions-list
    ${url}  Get Location
    Should Match  ${url}  http://app.matglad.nu/#/settings

v_Recipe_page
    Wait Until Page Contains Element  //*[@id="recipe-categories-container"]/collection-view/ul/li[14]/a/div/div
    ${url}  Get Location
    Should Match  ${url}  http://app.matglad.nu/#/recipe-categories

v_About_Page
    Wait Until Page Contains  För mer information om MatGlad
    ${url}  Get Location
    Should Match  ${url}  http://app.matglad.nu/#/about-view

v_Soup_Page
    Wait Until Page Contains  Gazpacho

v_Fish_page
    Wait Until Page Contains  Pestofisk i paket

v_Meat_Page
    Wait Until Page Contains  Biff med potatisgratäng
