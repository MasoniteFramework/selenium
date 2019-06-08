from ..drivers.chrome.ChromeDriver import ChromeDriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

class SeleniumTestCase:

    drivers = {
        'chrome': ChromeDriver
    }

    current_browser = None

    def make_browser_if_not_exists(self):
        if self.current_browser:
            return self.current_browser
        
        self.current_browser = self.make('chrome', '74')
        return self.current_browser
        
    def browser(self, browser, version):
        self.current_browser = self.make(browser, version)
        return self
    
    def visit(self, url):
        self.current_browser = self.make_browser_if_not_exists()
        self.current_browser.get(url)
        return self
    
    def assertTitleIs(self, text):
        assert self.current_browser.title == text, "Title {} is not {}".format(text, self.current_browser.title)
        return self

    def assertTitleIsNot(self, text):
        assert self.current_browser.title != text, "Title is {}".format(self.current_browser.title)
        return self
    
    def assertSee(self, text):
        assert text in self.current_browser.find_element_by_tag_name('html').text, "{} is not in the body element".format(text)
        return self

    def assertCanSee(self, text):
        return self.assertSee(text)

    def find(self, element):
        if element.startswith('#'):
            return self.current_browser.find_element_by_id(element[1:])
        elif element.startswith('name='):
            return self.current_browser.find_element_by_name(element.split('=')[1])
        elif element.startswith('.'):
            return self.current_browser.find_element_by_class_name(element[1:])
        else:
            try:
                return self.current_browser.find_element_by_tag_name(element)
            except NoSuchElementException:
                return self.current_browser.find_element_by_name(element)

    def text(self, element, text):
        self.last_element = self.find(element)
        self.last_element.send_keys(text)
        return self
    
    def selectBox(self, element, value):
        element = Select(self.find(element))
        element.select_by_value(value)
        return self

    def check(self, element):
        return self.click(element)

    def link(self, text):
        element = self.current_browser.find_element_by_link_text(text)
        element.click()
        return self

    def value(self, element, value=None):
        if element.startswith('#'):
            if value is None:
                # Get the value
                return self.find(element).get_attribute("value")
            else:
                return self.text(element, text)
        
        return self
    
    def submit(self, element=None):
        if not element:
            self.last_element.submit()
            return self
        else:
            return self.click(element)
    
    def wait(self, seconds):
        time.sleep(seconds)
    
    def click(self, element):
        element = self.find(element)
        element.click()
        return self
    
    def clickLink(self, element):
        return self.link(element)
    
    def assertCantSee(self, text):
        assert self.current_browser.find_element_by_tag_name('body').text in text, "{} is not in the body element".format(text)
        return self

    def make(self, platform='chrome', version='74'):
        return self.drivers.get(platform)().make(version)