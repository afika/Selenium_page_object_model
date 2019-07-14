from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_cart_page(self):
        self.should_be_cart_url()
        self.should_be_empty()
        self.should_be_message_about_empty()

    def should_be_cart_url(self):
        assert "/basket" in self.browser.current_url, "The page is not basket url"

    def should_be_empty(self):
        self.is_not_element_present(*CartPageLocators.ITEMS_LIST), "Products inside basket, but should not be"

    def should_be_message_about_empty(self):
        assert self.is_element_present(*CartPageLocators.MESSAGE_ABOUT_EMPTY),"The message about empty basket is not presented"
        if "/en-gb/" in self.browser.current_url:
           message_about_empty = self.browser.find_element(*CartPageLocators.MESSAGE_ABOUT_EMPTY).text
           assert message_about_empty  == "Your basket is empty. Continue shopping", \
               "Wrong message about empty basket: \"{}\" should be \"Your basket is empty. Continue shopping\"".format(message_about_empty)
