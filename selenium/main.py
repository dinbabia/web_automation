from driver import Driver
from _tools.web_actions import WebActions
from _tools.locators import Locators as loc



_driver = Driver().start_browser()
wa = WebActions(_driver)

search_text = input("What do you want to search? ")
wa.web_send_keys(
    by_locator = loc.homepage()['search_box'], 
    text = search_text)

wa.web_click(
    by_locator=loc.homepage()["google_search_button"])


