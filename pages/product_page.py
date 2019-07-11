from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
     def add_product_to_basket(self):
         add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
         add_button.click()
     def should_be_message_about_adding(self):
         assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Message about adding product to basket is not presented"
         assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
         product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
         message_about_adding = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
         assert product_name == message_about_adding[0:len(product_name)], "No product name in the message"
         if "/en-gb/" in self.browser.current_url:
               assert "has been added to your basket." in message_about_adding, "Product is not success adding to basket"

     def should_be_message_about_basket_total(self):
         assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
         assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), "Message about basket total is not presented"
         product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
         message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
         assert product_price in message_basket_total, "No product price in message about basket total price" 
