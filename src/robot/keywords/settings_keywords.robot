*** Keywords ***
Begin Webtest
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window

Reset Api
    Reset Rest Api

End Webtest
    Reset Api
    Close All Browsers
