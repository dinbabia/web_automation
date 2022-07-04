from driver import Driver
from _tools.web_actions import WebActions
from _tools.locators import Locators as loc

_driver = Driver().start_browser()
wa = WebActions(_driver)

def start_actions():
    # SEARCH ACTIONS
    # Try searching the exact word: "Selenium" to try this.
    search_text = input("What do you want to search? ")
    wa.web_send_keys(
        by_locator = loc.homepage()['search_box'], 
        text = search_text)

    wa.web_click(
        by_locator=loc.homepage()["google_search_button"])
    
    text = wa.web_get_element_text(
        by_locator=loc.homepage(var1=search_text)["search_text"])
    
    wa.web_click(
        by_locator=loc.homepage(var1=search_text)["search_text"])
    
    # RESULT PAGE
    print(_driver.current_url)
    text = wa.web_get_element_text(
        by_locator=loc.homepage()["result_page"])
    print(text)

start_actions()
_driver.close()


