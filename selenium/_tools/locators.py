from selenium.webdriver.common.by import By


class Locators:
    '''
    ----------------------------------------------------------------
    |A dictionary for all locators in the Results Page.            |
    ------------------------------------------------------------------------------------------------------------------
    |@param: var1 -> If the element address needs an interpolation, this will be added on the selector address.       |
    |@param: var2 -> If the element address needs an interpolation, this will be added on the selector address.       | 
    |@param: var3 -> If the element address needs an interpolation, this will be added on the selector address.       |
    |@return: A tuple that consist of attributes of By Class and the Selector Address                                    |
    ------------------------------------------------------------------------------------------------------------------
    Current Page Address Methods:  
    * [homepage]         
    '''
    def homepage(var1=None, var2=None, var3=None):
            '''
            Current Page Address Methods:  
                * [search_box, google_search_button, search_text, result_page]  
            '''
            return { 
                    "search_box" : (By.NAME, "q"),
                    "google_search_button" : (By.NAME, "btnK"),
                    "search_text" : (By.XPATH, f"//h3[text()='{var1}']"),
                    "result_page" : (By.XPATH, "//h1")
                    }
       
        