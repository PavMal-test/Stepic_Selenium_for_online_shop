# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 23:11:04 2021

@author: user
"""

from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn')
    
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn')
    
    
class LoginPageLocators():
    LOGIN_USERNAME_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_ENTER_BUTTON  = (By.CSS_SELECTOR, '[value="Log In"]')
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTTON = (By.CSS_SELECTOR, '[value="Register"]')
    
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > .price_color")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages > :nth-child(1) > div :nth-child(1)')
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, '#messages > :nth-child(3) > div :nth-child(1) > :nth-child(1)')
    
    
class BasketPageLocators():
    PRODUCT_TOTAL_PRICE = (By.CSS_SELECTOR, 'table  :nth-child(2) :nth-child(2)')
    #BASKET_TOTAL_TITLE = (By.CSS_SELECTOR, '.col-sm-4.col-sm-offset-8 a')
    BASKET_PROCEED_BTN = (By.CSS_SELECTOR, '.col-sm-4.col-sm-offset-8 a')
    BASKET_GOODS_IN_BASKET_TITLE = (By.CSS_SELECTOR, ".col-sm-6.h3")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')