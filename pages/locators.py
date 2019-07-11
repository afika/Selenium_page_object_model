from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form>button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".content h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR,".content .price_color")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR,"#messages .alertinner")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR,"#messages .alert-info")
