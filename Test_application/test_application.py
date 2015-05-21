from robotpageobjects import Page
import time
#pybot -vbrowser:firefox -vbaseurl:file:///C:/Users/Rama/Desktop/TestApplication_1/TestApplication test_application.robot
"""
This module extends Page
1. LoginPage
2. DatahubPage
3. FormTabSection
4. BrowserTabSection
"""

class LoginPage(Page):
    
    name = "testapplication"
    uri="/"
    
    """All the elements in a page targeted are listed in selectors"""
    
    selectors = {
        "go to testapplication": "/index.html",
        "login_user":"name=user",
        "login_password":"name=password",
        "login_button":"css=.x-btn.loginButton",
        "cancel_button":"css=.x-btn.cancelButton",
        "login_button_nv":"xpath=/html/body/div[3]/div[2]/div/div[2]/div/div/a[2]",       
        "wrongcredential popup ok":"xpath=/html/body/div[5]/div[3]/div/div/a[1]/span/span/span[2]",
    }
   #"login_button":"xpath=/html/body/div[3]/div[2]/div/div[2]/div/div/a[2]",
    def go_to_testapplicaiton(self):
        locator = self.resolve_selector("go to testapplication", n=1)
        self.go_to(locator)
        return self
    
    def login_button_not_visible(self):
        self.element_should_not_be_visible("login_button_nv")
        return self
            
        
    def maximize_page(self):
        self.maximize_browser_window()
        return self
          
    def credential_for_application(self, username="", password=""):
        self.input_text('login_user', username)
        self.input_text('login_password',password)
        self.click_element('login_button')
        #self._element_find('xpath=/html/body/div[3]/div[2]/div/div[2]/div/div/a[2]/span/span/span[2]', False, False)[0].click()    
        #self.submit_form('login_button')          #the right way to do
        return DatahubPage() 
    
    def click_popup_to_try_again(self):
        self.click_element("wrongcredential popup ok")
        return self 

    
    def click_cancel_button(self):
        self.click_element("cancel_button")
        return self    
            
    def verify_login_form_is_empty(self):
        login_text=self.get_text("login_user")
        self.log(login_text)
        #login_pasword=self.get_text("login_password")
        #if len(login_text) & len(login_password)==0
        if len(login_text) ==0:
            return self
        else:
            raise AssertionError("Cancel Button not functioning")     
    
    def  close_the_browser(self):
        self.close_browser()
        return self
        

class DatahubPage(Page):    
    selectors = {
        "Select form tab": "xpath=/html/body/div[2]/div/div/div/div[1]/div[3]/div/table/tbody/tr[2]/td/div/span",
        "Select browser info tab":"xpath=/html/body/div[2]/div/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div",
        "Panel one":"xpath=/html/body/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[2]/img",
        "Panel two":"xpath=/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[2]/img",
    }
    
    def  switch_to_panel_one(self):
        self.click_element("Panel one")
        return self
    
    def switch_to_panel_two(self):
        self.click_element("Panel two")
        return self    
    
    def select_form_tab(self):
        self.wait_until_page_contains_element("Select form tab")
        self.click_element("Select form tab")
        return FormtabSection()        

    def select_browser_tab(self):
        #time.sleep(5)
        self.click_element("Select browser info tab") 
        return BrowsertabSection()
        
        
class BrowsertabSection(Page):
    selectors = {
    "Browser render":"name=rendering_engine",
    "Browser type":"name=browser",
    "Browser platform":"name=platform",
    "Browser engine":"name=engine_version",
    "Browser css":"name=css_grade",
    "Browser info table":"xpath=/html/body/div[1]/div[2]/div[1]/div[2]/div/table",
    "Hiddenmenu elements":"css=.x-menu-item-text",
    "Reset Filters":"xpath=/html/body/div[1]/div[2]/div/div[3]/div/div/a/span/span",
    }

    def  input_rendering_engine(self,rendering_engine):
        self.input_text("Browser render", rendering_engine)
        return self
        
    def input_browser_type(self, browser_type):
        self.input_text("Browser type",browser_type)
        return self
    
    def input_browser_platform(self, browser_platform):
        self.input_text("Browser platform", browser_platform)
        return self
    
    def input_browser_engine(self, browser_engine):
        self.input_text("Browser engine", browser_engine)
        return self
        
    def input_browser_css_support(self, browser_css_support):
        self.input_text("Browser css", browser_css_support)
        return self
        
    def verify_filter_work_properly(self, row=1, column=1,verify_text='Gecko'):        
        # need to find out why this fails
        #self.table_cell_should_contain("Browser info table",1,1,u'Gecko')
        time.sleep(5)
        self.table_should_contain('css=.x-grid-cell-inner',verify_text)        
        return self
      
    def verify_page_must_not_have(self,text):
        time.sleep(5)
        self.page_should_not_contain(text)
        return self
        
    def enable_dropdown_for_browserinfo_table(self,column_name="Rendering engine"):
        #if 'Formtab ''is open the offset changes
        column_dictionary={"Rendering engine":"0","Browser":"8", "Platform(s)":"9","Engine version":"10","CSS grade":"11",}        
        #works:self.execute_javascript("window.document.getElementsByClassName('x-column-header-trigger')[7].click()")
        script_to_execute="window.document.getElementsByClassName('x-column-header-trigger')[{0}].click()".format(int(column_dictionary[column_name]))
        self.execute_javascript(script_to_execute)
        return self
    
    def toggle_column_in_browserinfo_table(self, column_name):
        column_dictionary={"Rendering engine":"3","Browser":"4", "Platform(s)":"5","Engine version":"6","CSS grade":"7",}
        #script_to_execute="window.document.getElementsByClassName('x-menu-item-link')[{0}].click()".format(int(column_dictionary[column_name]))
        #self.execute_javascript(script_to_execute)
        script_return_webelements="webelements=window.document.getElementsByClassName('x-menu-item-text'); return webelements;"
        elements=self.execute_javascript(script_return_webelements)
        #makes all elements visible to selenium now
        self.log(elements) 
        elements[2].click()
        time.sleep(10)       
        script_to_execute="window.document.getElementsByClassName('x-menu-item-text')[{0}].click()".format(int(column_dictionary[column_name]))
        #self.log("script to execute")
        self.execute_javascript(script_to_execute)            
        return self
        
    def reset_the_filters(self):
        self.click_element("Reset Filters")
        return self    
             

class FormtabSection(Page):
    save_button_id=None
    selectors = {
    "Fill title":"name=title",
    "Fill firstname":"name=firstname",
    "Fill lastname":"name=lastname",
    "Fill age":"name=age",
    "Fill manufacturer":"name=manufacturer",
    "Select checkbox greater than onefivezero":"xpath=/html/body/div[1]/div[2]/div[2]/div[2]/span/div/table[6]/tbody/tr/td[2]/input",
    "Fill textarea":"name=comments",
    "Save the form":"css=.x-btn.saveCustomerInfo.x-unselectable",
    "Reset the form":"css=.x-btn.resetCustomerInfo.x-unselectable",
    "Load first saved row":"xpath=/html/body/div[1]/div[2]/div[2]/div[2]/span/div/div/div[4]/div/table/tbody/tr[1]/td[1]/div",
    "Load into form":"css=.x-btn.loadCustomerInfo.x-unselectable",    
    "Data in table":"xpath=/html/body/div[1]/div[2]/div/div[2]/span/div/div/div[4]/div/table",
    "click nth row":"xpath=/html/body/div[1]/div[2]/div/div[2]/span/div/div/div[4]/div/table/tbody/tr[{n}]/td[1]/div"
    }

    def input_mandatory_userfields(self,title,firstname, lastname, age):
        self.input_text("Fill title",title)
        self.input_text("Fill firstname",firstname)
        self.input_text("Fill lastname",lastname)
        self.input_text("Fill age",age)
        return self

    def verify_form_is_reset(self, form_reset=True):
        # not all fields are verified
        # This function can do a lot more 
        title=self.get_text("Fill title")
        self.log(title)
        firstname=self.get_text("Fill firstname")
        self.log(firstname)
        lastname=self.get_text("Fill lastname")
        age=self.get_text("Fill age")
        if form_reset==True:
            if len(title) & len(firstname) & len(lastname) & len(age) == 0:
                return self
            else:
                raise AssertionError("Reset button not functioning")  
    
    def _concatenate_string(self, get_id):
        return 'id='+get_id
                 
    def save_data(self):
        time.sleep(5)       
        get_save_id=self.execute_javascript("save_buttonid=window.document.getElementsByClassName('x-btn-inner-center')[1].getAttribute('id'); return save_buttonid")        
        save_button_id=self._concatenate_string(get_save_id)
        self.click_element(save_button_id)
        return self
    
    def reset_form(self):      
        self.click_element("Reset the form")
        return self
    
    def load_form(self):
        self.click_element("Load into form")            
        return self
    
    def formtable_enable_dropdown(self, column_name="Title"):
        #method repeated as in class browserinfo
        column_dictionary={"Title":"0","Firstname":"1", "Lastname":"2","Age":"3","Manufacturer":"4","HP>150":"5","Comments":"6"}
        script_to_execute="window.document.getElementsByClassName('x-column-header-trigger')[{0}].click()".format(int(column_dictionary[column_name]))
        self.execute_javascript(script_to_execute)
        return self
    
    def toggle_column_in_formtable(self, column_name):
        # method repeated as in class browserinfo
        #Need documentation here
        #One of the last ways to access hidden elements
        #Could not find any alternatives
        column_dictionary={"Title":"3","Firstname":"4", "Lastname":"5","Age":"6","Manufacturer":"7","HP>150":"8","Comments":"9"}
        script_return_webelements="webelements=window.document.getElementsByClassName('x-menu-item-text'); return webelements;"
        elements=self.execute_javascript(script_return_webelements)
        #makes all elements visible to selenium now
        self.log(elements) 
        elements[2].click()
        time.sleep(10)       
        script_to_execute="window.document.getElementsByClassName('x-menu-item-text')[{0}].click()".format(int(column_dictionary[column_name]))
        #self.log("script to execute")
        self.execute_javascript(script_to_execute)     
        return self
    
    def sort_column_in_formtable(self, order="A-Z"):
        if order=="A-Z":
            script_to_execute="window.document.getElementsByClassName('x-menu-item-link')[0].click()"
            self.execute_javascript(script_to_execute)
            return self
        if order=="Z-A":
            script_to_execute="window.document.getElementsByClassName('x-menu-item-link')[1].click()"
            self.execute_javascript(script_to_execute)
            return self               
        
    def input_optional_userfields(self,manufacturer=None,select_checkbox=False, provide_comment=None):
        self.input_text("Fill manufacturer",manufacturer)
        if select_checkbox==True:
            self.click_element("Select checkbox greater than onefivezero")
        self.input_text("Fill textarea",provide_comment)
        return self
    
    def click_row(self, i):
        locator = self.resolve_selector("click nth row", n=int(i))
        self.click_element(locator)
        return self     
    
    def verify_data_saved_in_column(self, column, value):
        text_in_table=self.get_text("Data in table")
        assert  value in text_in_table
        return self
    
    def verify_sorting(self,order, column_name, text1, text2):
        if order=='A-Z':
            text_in_table=self.get_text("Data in table")
            text_as_list=text_in_table.split("\n")
            if text_as_list.index(str(text1))<text_as_list.index(str(text2)):
                return self
            else:
                raise AssertionError("A-Z sorting not functional")    
        if order=='Z-A':
            text_in_table=self.get_text("Data in table")
            text_as_list=text_in_table.split("\n")
            if text_as_list.index(str(text1))>text_as_list.index(str(text2)):
                return self
            else:
                raise AssertionError("Z-A sorting not functional")
         
    def verify_data_not_saved_in_table(self, comment):
        text_in_table=self.get_text("Data in table")
        assert  comment not in text_in_table
        return self