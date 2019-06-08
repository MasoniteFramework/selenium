import os
from sys import platform

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ChromeDriver:

    def make(self, version='74'):
        chrome_driver_directory = os.path.join(os.path.dirname(__file__), self.get_platform(), self.get_platform_filename(version))
        return webdriver.Chrome(chrome_driver_directory)

    def get_platform(self):
        if platform == "linux" or platform == "linux2":
            return 'linux'
        elif platform == "darwin":
            # OS X
            return 'mac'
        elif platform == "win32":
            return 'windows'

    def get_platform_filename(self, version):
        if self.get_platform() == 'windows':
            return 'chromedriver{}.exe'.format(version)
        
        return 'chromedriver'+version