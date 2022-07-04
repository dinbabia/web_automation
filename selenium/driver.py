from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import argparse
import os


# Add browser parameters
parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("-b", "--browser", help="| Choose Chrome Browser. Only firefox and chrome browser options can be selected.", default="chrome")
args = parser.parse_args()

class Driver:
     
    def __init__(self) -> None:
        self.browser = args.browser
        self.parent_url = ""

    def start_browser(self, **kwargs):
        self.parent_url =  "https://www.google.com/" if kwargs.get("url") == None else kwargs.get("url")
        
        if self.browser == "chrome":
            
            """You can change/add options for the browser here."""
            options = webdriver.ChromeOptions()
            # options.headless = True
            download_dir = os.getcwd()
            prefs = {
                "download.default_directory": f"{download_dir}\\tools"}
            options.add_experimental_option("prefs", prefs)
            options.add_argument('--log-level=3')
            
            #Add this if a specific website is very slow, hence it downloads many libraries, images and plugins. {normal, eager(interactive), none}
            c_caps = DesiredCapabilities().CHROME.copy()
            c_caps["pageLoadStrategy"] = "eager" 
            
            count = 0
            maxTries = 3
            while count != maxTries:
                try:
                    web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, desired_capabilities=c_caps)
                    web_driver.maximize_window()
                    web_driver.get(self.parent_url)
                    break
                except Exception as e:
                    print (e)
                    count += 1
                    
        elif self.browser == "firefox":
        
            """You can change/add options for the browser here."""
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            download_dir = os.getcwd()

            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.helperApps.alwaysAsk.force", False)
            profile.set_preference("browser.download.dir", f"{download_dir}\\tools")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv, application/pdf")
            profile.set_preference("pdfjs.disabled", True)
            profile.set_preference("browser.download.panel.shown", False)
            
            #Add this if a specific website is very slow, hence it downloads many libraries and plugins. {normal, eager(interactive), none}
            ff_caps = DesiredCapabilities().FIREFOX.copy()
            ff_caps["pageLoadStrategy"] = "normal" 
            
            count = 0
            maxTries = 3
            while count != maxTries:
                try:
                    web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile, options=options, desired_capabilities=ff_caps)
                    web_driver.maximize_window()
                    web_driver.get(self.parent_url)
                    break
                except Exception as e:
                    print (e)
                    count += 1
                    
        return web_driver
