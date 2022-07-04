from selenium.webdriver.common.by import By


class Locators:
    '''
    ----------------------------------------------------------------
    |A dictionary for all locators in the Results Page.            |
    ------------------------------------------------------------------------------------------------------------------
    |@param: var1 -> If the element address needs an interpolation, this will be added on the selector address.       |
    |@param: var2 -> If the element address needs an interpolation, this will be added on the selector address.       | 
    |@param: var3 -> If the element address needs an interpolation, this will be added on the selector address.       |
    |@return: A tuple that consist attributes of By Class and the Selector Address                                    |
    ------------------------------------------------------------------------------------------------------------------
    ATTRIBUTES:  
    * [checkbox, columns, export, filter, graph, page, search_params]         
    '''
    def homepage(var1=None, var2=None, var3=None):
            return { 
                    "search_box" : (By.NAME, "q"),
                    "google_search_button" : (By.NAME, "btnK")
                    }
        
       
        