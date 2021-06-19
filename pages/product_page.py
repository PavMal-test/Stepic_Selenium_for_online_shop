# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:09:33 2021

@author: user
"""

from .main_page import MainPage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException
import time

class ProductPage(MainPage):                    #Т.к. у нас MainPage это не главная страница, а выходит общей частью всех страниц, наследум от неё
    def should_be_product_page(self):
        self.should_be_part_of_product_url()
        self.should_be_add_to_cart_button()

        
    def should_be_part_of_product_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'catalogue/' in self.browser.current_url, "Not a product page"
        
    def should_be_add_to_basket_button(self):
        # реализуйте проверку, что есть кнопка добавления в корзину
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add_to_basket_button is not presented"
        
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
       
    def get_product_name(self):
        product_name =  self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name
        print(product_name)
         
    def get_product_price(self):
        product_price =  self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price
        print(product_price)
        
    def correct_product_name_added(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
            self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text, "Incorrect added product name"
        
    def correct_product_price_added(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
            self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text, "Incorrect added product price"       
        
        
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
      
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")