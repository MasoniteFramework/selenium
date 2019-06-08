import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from src.masonite.testing.selenium import SeleniumTestCase


class TestBrowser(unittest.TestCase, SeleniumTestCase):

    _has_prepared = False

    def setUp(self):
        if self._has_prepared:
            self.prepare()

            self.__class__._has_prepared = False

    def prepare(self):
        self.useBrowser('chrome', '74')

    @classmethod
    def setUpClass(cls):
        if hasattr(cls, 'prepare'):
            cls._has_prepared = True

    def test_visit(self):
        # (self.visit('http://python.org')
        #     .text('#id-search-field', 'Masonite')
        #     .submit('#submit').assertSee('Results'))

        # (self.visit('https://pypi.org/')
        #     .link('Log in')
        #     .assertSee('Log in to PyPI')
        #     .text('#username', 'josephmancuso')
        #     .text('#password', 'secret')
        #     .submit().assertSee('Your projects'))

        # (self.visit('https://websiteopedia.com/')
        #     .text('website', 'masoniteproject.com')
        #     .submit().assertSee('Web Analysis for masoniteproject.com'))

        (self.useBrowser('chrome').visit('https://gbaleague.com').link('Login')
            .text('username', 'idmann509@gmail.com')
            .text('password', 'secret')
            .submit()
            .assertSee('Invalid username or password', element='.alert')
            .assertCanSee('Invalid username or password', element=".alert"))

        # self.assertEqual(self.visit('http://python.org')
        #                  .text('#id-search-field', 'Masonite')
        #                  .value('#id-search-field'), 'Masonite')

