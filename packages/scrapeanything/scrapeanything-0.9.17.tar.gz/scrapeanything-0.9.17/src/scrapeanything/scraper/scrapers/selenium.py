from scrapeanything.scraper.scraper import Scraper

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException        
from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.remote.remote_connection import LOGGER

import logging
import platform
import base64

class Selenium(Scraper):

    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()
        
        options.add_argument('--no-sandbox')
        options.add_argument('--log-level=3')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-dev-shm-usage')

        if headless is True:
            options.add_argument('headless')

        LOGGER.setLevel(logging.WARNING)

        if platform.system() == 'Windows':
            self.driver = webdriver.Chrome(executable_path='c:\chromedriver.exe', options=options)
        if platform.system() == 'Linux':
            self.driver = webdriver.Chrome(executable_path='/chromedriver', options=options)
        
        self.handles = {}

        super().__init__()

    def on_wget(self, url):
        self.driver.get(url)
        return self.driver

    def on_xPath(self, path, element=None, timeout=0):

        try:
            el = self.on_exists(element=element, path=path, timeout=timeout)
            if el != False:
                return (self.driver if element is None else element).find_elements(by=By.XPATH, value=path)
            else:
                return None
        
        except NoSuchElementException:
            return None

        return element

    def on_exists(self, path, element, timeout=0):
        element = self.driver if element is None else element

        if timeout > 0:
            try:
                return WebDriverWait(element, timeout).until(
                    EC.presence_of_element_located((By.XPATH, path))
                )
            except Exception as e:
                return False
        else:
            try:
                return element.find_elements(by=By.XPATH, value=path)

            except NoSuchElementException:
                return False
            except StaleElementReferenceException:
                raise StaleElementReferenceException()

    def on_get_text(self, element):
        return element.text

    def on_get_html(self, element):
        return element.get_attribute('innerHTML')

    def on_get_attribute(self, element, prop):
        return element.get_attribute(prop)

    def on_click(self, path, element=None, timeout=0):
        element = self.on_xPath(path=path, element=element, timeout=timeout)

        if element is not None:
            if type(element) is list:
                element = element[0]

            try:
                self.driver.execute_script("arguments[0].click();", element)
            except Exception as e:
                element.click()                

            return element
        else:
            return None

    def on_back(self):
        self.driver.back()

    def on_get_current_url(self):
        return self.driver.current_url

    def on_enter_text(self, path: str, text: str, clear: bool=False, element: any=None, timeout: int=0):
        element = self.on_xPath(path=path, element=element, timeout=timeout)
        if element is not None:
            if type(element) is list:
                element = element[0]

            if clear is True:
                element.send_keys(Keys.CONTROL + 'a')
                element.send_keys(Keys.BACKSPACE)

            element.send_keys(text)
            return True
        else:
            return False

    def on_solve_captcha(self, path):
        pass

    def on_login(self, username_text=None, username=None, password_text=None, password=None):
        self.on_enter_text(username_text, username)
        self.on_enter_text(password_text, password)

        self.on_click('//button[@class="sign-in-form__submit-button"]')

    def on_search(self, path=None, text=None):
        self.on_enter_text(path, text)
        return self.on_enter_text(path, Keys.RETURN)

    def on_scroll_to_bottom(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def on_get_scroll_top(self):
        return self.driver.execute_script('return document.documentElement.scrollTop;')

    def on_get_scroll_bottom(self):
        return self.driver.execute_script('return document.body.scrollHeight')

    def on_select(self, path: str, option: str, element: any=None) -> None:
        element = WebDriverWait(self.driver if element is None else element, 10).until(
            EC.presence_of_element_located((By.XPATH, path))
        )

        if element is not None:
            Select(element).select_by_visible_text(option)

    def on_get_image_from_canvas(self, path, local_path, element):
        image_filename = f'{local_path}/image.png'

        # get the base64 representation of the canvas image (the part substring(21) is for removing the padding "data:image/png;base64")
        base64_image = self.driver.execute_script(f'return document.querySelector("{path}").toDataURL("image/png").substring(21);')

        # decode the base64 image
        output_image = base64.b64decode(base64_image)

        # save to the output image
        with open(image_filename, 'wb') as f:
            f.write(output_image)

        return image_filename

    def on_close(self):
        self.driver.quit()