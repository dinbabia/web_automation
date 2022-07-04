from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
from selenium.webdriver.remote import webelement
import time


"""
EC docu = https://selenium-python.readthedocs.io/waits.html
"""


class WebActions:
    """
    Contains Web Interactions.
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)
        

    def web_click(self, by_locator, element=None):
        '''Web Interaction: Basic left click on a web element
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @return : None
        '''
        if element != None:
            try:
                elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
                elements[element].click()
            except:
                elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
                self.driver.execute_script("arguments[0].click();", elements[element])
        else:

            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()
            except:

                try:
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()
                except:
                    element = self.driver.find_element(by_locator[0], by_locator[1])
                    self.driver.execute_script("arguments[0].click();", element)

    def web_element_visible(self, by_locator):
        '''Web Interaction: Check if the element is visible
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @return: boolean-> True if visible
        '''
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def web_get_all_elements(self, by_locator):
        '''Web Interaction: Get all elements and return it as a list
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @return: The title of the page as string
        '''
        elements = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(by_locator))
        return elements

    def web_get_element_text(self, by_locator, element=None):
        '''Web Interaction: Get the string/text of a web element
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @return: String/Text of a web element
        '''
        if element != None:
            elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
            return elements   

        else:
            try:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
                return element.text.strip()
            except:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
                return element.text.strip()

    def web_get_element_value(self, by_locator, options=None):
        '''Web Interaction: Get the value attribute of a web element
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @param: options -> If value but different attribute. e.g.[data-value]
        * @return: Value attribute of a web element
        '''
        try:
            if options == None:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
                return element.get_attribute('value')
            else:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
                return element.get_attribute(options)
        except:
            if options == None:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
                return element.get_attribute('value')
            else:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
                return element.get_attribute(options)

    def web_get_title(self):
        '''Web Interaction: Get the title of the webpage
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @return: The title of the page as string
        '''
        return self.driver.title

    def web_send_keys(self, by_locator, text, element=None):
        '''Web Interaction: Send a string to a web element
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @param: text -> The string to be inputted on an element
        * @return: None
        ''' 
        if element != None:
            elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
            elements[element].send_keys(text)
        else:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).send_keys(text)
            

    def web_wait(self, by_locator):
        '''Web Interaction: Wait for a certain element 
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @param: text -> The string to be inputted on an element
        * @return: None
        '''
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    
    def web_wait_absence(self, by_locator):
        '''Web Interaction: Wait for a certain element 
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @param: text -> The string to be inputted on an element
        * @return: None
        '''
        try:
            WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(by_locator))
            return False
        except:
            return True
        
    def web_wait_presence(self, by_locator):
        '''Web Interaction: Wait for a certain element 
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @param: text -> The string to be inputted on an element
        * @return: None
        '''
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
    
    def web_wait_presence_of_elements(self, by_locator):
        '''Web Interaction: Wait for all elements 
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @param: text -> The string to be inputted on an element
        * @return: None
        '''
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(by_locator))
    
    def web_wait_visible(self, by_locator):
        '''Web Interaction: Wait for a certain element 
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @param: text -> The string to be inputted on an element
        * @return: None
        '''
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
      
    def web_type_on_keyboard(self, text="", text2=None, press_enter=False, press_tab=False, timeout=6):
        '''Web Interaction: Keyboard keys are pressed 
            --------------------------------
        * @param: text -> The string to be inputted on an element
        * @press_enter -> Assign true if you want to press enter after typing the text
        * @press_tab -> Assign true if you want to press tab after pressing enter
        * @timeout -> Timeout assign after each action
        * @return: None
        '''
        time.sleep(2)
        action = ActionChains(driver=self.driver)
        if text2 == None:
            action.send_keys(text)
            if press_enter: action.send_keys(Keys.ENTER)
            action.perform()
            time.sleep(timeout)
            if press_tab: action.send_keys(Keys.TAB).perform()
        if text2 != None:
            action.send_keys(text)
            if press_enter: action.send_keys(Keys.ENTER)
            action.perform()
            time.sleep(timeout)
            if press_tab: action.send_keys(Keys.TAB)
            action.send_keys(text2)
            if press_enter: action.send_keys(Keys.ENTER)
            action.perform()
       
      
    def web_press_enter(self):
        '''Web Interaction: Keyboard Enter is pressed 
            --------------------------------
        * @param: text -> The string to be inputted on an element
        * @press_enter -> Assign true if you want to press enter after typing the text
        * @press_tab -> Assign true if you want to press tab after pressing enter
        * @timeout -> Timeout assign after each action
        * @return: None
        '''
        self.action.send_keys(Keys.ENTER).perform()
        time.sleep(2)

    def web_press_tab(self):
        '''Web Interaction: Keyboard Tab is pressed 
            --------------------------------
        * @param: text -> The string to be inputted on an element
        * @press_enter -> Assign true if you want to press enter after typing the text
        * @press_tab -> Assign true if you want to press tab after pressing enter
        * @timeout -> Timeout assign after each action
        * @return: None
        '''
        self.action.send_keys(Keys.TAB).perform()
        time.sleep(2)
        
    def web_clear_field(self, by_locator, element=None):
        '''Web Interaction: Command "Clear" is pressed 
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @return: None
        '''
        if element != None:
            elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
            elements[element].clear()  
        else:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).clear()
            
