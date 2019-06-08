import os
from sys import platform

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FirefoxDriver:

    def make(self, version='74'):
        driver_directory = os.path.join(os.path.dirname(
            __file__), self.get_platform(), self.get_platform_filename(version))
        return webdriver.Firefox(executable_path=driver_directory)

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
            return 'geckodriver-{}.exe'.format(self.get_architecture())
        elif self.get_platform() == 'linux':
            return 'geckodriver-{}'.format(self.get_architecture())
        else:
            return 'geckodriver'

    def get_architecture(self):
        if platform.machine().endswith('64'):
            return '64'
        
        return '32'
