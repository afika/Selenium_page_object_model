from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
     def add_product_to_basket(self):
         add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
         add_button.click()

     def should_be_message_about_adding(self):
         assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"
         assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
         product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
         message_about_adding = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
         assert product_name == message_about_adding, "No product name in the message"

     def should_be_message_about_basket_total(self):
         assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
         assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), "Message about basket total is not presented"
         product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
         message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
         assert product_price == message_basket_total, "No product price in message about basket total"

     def should_not_be_success_message(self):
         assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
     def should_be_disappeared_success_message(self):
         assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is disappeared"
