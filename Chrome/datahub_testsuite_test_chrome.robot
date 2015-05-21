*** Settings ***



Library  data_hub_chrome.LoginPage
Library  data_hub_chrome.DatahubMenu
Library  data_hub_chrome.ProcessTab
Library  data_hub_chrome.SystemMenu
Library  data_hub_chrome.Datahub
Library  data_hub_chrome.UserSetup
Library  data_hub_chrome.Partners
Library  data_hub_chrome.Endpoints
Library  data_hub_chrome.Messages
Library  data_hub_chrome.Routes
Library  data_hub_chrome.LogsMenu
Library  data_hub_chrome.ApplicationLog
Library  data_hub_chrome.SQLLog
Library  data_hub_chrome.AccessLog
Library  data_hub_chrome.ProcessTab
Library  data_hub_chrome.ProcessLastRun
Library  data_hub_chrome.ProcessLog
Library  data_hub_chrome.ProcessRun
Library  data_hub_chrome.ProcessLastRun
Library  data_hub_chrome.ProcessNotProcessed
Library  data_hub_chrome.ProcessDependencies
Library  data_hub_chrome.ProcessRunDependency

*** Test Cases ***


Datahub Process Dependencies
    Open DatahubApp
    Login to datahub
    Click process dependencies
    Verify text in process run dependency
    [Teardown]  Close DatahubApp

Datahub process run dependency
    Open DatahubApp
    Login to datahub
    Click Process
    Verify text in Process tab
    [Teardown]  Close DatahubApp


Datahub Process
    Open DatahubApp
    Login to datahub
    Click Process
    Verify text in Process tab
    #Close Process tab
    [Teardown]  Close DatahubApp

Datahub Process run
    Open DatahubApp
    Login to datahub
    Click Process Run
    Verify text in processrun
    #Close Process Run tab
    [Teardown]  Close DatahubApp

Datahub Process Last Run
    Open DatahubApp
    Login to datahub
    Click Process LastRun
    Verify text in Processlastrun
    #Close Process Last Run tab
    [Teardown]  Close DatahubApp

Datahub Process Log
    Open DatahubApp
    Login to datahub
    Click Process Log
    Verify text in Processlog
    #Close Process Log tab
    [Teardown]  Close DatahubApp

Datahub Process Not Processed
    Open DatahubApp
    Login to datahub
    Click process not processed
    Verify text in process not processed
    #Close process Not Processed tab
    [Teardown]  Close DatahubApp

Datahub Process Run Dependencies
    Open DatahubApp
    Login to datahub
    Click process run dependencies
    Verify text in process run dependency
    #Close Process Run Dependencies tab
    [Teardown]  Close DatahubApp

System Usersetup
    Open DatahubApp
    Login to datahub
    Navigate to other menu           #System
    Toggle system menu
    Click Users
    Click Usersetup
    Verify text in usersetup
    [Teardown]  Close DatahubApp

System Messages
    Open DatahubApp
    Login to datahub
    Navigate to other menu           #System
    Toggle system menu
    Click Connections
    Click Message
    Verify text in messages
    [Teardown]  Close DatahubApp

System Routes
    Open DatahubApp
    Login to datahub
    Navigate to other menu           #System
    Toggle system menu
    Click Connections
    Click Routes
    Verify text in routes
    [Teardown]  Close DatahubApp

System Partners
    Open DatahubApp
    Login to datahub
    Navigate to other menu           #System
    Toggle system menu
    Click Connections
    Click Partners
    Verify text in partners
    [Teardown]  Close DatahubApp

System Endpoints
    Open DatahubApp
    Login to datahub
    Navigate to other menu           #System
    Toggle system menu
    Click Connections
    Click Endpoints
    Verify text in endpoints
    #Close Process Dependencies table
    [Teardown]  Close DatahubApp

Logs Applicationlog
    Open DatahubApp
    Login to datahub
    Navigate to other menu           #Application log
    Toggle logs menu
    Click application log
    Verify text in application log
    [Teardown]  Close DatahubApp

Logs Accesslog
    Open DatahubApp
    Login to datahub
    Navigate to other menu           #Application log
    Toggle logs menu
    Click access log
    Verify text in accesslog
    [Teardown]  Close DatahubApp

Logs SQLlog
    Open DatahubApp
    Login to datahub
    Navigate to other menu           #Application log
    Toggle logs menu
    Click sql log
    Verify text in sqllog
    [Teardown]  Close DatahubApp

*** Keywords ***
Login to datahub
    data_hub_chrome.LoginPage.Go to datahub
    Type in credential
    Click submit credential


#1. Reset button
#2. Process list


























































#*** Comment ***

#Datahub Process
#    Login to datahub
#    Click Process
#    Verify text in Process tab

#Datahub Process run
#    Login to datahub
#    Click Process Run
#    Verify text in processrun

#Datahub Process Last Run
    #Login to datahub
    #Click Process Last Run
    #Verify text in Processlastrun

#Datahub Process: Filter Process description
  #  Login to datahub
  #  Click Process
  #  Type input process name     #clean%
  #  Click retreive data
  #  #Verify process description filter
   # Get all process
   # Click Add Button

#Datahub Process: verify gridcolumn headers are fine and filter works
#    Login to datahub
#    Click Process
#    Toggle Column
#    Toggle Column
#    Type input process description     #clean%
#    Click retreive data
#    #Verify process description filter
#    Get all process
#    Click Retreive Button
























































#*** Comment ***

#Datahub Process: Filter Process description
  #  Login to datahub
  #  Click Process
  #  Type input process name     #clean%
  #  Click retreive data
  #  #Verify process description filter
   # Get all process
   # Click Add Button
