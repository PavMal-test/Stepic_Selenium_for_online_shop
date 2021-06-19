# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 00:29:36 2021

@author: user
"""

from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators



class BasePage():
    def __init__(self, browser, url, timeout=6):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        self.browser.get(self.url)
        
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return False
        return True
    
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        
    def go_to_basket(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()