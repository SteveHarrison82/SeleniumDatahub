*** Settings ***
Documentation  testapplication sample tests
...
Library  test_application.LoginPage
Library  test_application.DatahubPage
Library  test_application.BrowsertabSection
Library  test_application.FormtabSection
Library  String

*** Test Cases ***
#Run testcases: pybot -vbrowser:chrome -vbaseurl:file:///C:/Users/Rama/Desktop/TestApplication test_application.robot

Test Data for the suite
    # This testcase needs to be placed as testsuite setup
    Create test data

#---------------------Login  Page-----------------------------#
#ToDo: Cancel button


A user tries to login without Username and Password
    Open testapplication   #This should be test case set up
    Go to testapplicaiton
    Maximize page
    Credential for application
    #ToDo: Login button inactive
    [Teardown]  Close the browser
   
A registered user logs in with correct password               
    #This testcase is an e.g Gearkin language "Given, When, Then"
    Given Open testapplication
    and Go to testapplicaiton
    When Maximize page
    Then Credential for application            test          test
    [Teardown]  Close the browser   

#data driven
A user tries to login with random user and random password
    Open testapplication   #This should be test case set up
    Go to testapplicaiton
    Maximize page
    Credential for application            ${user}          ${password}
    Click popup to try again
    Credential for application            test          ${password}
    Click popup to try again
    Credential for application            ${user}          test
    Click popup to try again
    Credential for application            test          test
    [Teardown]  Close the browser

#------------------Form Panel-----------------------#
#  Done: check mandatory 4 fields: number of test cases 4C1+4C2+4C3+4C4= 15 possible testcases (testscenario/sample testcase provided)
#  Done: Edit operations, Load button and check results on table
#  Done: Reset Button
#  To Do: Check field types: String (e.g name fields) or Integer and positive  (e.g age) or Combintion of both (e.g manufacturer)
#  Done: Issue: Hidden hidden elements

User logs in, selects form tab and registers with all fields
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test
    Select Form Tab
    Input Mandatory Userfields      Mr       ${firstname}          ${lastname}               23
    Input Optional Userfields         BMW     True        ${comment}
    Save Data
    Verify Data Saved in column       2        ${firstname}
    [Teardown]  Close the browser
    
User logs in and registers without optional field
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test
    Select Form Tab
    Input Mandatory Userfields      Mr       rama          kris               23
    Save Data
    Verify Data Saved in column       2        rama
    [Teardown]  Close the browser    

User logs in and registers without mandatory field 
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test
    Select Form Tab
    Input Optional Userfields         BMW     True         ${comment}
    Save Data
    Verify Data Not Saved in table        ${comment}
    [Teardown]  Close the browser 

#This testcase is a template and  can be repeated for any input field to verify
User clicks the first row of the table, edits and saves
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test    
    Select Form Tab
    Click row             1
    load form 
    Input Mandatory Userfields      Mr       ${firstname}         ${lastname}               34
    Input Optional Userfields         BMW     True         ${comment}
    Save Data
    Verify Data Saved in Column     1    ${firstname}
    Click row             1
    load form 
    Input Mandatory Userfields      Mr       ${firstname_edit}         ${lastname}               34
    Input Optional Userfields         BMW     True         ${comment}
    Save Data
    Verify Data Not Saved in table              ${firstname}      
    [Teardown]  Close the browser
            
User clicks the first row and reset the form 
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test    
    Select Form Tab
    Click row             1
    Reset Form
    Verify Form is Reset 
    [Teardown]  Close the browser
    
Check Togglecolumn is functional e.g Firstname
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test
    Select Form Tab
    Input Mandatory Userfields      @{Title}[0]       aFirst          aLast               23
    Input Optional Userfields         BMW     True        ${comment}
    Save Data
    Select Form Tab
    Input Mandatory Userfields      @{Title}[1]       zFirst          zLast               23
    Input Optional Userfields         BMW     True        ${comment}
    Save Data
    Formtable enable dropdown
    Toggle Column in Formtable           Firstname
    Verify Data Not Saved in table        aFirst
    Verify Data Not Saved in table        zFirst
    [Teardown]  Close the browser    
    
        
Check sorting is functional corresponding to Firstname
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test
    Select Form Tab
    Input Mandatory Userfields      @{Title}[0]       aFirst          aFirst               23
    Input Optional Userfields         BMW     True        ${comment}
    Save Data
    Select Form Tab
    Input Mandatory Userfields      @{Title}[1]       zFirst          zFirst               23
    Input Optional Userfields         BMW     True        ${comment}
    Save Data
    Formtable enable dropdown            Firstname
    Sort Column in Formtable                 A-Z 
    Verify sorting              A-Z             Firstname           aFirst            zFirst
    Formtable enable dropdown            Firstname
    Sort Column in Formtable                 Z-A
    Verify sorting              Z-A             Firstname           aFirst            zFirst
    [Teardown]  Close the browser

Check sorting is functional corresponding to Age
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test
    Select Form Tab
    Input Mandatory Userfields      @{Title}[0]       aFirst          aFirst               23
    Input Optional Userfields         BMW     True        ${comment}
    Save Data
    Select Form Tab
    Input Mandatory Userfields      @{Title}[1]       zFirst          zFirst               67
    Input Optional Userfields         BMW     True        ${comment}
    Save Data
    Formtable enable dropdown            Firstname
    Sort Column in Formtable                 A-Z 
    Verify sorting              A-Z             Age           23            67
    Formtable enable dropdown            Firstname
    Sort Column in Formtable                 Z-A
    Verify sorting              Z-A             Age           23            67
    [Teardown]  Close the browser

    
Toggle tab between form and browser info
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test
    Select Form Tab
    #ToDo: Verify Text             FormTab
    Select Browser Tab
    #ToDo: Verify BrowserTab Selected      
    Select Form Tab
    #ToDo: Verify FormTab Selected
    
     
#---------------------Browser Info Panel----------------------------------#
# Done:Check Five filters are working properly : 5 testcases (sample testcase)
# Done: Check Combinations of five filters are working properly Testcases : 5C2 + 5C3+5C4+5C5  (testscenario/sample testcase)
# Done: Issue: Hidden elements in this panel could not be found 
# ToDo: Handle sorting
# ToDo:Reset button
# Done: Handle toggle of columns

User logs in and selects browser info tab
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test
    Select browser tab  
    [Teardown]  Close the browser

User Selects browser info tab, filter and reset
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test
    Select browser tab
    Input browser type         Camino 1.5
    Input browser platform         Gnome
    Input rendering engine         Gecko
    Reset the filters
    #Verify
     [Teardown]  Close the browser

User Selects browser info tab and checks filter browser type
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test
    Select browser tab
    Input browser type         Camino 1.5
    Verify Filter Work Properly       1     1      Gecko
    Verify Page Must Not Have         Camino 1.0    
    [Teardown]  Close the browser

User Selects browser info tab and checks filter browser platform
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test
    Select browser tab
    Input browser platform         Gnome
    Verify Filter Work Properly       1     1      Gnome
    Verify Page Must Not Have         Win XP    
    [Teardown]  Close the browser
 
User Selects browser info tab and checks filter renderning engine
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test
    Select browser tab
    Input rendering engine         Gecko
    Verify Filter Work Properly       1     1      Gecko
    Verify Page Must Not Have         Trident    
    [Teardown]  Close the browser
    
User Selects browserinfo tab and checks filter CSS Grade and Browser
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test
    Select browser tab
    Input browser css support         A
    Input browser type                    Firefox
    Verify Filter Work Properly       1     1      A
    Verify Page Must Not Have        C/A
    Verify Page Must Not Have        Internet Explorer     
    [Teardown]  Close the browser
    
User Selects browserinfo tab and toggles a column
    Open testapplication
    Go to testapplicaiton
    Credential for application            test          test
    Select browser tab
    Builtin.Sleep     5
    Enable dropdown for Browserinfo Table
    Toggle column in browserinfo Table            Rendering engine
    # verify data not in table
    [Teardown]  Close the browser


*** Keywords *** 

Create test data
    ${user}=    Generate Random String    4   [LOWER][LETTERS]
    ${firstname}=      Generate Random String    4   [LOWER][LETTERS]
    ${firstname_edit}=      Generate Random String    4   [LOWER][LETTERS]
    ${lastname}=      Generate Random String    4   [LOWER][LETTERS]
    ${password}=    Generate Random String    5   [LOWER][LETTERS]
    ${comment}=     Generate Random String      8    [LOWER][LETTERS]
    @{Title} =            Create List                 Mr         Mrs
    Set Global Variable      ${firstname_edit}
    Set Global Variable      @{Title}
    Set Global Variable     ${user}
    Set Global Variable     ${firstname}
    Set Global Variable     ${lastname} 
    Set Global Variable     ${password}
    Set Global Variable     ${comment} 
    
