# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:41:17 2021

@author: user
"""

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):                    
    def should_be_basket_page(self):
        self.should_be_basket_url()
       
        
    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'basket' in self.browser.current_url, "Incorrect Basket URL"
        
    #def should_be_proceed_button(self):
        #assert self.is_element_present(*BasketPageLocators.BASKET_PROCEED_BTN), "There is no 'Proceed' button on page"   
        
        
        
        
    def should_not_be_goods_in_basket_title(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS_IN_BASKET_TITLE, timeout=2), \
        "There is goods-in-basket message"
        
    def should_be_empty_basket_message(self):
         assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
        "There is no basket-is-empty message"
        