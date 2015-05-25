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

Datahub: Click all process properties and check input fields exist(standard report->process)

    Open DatahubApp
    Login to datahub
    Click link in standard report                          menu_name=Process
    Input Text into Process Tab filter                     Process Name      LOAD%
    Click Button in Process Tab                            Retrieve
    Click all process and close
    Close active tab
    [Teardown]  Close DatahubApp
    
Datahub: Click all process properties and check input fields exist(standard report->process)

    Open DatahubApp
    Login to datahub
    Click link in standard report                          menu_name=Process
    Input Text into Process Tab filter                     Process Name      SAP%
    Click Button in Process Tab                            Retrieve
    Click all process and close
    Close active tab
    [Teardown]  Close DatahubApp    

Datahub: Toggle column in Process tab(standard report->process)

    Open DatahubApp
    Login to datahub
    Click link in standard report                           menu_name=Process
    Toggle table column in Process Tab                      Process Name      Process Desc
    Close active tab
    [Teardown]  Close DatahubApp


Datahub: Verify filter Process Desc in Process(standard report->process)

    Open DatahubApp
    Login to datahub
    Click link in standard report                          menu_name=Process
    Input Text into Process Tab filter                     Process Desc      abc
    Click Button in Process Tab                            Retrieve
    Verify filter in Process Tab                           MONITOR           False
    Input Text into Process Tab filter                     Process Desc      abc    clear=True
    Click Button in Process Tab                            Retrieve
    Verify filter in Process Tab                           MONITOR
    Close active tab
    [Teardown]  Close DatahubApp
    

Datahub: Verify filter Process Name in Process(standard report->process)

    Open DatahubApp
    Login to datahub
    Click link in standard report                          menu_name=Process
    Input Text into Process Tab filter                     Process Name      abc
    Click Button in Process Tab                            Retrieve
    Verify filter in Process Tab                           MONITOR           False
    Input Text into Process Tab filter                     Process Name      abc    clear=True
    Click Button in Process Tab                            Retrieve
    Verify filter in Process Tab                           MONITOR           
    Close active tab
    [Teardown]  Close DatahubApp


Datahub: Verify filter Message in Process Log(standard report->process log) 

    Open DatahubApp
    Login to datahub
    Click link in standard report                          menu_name=Process Log
    Input text into Process Log filter                     Message               abc
    Click Button in Process Log                            Retrieve
    Verify filter in Process Log                           MONITOR               False
    Input text into Process Log filter                     Message               abc     clear=True
    Click Button in Process Log                            Retrieve
    Verify filter in Process Log                           MONITOR               
    Close active tab
    [Teardown]  Close DatahubApp


Datahub: Verify filter Start Date in Process Last Run(standard report->process last run) 

    Open DatahubApp
    Login to datahub
    Click link in standard report                          menu_name=Process Last Run
    Input date into Process Last Run filter                Start Date            2014-04-04     2014-04-11
    Click Button in Process Last Run                       Retrieve
    Verify filter in Process Last Run                      MONITOR               False
    Input date into Process Last Run filter                Start Date            2014-04-04     2014-04-11        clear=True
    Click Button in Process Last Run                       Retrieve
    Verify filter in Process Last Run                      MONITOR               
    Close active tab
    [Teardown]  Close DatahubApp  

Datahub: Verify filter Creation Date in Process Run(standard report->process run) 

    Open DatahubApp
    Login to datahub
    Click link in standard report                          menu_name=Process Run
    Input date into Process Run filter                     Creation Date         2014-04-04     2014-04-11
    Click Button in Process Run                            Retrieve
    Verify filter in Process Run                           MONITOR               False
    Input date into Process Run filter                     Creation Date         2014-04-04     2014-04-11        clear=True
    Click Button in Process Run                            Retrieve
    Verify filter in Process Run                           MONITOR               
    Close active tab
    [Teardown]  Close DatahubApp
    
Datahub: Verify filter Process Run Ref in Process Run(standard report->process run)

    Open DatahubApp
    Login to datahub
    Click link in standard report                          menu_name=Process Run
    Input Text into Process Run filter                     Process Run Ref      abc
    Click Button in Process Run                            Retrieve
    Verify filter in Process Run                           MONITOR              False
    Input Text into Process Run filter                     Process Run Ref      abc    clear=True
    Click Button in Process Run                            Retrieve
    Verify filter in Process Run                           MONITOR               
    Close active tab
    [Teardown]  Close DatahubApp

Datahub: Verify filter Process Name in Process Run(standard report->process run)

    Open DatahubApp
    Login to datahub
    Click link in standard report                          menu_name=Process Run
    Input Text into Process Run filter                     Process Name         abc
    Click Button in Process Run                            Retrieve
    Verify filter in Process Run                           MONITOR              False
    Input Text into Process Run filter                     Process Name         abc    clear=True
    Click Button in Process Run                            Retrieve
    Verify filter in Process Run                           MONITOR
    Close active tab
    [Teardown]  Close DatahubApp    

    
Datahub: Toggle column in Process Not Processed(standard report->process not processed)

    Open DatahubApp
    Login to datahub
    Click link in standard report                           menu_name=Process Not Processed
    Toggle table column in Process Not Processed            End Date      Pre Process Name
    Close active tab
    [Teardown]  Close DatahubApp 

Datahub: Toggle column in Process Last Run(standard report->process Last Run)

    Open DatahubApp
    Login to datahub
    Click link in standard report                           menu_name=Process Last Run
    Toggle table column in Process Last Run                 Creation Date      Process Name
    Close active tab
    [Teardown]  Close DatahubApp




*** Keywords ***
Login to datahub
    data_hub.LoginPage.Go to datahub
    Type in credential
    Click submit credential
