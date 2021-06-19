# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:08:16 2021

@author: user
"""

import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time



def test_guest_can_add_item_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    prod_text = page.get_product_name()
    prod_price = page.get_product_price()
    page.correct_product_name_added()
    page.correct_product_price_added()
    page.go_to_basket()
    assert browser.find_element_by_link_text(prod_text), "Can't find product in basket"
    assert browser.find_element_by_css_selector('table  :nth-child(2) :nth-child(2)').text == prod_price, "Wrong price!"

@pytest.mark.skip    
@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_item_to_basket_with_promo(browser, url):
    link = url
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    prod_text = page.get_product_name()
    prod_price = page.get_product_price()
    page.correct_product_name_added()
    page.correct_product_price_added()
    page.go_to_basket()
   
    assert browser.find_element_by_link_text(prod_text), "Can't find product in basket"
 
    assert browser.find_element_by_css_selector('table  :nth-child(2) :nth-child(2)').text == prod_price, "Wrong price!"
    
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser) :
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
    
    