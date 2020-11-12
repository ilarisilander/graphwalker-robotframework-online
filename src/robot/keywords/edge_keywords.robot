*** Keywords ***
e_Begin_Web_Test
    Log To Console    Application started, starting test

e_Settings
    Wait Until Page Contains Element  id=settings-btn
    Click Element  id=settings-btn

e_Back
    Wait Until Page Contains Element  id=back-button
    Click Element  id=back-button

e_Recipe
    Wait Until Page Contains Element  id=recipe-btn
    Click Element  id=recipe-btn

e_About
    Wait Until Page Contains Element  id=about-btn
    Click Element  id=about-btn

e_Soup
    Wait Until Page Contains Element  //*[@id="recipe-categories-container"]/collection-view/ul/li[1]/a/div/img
    Click Element  //*[@id="recipe-categories-container"]/collection-view/ul/li[1]/a/div/img

e_Fish
    Wait Until Page Contains Element  //*[@id="recipe-categories-container"]/collection-view/ul/li[2]/a/div/img
    Click Element  //*[@id="recipe-categories-container"]/collection-view/ul/li[2]/a/div/img

e_Meat
    Wait Until Page Contains Element  //*[@id="recipe-categories-container"]/collection-view/ul/li[3]/a/div/img
    Click Element  //*[@id="recipe-categories-container"]/collection-view/ul/li[3]/a/div/img
