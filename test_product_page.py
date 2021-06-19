# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:08:16 2021

@author: user
"""

import pytest
from .pages.product_page import ProductPage
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