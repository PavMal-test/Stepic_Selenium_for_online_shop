# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 00:35:47 2021

@author: user
"""

from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    
       
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        
    def go_to_login_page(self):
       login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
       login_link.click()
       
    def go_to_basket(self):
        basket_link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        basket_link.click()
        
      