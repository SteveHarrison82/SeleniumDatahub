*** Settings ***

#Library  data_hub.ExtJSHelper
Library  data_hub.LoginPage
Library  data_hub.DatahubMenu
Library  data_hub.ProcessTab
Library  data_hub.Datahub
Library  data_hub.ProcessTab
Library  data_hub.ProcessLastRun
Library  data_hub.ProcessLog
Library  data_hub.ProcessRun
Library  data_hub.ProcessLastRun
Library  data_hub.ProcessNotProcessed
Library  data_hub.ProcessDependencies
Library  data_hub.ProcessRunDependency

*** Test Cases ***

Datahub: Verify filter in *any* of the datahub menu
    Open DatahubApp
    Login to datahub
    Click link in datahub menu                     menu_name             Process
    Input text into filter                         column_name           #value
    Verify filter
    close active tab
    [Teardown]  Close DatahubApp

Datahub Process: Verify the filter 'Process Name'

    Open DatahubApp
    Login to datahub
    Click Process
    Input text into filter                         column_name=            text_input=
    Verify Filter                                  column_name=            text_input=
    Close Process tab
    [Teardown]  Close DatahubApp


Datahub: Toggle the column in *any* of the datahub menu

    Open DatahubApp
    Login to datahub
    Click link in datahub menu
    Toggle table column                            column_name           Process Name
    Verify column                                  column_name           Process Name         Exist      True
    Toggle table column                            column_name           Process Name
    Verify column                                  column_name           Process Name         Exist      False
    Close active tab
    [Teardown]  Close DatahubApp


Datahub Process: Toggle the columns in process

    Open DatahubApp
    Login to datahub
    Click Process
    Toggle table column                            column_name           Process Name
    Verify column                                  column_name           Process Name         Exist      True
    Toggle table column                            column_name           Process Name
    Verify column                                  column_name           Process Name         Exist      False
    Close process tab
    [Teardown]  Close DatahubApp

Datahub Process:

    Open DatahubApp
    Login to datahub
    Click Process
    Input text into filter                         column_name            # value
    Click Process name                             #First_row
    Verify process property                        input_fileds           # values
    Close Process tab
    [Teardown]  Close DatahubApp


*** Keywords ***
Login to datahub
    data_hub.LoginPage.Go to datahub
    Type in credential
    Click submit credential
