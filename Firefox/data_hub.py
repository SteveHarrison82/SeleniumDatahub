__author__ = 'rramasubramanian'

from robotpageobjects import Page, robot_alias
from bs4 import BeautifulSoup
from robot.utils import asserts
from robot.api import logger
import time

# pybot -L DEBUG -vbrowser:Ie -vbaseurl:http://localhost:9996 datahub_testsuite_test.robot
# pybot -L DEBUG -vbrowser:Firefox -vbaseurl:http://hulk:9960 datahub_testsuite_test.robot


class ExtJSHelper(Page):

    custom_selectors = {
        "go to testapplication": "/e2dh",
        "ActiveTab": "centertabpanel tabbar tab[active=\'true\']"
    }

    def _append_headerEl(self, id):
        """ Appends string '-headerEl' to the id
        Args:
            id of html e.g 'ext-123'
        Returns:
            string '-triggerEl' appended 'ext-123-headerEl'
        """
        return id+'_header'

    def _append_triggerEl(self, id):
        """ Appends string '-triggerEl' to the id
        Args:
            id of html e.g 'ext-123'
        Returns:
            string '-triggerEl' appended 'ext-123-triggerEl'
        """
        return id+'-triggerEl'

    def _append_id(self, element_id):
        """ Appends string '-triggerEl' to the id
        Args:
            id of html e.g 'ext-123'
        Returns:
            string 'id=' appended 'id=ext-123'
        """
        element_id = 'id='+element_id
        return element_id

    def _append_xpath(self, element_xpath):
        """ Appends string '-triggerEl' to the id
        Args:
            xpath of html e.g '/my/xpath'
        Returns:
            string 'xpath=' appended 'xpath=/my/xpath'
        """

        element_xpath = 'xpath='+element_xpath
        return element_xpath

    def _get_inputfield_id(self, selector_section):
        """ Fetches dom of the selector section
        Args:
            selector_section is xtype or itemid
        Returns:
            view property of the interested component
        """

        my_query = """
                return Ext.ComponentQuery.query(\"{0}\").getEl().dom.querySelector('input').id;
             """.format(selector_section)
        inputfield_id = self.execute_javascript(my_query)
        return self._append_id(inputfield_id)

    def _get_all_inputfields(self, selector_section):
        """ Fetches dom of the selector section
        Args:
            selector_section is xtype or itemid
        Returns:
            view property of the interested component
        """

        my_query = """
                return Ext.ComponentQuery.query(\"{0}\").getEl().dom.querySelectorAll('input');
             """.format(selector_section)
        inputfields_dom = self.execute_javascript(my_query)
        return inputfields_dom

    def _get_component_dom(self, selector_section):
        """ Fetches dom of the selector section
        Args:
            selector_section is xtype or itemid
        Returns:
            view property of the interested component
        """
        my_query = """
                return Ext.ComponentQuery.query(\"{0}\").reduce(function(prev,component){var element =  component.getActionEl() ||  component.getEl(); if(element && element.dom){return prev.concat(element.dom);}},[]);
             """.format(selector_section)
        dom_html = self.execute_javascript(my_query)
        return dom_html[0]

    def _get_component_id(self, selector_section):
        """ Fetches id of the selector section
        Args:
            selector_section is xtype or itemid
        Returns:
            view property of the interested component
        """

        my_query = """
                return Ext.ComponentQuery.query(\"{0}\").reduce(function(prev,component){var element =  component.getActionEl() ||  component.getEl(); if(element && element.dom){return prev.concat(element.id);}},[]);
            """.format(selector_section)
        element_id = self.execute_javascript(my_query)
        return element_id[0]

    def _get_component_all_nodes(self, selector_section):
        """ Fetches all nodes of the component
        Args:
            selector_section is xtype or itemid
        Returns:
            view property of the interested component
        """

        my_query = 'return Ext.ComponentQuery.query(\"{0}\")[0].view.getNodes(1)[0];'.format(selector_section)
        web_element = self.execute_javascript(my_query)
        return web_element
        # e.g Ext.ComponentQuery.query('#' + treePanelItemId)[0]

    def _get_parent_component_node_id(self, selector_section, position=0):
        """ Fetches all nodes of the component
        Args:
            selector_section is xtype or itemid
        Returns:
            view property of the interested component
        """

        my_query = 'return Ext.ComponentQuery.query(\"{0}\")[0].view.getNodes(0)[{1}].id;'.format(selector_section, int(position))
        id_element = self.execute_javascript(my_query)
        return self._append_id(id_element)

    def _get_component_node_id(self, selector_section, position):
        """ Fetches all nodes of the component
        Args:
            selector_section is xtype or itemid
        Returns:
            view property of the interested component
        """

        my_query = 'return Ext.ComponentQuery.query(\"{0}\")[0].view.getNodes(1)[{1}].id;'.format(selector_section, int(position))
        id_element = self.execute_javascript(my_query)
        return self._append_id(id_element)
        # e.g Ext.ComponentQuery.query('#' + treePanelItemId)[0]

    def _get_gridid(self, selector_section, for_js=False, position=0):
        """ Fetches dynamic id of a xtype or itemid
        Args:
            selector_section is xtype or itemid
        Returns:
            dynamic id of html element
        """

        my_query = 'return Ext.ComponentQuery.query(\"{0}\")[{1}].el.id'.format(selector_section, int(position))
        element_id = self.execute_javascript(my_query)
        # When executing javascript, id need not be appended
        if for_js:
            return element_id
        return self._append_id(element_id)

    def _get_gridid_2(self, selector_section, for_js=False, position=0):
        """ <duplicates method _get_gridid> Returns dynamic id of a xtype or itemid
        Args:
            selector_section of html element : xtype or itemid
        Returns:
            dynamic id of html element
        """

        my_query = 'return Ext.ComponentQuery.query(\"{0}\")[{1}].id'.format(selector_section, int(position))
        element_id = self.execute_javascript(my_query)
        # When executing javascript, id need not be appended
        if for_js:
            return element_id
        return self._append_id(element_id)

    def _get_custom_selectors(self, select_selector, position):
        element_id = self._get_component_node_id(select_selector, position)
        return self._append_id(element_id)

    def _click_element_js(self, selector_section):
        """ Click an element in the html page by executing javascript
        Use the method seldom on running out of option
        Args:
            selector_section is 'id'
        Returns:
            None
        """

        my_query = 'document.getElementById("{0}").click()'.format(selector_section)
        logger.debug('javascript to trigger dropdown {0}'.format(my_query))
        self.execute_javascript(my_query)
        return self

    def _get_elements_js(self, selector_selection):
        my_query = 'return document.getElementsByClassName("{0}")'.format(selector_selection)
        elements = self.execute_javascript(my_query)
        return elements

    def _get_len_of_elements(self, element_array):
        return len(element_array)

    def _get_textcontent_js(self, selector_selection, position = 0):
        my_query = 'return document.getElementsByClassName("{0}")[{1}].textContent'.format(selector_selection, position)
        text_content = self.execute_javascript(my_query)
        return text_content

    def _construct_query(self, xtype, filter_value, filter_type='text'):
        """ Constructs a string to be used for quering using Ext.ComponentQuery.query API.
        This method is needed esp. when query parameter needs a filter.
        E.g Consider query "processPanel headercontainer [text=Process Name]".
        The filter in this case is '[text=Process Name]'

        Args:
            selector_section is xtype
        Returns:
            None
        """

        return xtype+'['+filter_type+'='+filter_value+']'

    def _get_webelements(self, selector_selection):
        # wont work
        time.sleep(5)
        my_query = 'return Ext.ComponentQuery.query("{0}")'.format(selector_selection)
        web_elements = self.execute_javascript(my_query)
        return list(web_elements)

    def _get_webelement(self, selector_selection, position=0):
        time.sleep(5)
        my_query = 'return Ext.ComponentQuery.query("{0}")[{1}].el.id'.format(selector_selection, int(position))
        web_element_id = self.execute_javascript(my_query)
        web_element = self.find_element(self._append_id(web_element_id))
        return web_element

    def _get_id_from_webelement(self, web_element):
        logger.debug('id is' + str(web_element.id))
        return web_element.id

    def _is_webelement_displayed(self, web_element):
        return web_element.is_displayed()

    def _is_webelement_enabled(self, web_element):
        return web_element.is_enabled()

    def _get_text_from_webelement(self, web_element):
        return web_element.text

    def _get_attribute_from_webelement(self, web_element, check_attribute):
        return web_element.get_attribute(check_attribute)

    def _click_webelement(self, web_element):
        web_element.click()

    def _send_keys_from_webelement(self, web_element, my_keys):
        web_element.send_keys(my_keys)

    def _submit_webelement(self, web_element):
        web_element.submit()

    def _get_tagname_from_webelement(self, web_element):
        return web_element.tag_name()

    def _get_form_inputEl(self, selector_selection):
        """ Returns the input text field id
        Args:
            Selector_selection: xtype or itemid
        Returns:
            id of the input field
        """

        time.sleep(5)
        #self.wait_until_element_is_visible("xpath=//div[3]/div/div[2]/table/tbody/tr")
        #self.wait_for_condition('return Ext.ComponentQuery.query("{0}")[0]'.format(selector_selection))
        my_query = 'return Ext.ComponentQuery.query("{0}")[0].inputEl.id'.format(selector_selection)
        input_id = self.execute_javascript(my_query)
        return self._append_id(input_id)

    def _get_innerhtml(self, selector_selection):
        """ Returns the innnerHTML of a dom
        Args:
            selector_selection is xtype or itemid

        Returns:
            html content corresponding to xtype or itemid
        """

        time.sleep(5)
        #self.wait_until_element_is_visible("xpath=//div[3]/div/div[2]/table/tbody/tr")
        #self.wait_for_condition('return Ext.ComponentQuery.query("{0}")[0]'.format(selector_selection))
        my_query = 'return Ext.ComponentQuery.query("{0}")[0].el.dom.innerHTML'.format(selector_selection)
        dom_html = self.execute_javascript(my_query)
        return dom_html

    def _number_of_gridrows(self, selector_selection):
        """ Returns number of rows in a gridview
        Args:
            selector e.g css or xpath; of the div correponding to gridview
        Returns:
             Number of gridrows
        """

        dom_html = self._get_innerhtml(selector_selection)
        soup = BeautifulSoup(dom_html)
        table_list = soup.findAll('table')
        number_of_rows = len(table_list)
        logger.debug("soup {0}".format(number_of_rows))
        return number_of_rows

    def _construct_xpath_of_rows(self, xpath_of_grid, number_of_rows):
        """ Constructs xpath of each row
        Args:
            a. xpath template
            b. number of rows
        Returns:
            c. Actual xpaths corresponding to each row
        """

        my_xpath_gen_0 = xpath_of_grid.replace('[{0}]', '')
        my_xpath_gen = [xpath_of_grid.format(each_value) for each_value in xrange(1, number_of_rows)]
        my_xpath_gen.insert(0, my_xpath_gen_0)
        logger.debug("xpath_generator is {0}".format(my_xpath_gen))
        return my_xpath_gen

    def _get_text_from_activetab(self, my_xpath):
        """ Fetches the complete text from active tab
        Returns:
            Returns the complete text of a active tab
        """

        my_xpath = self._append_xpath(my_xpath)
        logger.debug("my_xpath_is: {0}".format(my_xpath))
        my_text = self.get_text(my_xpath)
        logger.debug("Text from active tab: {0}".format(my_text))
        return my_text

    def _get_inputid_from_itemtype(self, selector):
        """ Fetches the inputid when selector is  itemid
        Returns:
            Returns the input id of a text field in the format 'id=<input_id>'
        """

        time.sleep(5)
        my_query = 'return Ext.ComponentQuery.query(\"#{0}\")[0].inputId'.format(selector)
        input_id = self.execute_javascript(my_query)
        return self._append_id(input_id)     # id=someid-1234

    def _get_inputid_from_xtype(self, selector):
        """ Fetches the inputid of textfield when selector is xtype or itemid
        Returns:
            Returns the input id of a text field in the format 'id=<input_id>'
        """

        time.sleep(5)
        my_query = 'return Ext.ComponentQuery.query(\"{0}\")[0].inputId'.format(selector)
        input_id = self.execute_javascript(my_query)
        return self._append_id(input_id)

    def _get_id_from_xtype(self, selector):
        time.sleep(5)
        my_query = 'return Ext.ComponentQuery.query(\"{0}\")[0].id'.format(selector)
        id = self.execute_javascript(my_query)
        return self._append_id(id)

    def _get_active_tab(self, active_tab_xtype = None):
        """ Returns id of tab thats currently active(open)
        Returns:
            active_tab_id: Returns the id of the active tab in the format 'id=<active_tab_id>'
        """
        if active_tab_xtype == None:
            active_tab_xtype = self.custom_selectors['ActiveTab']
        active_tab_id = self._get_gridid(active_tab_xtype)
        # centertabpanel tabbar tab[active="true"]
        logger.debug("active tab id is {0}".format(active_tab_id))
        return self._append_id(active_tab_id)

    def close_tab(self, active_tab_id):
        """ Closes the active tab.
        Args:
           active_tab_xtype: xtype of (active tab in centertabpanel)
        """

        self.click_element(active_tab_id)
        return self


class LoginPage(ExtJSHelper):
    name = "DatahubApp"
    uri = "/"

    selectors = {
        "go to datahub": "/e2dh",
        "username": "name=username",
        "submit button": "xpath=/html/body/div/form/input[2]",
    }

    custom_selectors = {
        "Browser": "Firefox",
    }

    def go_to_datahub(self):
        locator = self.resolve_selector("go to datahub", n=1)
        # self.create_webdriver(self.custom_selectors["Browser"])
        self.go_to(locator)
        self.maximize_browser_window()
        return self

    def type_in_credential(self):
        self.input_text("username", "admin")
        return self

    def click_submit_credential(self):
        self.click_element("submit button")
        return DatahubMenu()


class Datahub(ExtJSHelper):
    uri = "/e2dh"

    selectors = {
        "DatahubMenu": "css=.dataHubTreePanel"
    }

    custom_selectors = {
        "DatahubMenu": "#datahubTreePanel",
        "SystemMenu": "#systemTreePanel",
        "LogsMenu": "#dhLogsTreePanel",
        "DatasourceMenu": "",
    }

    id_custom_selectors = {
        "id_datahub_menu": "",
        "id_system_menu": "",
        "id_logs_menu": "",
        "id_datasource_menu": "",
    }

    def toggle_datahub_menu(self):
        if not self.id_custom_selectors["id_datahub_menu"]:
            id_element = self._get_gridid_2(self.custom_selectors["DatahubMenu"])
            logger.debug("datahub menu element id is {0}".format(id_element))
            self.id_custom_selectors["id_datahub_menu"] = id_element
        id_datahub_menu = self._append_headerEl(self.id_custom_selectors["id_datahub_menu"])
        self.click_element(id_datahub_menu)
        return DatahubMenu()

    def toggle_system_menu(self):
        if not self.id_custom_selectors["id_system_menu"]:
            id_element = self._get_gridid_2(self.custom_selectors["SystemMenu"])
            logger.debug("system menu element id is {0}".format(id_element))
            self.id_custom_selectors["id_system_menu"] = id_element
        id_system_menu = self._append_headerEl(self.id_custom_selectors["id_system_menu"])
        self.click_element(id_system_menu)
        return SystemMenu()

    def toggle_logs_menu(self):
        if not self.id_custom_selectors["id_logs_menu"]:
            id_element = self._get_gridid_2(self.custom_selectors["LogsMenu"])
            logger.debug("logs menu element id is {0}".format(id_element))
            self.id_custom_selectors["id_logs_menu"] = id_element
        id_logs_menu = self._append_headerEl(self.id_custom_selectors["id_logs_menu"])
        self.click_element(id_logs_menu)
        return LogsMenu()

    def toggle_datasource_menu(self):
        if not self.id_custom_selectors["id_datasource_menu"]:
            id_element = self._get_gridid_2(self.custom_selectors["DatassourceMenu"])
            logger.debug("datasource menu element id is {0}".format(id_element))
            self.id_custom_selectors["id_datasource_menu"] = id_element
        id_datasource_menu = self._append_headerEl(self.id_custom_selectors["id_datasource_menu"])
        self.click_element(id_datasource_menu)
        return DatasourceMenu()


class SystemMenu(ExtJSHelper):

    custom_selectors = {
        "SystemMenu": "#systemTreePanel",
        "Users": "",
        "Connections": "",
        "UserSetup": ""
    }

    id_custom_selectors = {
        "id_users": "",
        "id_connections": "",
        "id_current_threads": "",
        "id_usersetup": "",
        "id_partners": "",
        "id_endpoints": "",
        "id_messages": "",
        "id_routes": ""
    }

    def _get_id_for_systemcomponents(self):

        if not self.id_custom_selectors["id_users"]:
            logger.debug("executing method: {0}".format("_get_parent_component_node_id"))
            id_element = self._get_parent_component_node_id(self.custom_selectors["SystemMenu"])
            logger.debug("Users element id is {0}".format(id_element))
            self.id_custom_selectors["id_users"] = id_element
            self.id_custom_selectors["id_connections"] = id_element.replace('record-11', 'record-12')
            logger.debug("Connections element id is {0}".format(self.id_custom_selectors["id_connections"]))
            self.id_custom_selectors["id_usersetup"] = id_element.replace('record-11', 'record-14')
            logger.debug("Usersetup element id is {0}".format(self.id_custom_selectors["id_usersetup"]))
            self.id_custom_selectors["id_partners"] = id_element.replace('record-11', 'record-15')
            logger.debug("Partners element id is {0}".format(self.id_custom_selectors["id_partners"]))
            self.id_custom_selectors["id_endpoints"] = id_element.replace('record-11', 'record-16')
            logger.debug("Endpoints element id is {0}".format(self.id_custom_selectors["id_endpoints"]))
            self.id_custom_selectors["id_messages"] = id_element.replace('record-11', 'record-17')
            logger.debug("Messages element id is {0}".format(self.id_custom_selectors["id_messages"]))
            self.id_custom_selectors["id_routes"] = id_element.replace('record-11', 'record-18')
            logger.debug("Routes element id is {0}".format(self.id_custom_selectors["id_routes"]))
        return self

    def click_users(self):
        self._get_id_for_systemcomponents()
        self.double_click_element(self.id_custom_selectors["id_users"])
        return self

    def click_usersetup(self):
        self._get_id_for_systemcomponents()
        self.click_element(self.id_custom_selectors["id_usersetup"])
        return UserSetup()

    def click_connections(self):
        self._get_id_for_systemcomponents()
        self.double_click_element(self.id_custom_selectors["id_connections"])
        return self

    def click_partners(self):
        self._get_id_for_systemcomponents()
        self.double_click_element(self.id_custom_selectors["id_partners"])
        return Partners()

    def click_endpoints(self):
        self._get_id_for_systemcomponents()
        self.click_element(self.id_custom_selectors["id_endpoints"])
        return Endpoints()

    def click_message(self):
        self._get_id_for_systemcomponents()
        self.click_element(self.id_custom_selectors["id_messages"])
        return Messages()

    def click_routes(self):
        self._get_id_for_systemcomponents()
        self.click_element(self.id_custom_selectors["id_routes"])
        return Routes()


class Partners(ExtJSHelper):

    custom_selectors = {
        "Text Body": "/html/body/div[3]/div[2]",
    }

    def verify_text_in_partners(self, search_text='Service Address'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "partners doesnot contain {0}".format(search_text))
        return self


class Endpoints(ExtJSHelper):

    custom_selectors = {
        "Text Body": "/html/body/div[3]/div[2]",
    }

    def verify_text_in_endpoints(self, search_text='Partner Id'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "Endpoints doesnot contain {0}".format(search_text))
        return self


class Messages(ExtJSHelper):

    custom_selectors = {
        "Text Body": "/html/body/div[3]/div[2]",
    }

    def verify_text_in_messages(self, search_text='Message Type'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "Message doesnot contain {0}".format(search_text))
        return self


class Routes(ExtJSHelper):

    custom_selectors = {
        "Text Body": "/html/body/div[3]/div[2]",
    }

    def verify_text_in_routes(self, search_text='From End Point'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "Routes doesnot contain {0}".format(search_text))
        return self


class UserSetup(ExtJSHelper):

    custom_selectors = {
        "UserSetup": "",
        "Text Body": "/html/body/div[3]/div[2]",
    }

    def verify_text_in_usersetup(self, search_text='User Name'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "processrun doesnot contain {0}".format(search_text))
        return self


class LogsMenu(ExtJSHelper):

    custom_selectors = {
        "LogsMenu": "#dhLogsTreePanel",
    }

    id_custom_selectors = {
        "id_application_log": "",
        "id_sql_log": "",
        "id_access_log": "",
    }

    def click_application_log(self):
        if not self.id_custom_selectors["id_application_log"]:
            id_element = self._get_component_node_id(self.custom_selectors["LogsMenu"], "0")
            logger.debug("application log element id is {0}".format(id_element))
            self.id_custom_selectors["id_application_log"] = id_element
        self.click_element(self.id_custom_selectors["id_application_log"])
        return ApplicationLog()

    def click_sql_log(self):
        if not self.id_custom_selectors["id_sql_log"]:
            id_element = self._get_component_node_id(self.custom_selectors["LogsMenu"], "1")
            logger.debug("sql log element id is {0}".format(id_element))
            self.id_custom_selectors["id_sql_log"] = id_element
        self.click_element(self.id_custom_selectors["id_sql_log"])
        return SQLLog()

    def click_access_log(self):
        if not self.id_custom_selectors["id_access_log"]:
            id_element = self._get_component_node_id(self.custom_selectors["LogsMenu"], "2")
            logger.debug("access log element id is {0}".format(id_element))
            self.id_custom_selectors["id_access_log"] = id_element
        self.click_element(self.id_custom_selectors["id_access_log"])
        return AccessLog()


class ApplicationLog(ExtJSHelper):

    custom_selectors = {
        "Text Body": "/html/body/div[3]/div[2]",
    }

    def verify_text_in_applicationlog(self, search_text='Logger'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "Applicationlog doesnot contain {0}".format(search_text))
        return self


class SQLLog(ExtJSHelper):

    custom_selectors = {
        "Text Body": "/html/body/div[3]/div[2]",
    }

    def verify_text_in_sqllog(self, search_text='Execution Time (ms)'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "SQLlog doesnot contain {0}".format(search_text))
        return self


class AccessLog(ExtJSHelper):

    custom_selectors = {
        "Text Body": "/html/body/div[3]/div[2]",
    }

    def verify_text_in_accesslog(self, search_text='Path'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "Accesslog doesnot contain {0}".format(search_text))
        return self


class DatasourceMenu():
    pass


class DatahubMenu(ExtJSHelper):
    uri = "/e2dh"

    selectors = {
        "Process": "css=.processes",
    }

    custom_selectors = {
        "DatahubMenu": "#dataHubTreePanel",
    }

    id_custom_selectors = {
        "id_proc_run": "",
        "id_proc_lastrun": "",
        "id_proc_log": "",
        "id_proc_notprocessed": "",
        "id_proc_rundependencies": "",
        "id_proc_dependencies": "",
    }

    def click_link_in_datahub_menu(self, menu_name='Process'):
        if menu_name == 'Process Run':
            self.click_process_run()
        elif menu_name == 'Process Dependenices':
            self.click_process_dependencies()
        elif menu_name == 'Process Run Dependencies':
            self.click_process_run_dependencies()
        elif menu_name == 'Process Last Run':
            self.click_process_last_run()
        elif menu_name == 'Process Log':
            self.click_process_log()
        elif menu_name == 'Process Not Processed':
            self.click_process_not_processed()
        else:
            self.click_process()

    def click_process(self):
        time.sleep(5)
        self.click_element("Process")
        return ProcessTab()

    def click_process_run(self):
        if not self.id_custom_selectors["id_proc_run"]:
            id_element = self._get_component_node_id(self.custom_selectors["DatahubMenu"], "1")
            logger.debug("process run element id is {0}".format(id_element))
            self.id_custom_selectors["id_proc_run"] = id_element
        self.click_element(self.id_custom_selectors["id_proc_run"])
        return ProcessRun()

    def click_process_last_run(self):
        if not self.id_custom_selectors["id_proc_lastrun"]:
            id_element = self._get_component_node_id(self.custom_selectors["DatahubMenu"], "2")
            logger.debug("process last run element id is {0}".format(id_element))
            self.id_custom_selectors["id_proc_lastrun"] = id_element
        self.click_element(self.id_custom_selectors["id_proc_lastrun"])
        return ProcessLastRun()

    def click_process_log(self):
        if not self.id_custom_selectors["id_proc_log"]:
            id_element = self._get_component_node_id(self.custom_selectors["DatahubMenu"], "3")
            logger.debug("process log element id is {0}".format(id_element))
            self.id_custom_selectors["id_proc_log"] = id_element
        self.click_element(self.id_custom_selectors["id_proc_log"])
        return ProcessLog()

    def click_process_not_processed(self):
        if not self.id_custom_selectors["id_proc_notprocessed"]:
            id_element = self._get_component_node_id(self.custom_selectors["DatahubMenu"], "4")
            logger.debug("process not processed element id is {0}".format(id_element))
            self.id_custom_selectors["id_proc_notprocessed"] = id_element
        self.click_element(self.id_custom_selectors["id_proc_notprocessed"])
        return ProcessNotProcessed()

    def click_process_run_dependencies(self):
        if not self.id_custom_selectors["id_proc_rundependencies"]:
            id_element = self._get_component_node_id(self.custom_selectors["DatahubMenu"], "5")
            logger.debug("Proc Run Dependencies element id is {0}".format(id_element))
            self.id_custom_selectors["id_proc_rundependencies"] = id_element
        self.click_element(self.id_custom_selectors["id_proc_rundependencies"])
        return ProcessRunDependency()

    def click_process_dependencies(self):
        if not self.id_custom_selectors["id_proc_dependencies"]:
            id_element = self._get_component_node_id(self.custom_selectors["DatahubMenu"], "6")
            logger.debug("Proc Dependencies element id is {0}".format(id_element))
            self.id_custom_selectors["id_proc_dependencies"] = id_element
        self.click_element(self.id_custom_selectors["id_proc_dependencies"])
        return ProcessDependencies()

    def navigate_to_other_menu(self):
        return Datahub()


class DatahubMenuCommonActions():

    custom_selectors = {
        "Text Body": "/html/body/div[3]/div[2]",
        "GridColumn": 'gridcolumn',
        "MenuItem": 'menu menuitem',
    }

    def _toggle_column(self, column_name):
        my_query = self._construct_query(self.custom_selectors["GridColumn"], column_name, 'text')
        id = self._get_gridid(my_query, for_js=True, position=1)
        id_triggerEl = self._append_triggerEl(id)
        logger.debug('trigger element id is {0}'.format(id_triggerEl))
        self._click_element_js(id_triggerEl)
        # looks as execute_javascript('return document.getElementById("gridcolumn-
        # 1200-triggerEl").click()')
        self.mouse_over("Menu items")
        my_query = self._construct_query(self.custom_selectors["MenuItem"], column_name, 'text')
        id_of_menucheckitem = self._get_gridid_2(my_query, for_js=False)
        logger.debug('menucheck item id is  {0}'.format(id_of_menucheckitem))
        # looks as Ext.ComponentQuery.query("menu menuitem [text = Process Name]")[0].id
        self.click_element(id_of_menucheckitem)
        return self

    def _input_text_into_filter(self, id, write_input_text):
        self.input_text(id, write_input_text)
        return self

    def _input_date_into_filter(self, from_date, to_date):
        pass

    def _verify_filter(self, column_name, text_input):
        web_elements = self._get_elements_js(column_name)
        element_len = self._get_len_of_elements(web_elements)
        for each_element in range(element_len):
            verify_text = self._get_textcontent_js(column_name, each_element)
            assert text_input in verify_text
        return self


    def _click_button(self, Button):
        #xtype_for_button = "processPanel reportTopBar button"
        logger.debug(Button)
        id_element = self._get_gridid(Button)
        logger.debug("+id webelement *Retreive button* ={0} ".format(id_element))
        self.click_element(id_element)
        return self


class ProcessTab(ExtJSHelper, DatahubMenuCommonActions):
    uri = "/e2dh"

    selectors = {
        "Process Name": "css = .processName input",
        "Process Desc Input": "css =.processDescription input",
        "Retreive data": "css = .retrieveReportData",
        "gridview": "processPanel gridview",
        "Table first row": "xpath=//div[3]/div/div[2]/table/tbody/tr",
        "process specific row": "//div[3]/div/div[2]/table[{0}]/tbody/tr/td[2]/div/span",
        "add retreive button": "processPanel reportTopBar button",
        "Menu items": "css=.x-menu-item-arrow",
        "CloseProcessProperty": "css= .x-tool-img.x-tool-close",
        "Click Process Name": "xpath=//span[contains(text(),\"{0}\")]"
    }

    custom_selectors = {
        "ProcessPanel": "processPanel",
        "ProcessPanel header":"processPanel header",
        "Text Body": "/html/body/div[3]/div[2]",
        "GridColumn": 'gridcolumn',
        "MenuItem": 'menu menuitem',
        "Button": "processPanel reportTopBar button",
        "Process Name": "x-grid-cell-processName",
        "Process Desc": "x-grid-cell-processDescription",
        "Process Properties Window": "ProcessPropertiesWindow",
        "Tab": "centertabpanel tabbar tab"
    }

    def toggle_table_column(self, column_name='Process Name'):
        ''' Trigger the dropdown, move the mouse over, toggle the column name
        '''
        self._toggle_column(column_name)

    def type_input_process_name(self, text_input = "CLEAN%"):
        self.input_text("Process Name", text_input)
        return self

    def type_input_process_description(self, text_input = "Clean%"):
        self.input_text("Process Desc Input", text_input)
        return self

    def click_retreive_data(self):
        self.click_element("Retreive data")
        return self

    def get_all_process(self):
        selectors = ProcessTab.selectors
        number_of_gridrows = self._number_of_gridrows(selectors["gridview"])
        logger.debug("Table has {0} rows".format(number_of_gridrows))
        if number_of_gridrows > 0:
            xpath_gen = self._construct_xpath_of_rows(selectors["process specific row"], number_of_gridrows)
            for each_xpath in xpath_gen:
                logger.debug(each_xpath)
                logger.debug(self._get_text_from_activetab(each_xpath))
            return self
        return self

    def click_add_button(self):
        xpath_for_button = "processPanel reportTopBar button"
        logger.debug(xpath_for_button)
        id_element = self._get_gridid(xpath_for_button, 1)
        logger.debug("+id webelement *Add button*={0}".format(id_element))
        self.click_element(id_element)
        return self

    def click_button(self, Button = "Retreive"):
        if Button == "Retrieve":
            self._click_button(self.custom_selectors["Button"])
        elif Button == "Add":
            pass

    def verify_text_in_process_tab(self, search_text='Process Name'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "processTab doesnot contain {0}".format(search_text))
        return self

    def input_text_into_filter(self, column_name, text_input):
        xtype_input = self._construct_query(self.custom_selectors["ProcessPanel header"], column_name)
        id = self._get_inputfield_id(xtype_input)
        self._input_text_into_filter(id, text_input)

    def close_process_property(self):
        self.click_element("CloseProcessProperty")
        return self

    def verify_filter(self, column_name, text_input):
        #column_name = column_name + ' Column'
        if not self.custom_selectors[column_name]:
            # get the gridcolumn id e.g gridcolumn-123 from extjs api
            # 'x-grid-cell-' append to the id e.g  x-grid-cell-gridcolumn-123
            # self.custom_selectors[column_name] = 'x-grid-cell-gridcolumn-123'
            pass
        self._verify_filter(self.custom_selectors[column_name], text_input)

    def click_all_process_and_close(self, close=True):
        web_elements = self._get_elements_js(self.custom_selectors["Process Name"])
        element_len = self._get_len_of_elements(web_elements)
        for each_element in range(element_len):
            get_text = self._get_textcontent_js(self.custom_selectors["Process Name"], each_element)
            self.selectors["Click Process Name"].format(get_text)
            self.click_element("Click Process Name")
            inputfields_dom = self._get_all_inputfields(self.custom_selectors["Process Properties Window"])
            assert len(inputfields_dom) > 0
            if close == True :
            #if one process on filtering and dont want to close, then give close=False
                self.close_process_property()

    def close_process_tab(self):
        selector_section = self._construct_query(self.custom_selectors["Tab"], "Process", "text")
        id_tab = self._get_component_id(selector_section)
        id_tab_triggerEl = self._append_triggerEl(id_tab)
        self.close_tab(id_tab_triggerEl)

class ProcessRun(ExtJSHelper):

    custom_selectors = {
        "Text Body": "/html/body/div[3]/div[2]",
    }

    def verify_text_in_processrun(self, search_text='Process Run Ref'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "processrun doesnot contain {0}".format(search_text))
        return self


class ProcessLastRun(ExtJSHelper):

    custom_selectors = {
        "Text Body": "/html/body/div[3]/div[2]",
    }

    def verify_text_in_processlastrun(self, search_text='Process Run Ref'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "processrun doesnot contain {0}".format(search_text))
        return self


class ProcessLog(ExtJSHelper):

    custom_selectors = {
        "Text Body": "/html/body/div[3]/div[2]",
    }

    def verify_text_in_processlog(self, search_text='Process Run Ref'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "processrun doesnot contain {0}".format(search_text))
        return self


class ProcessNotProcessed(ExtJSHelper):

    custom_selectors = {
        "Text Body": "/html/body/div[3]/div[2]",
    }

    def verify_text_in_process_not_processed(self, search_text='Proc Run Reference'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "processnotprocessed doesnot contain {0}".format(search_text))
        return self


class ProcessRunDependency(ExtJSHelper):

    custom_selectors = {
        "Text Body": "/html/body/div[3]/div[2]",
    }

    def verify_text_in_process_run_dependency(self, search_text='Pre-Process Run Ref'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "processnotprocessed doesnot contain {0}".format(search_text))
        return self


class ProcessDependencies(ExtJSHelper):

    custom_selectors = {
        "Text Body": "/html/body/div[3]/div[2]",
    }

    def verify_text_in_process_run_dependencies(self, search_text='PK Load Table Name'):
        text_body = self._get_text_from_activetab(self.custom_selectors["Text Body"])
        asserts.assert_true(search_text in text_body, "processrundendencies doesnot contain {0}".format(search_text))
        return self
    

