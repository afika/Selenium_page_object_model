from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")

class CartPageLocators(object):
    MESSAGE_ABOUT_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    ITEMS_LIST = (By.CSS_SELECTOR, "#content_inner h2")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form>button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".content h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR,".content .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages .alertinner strong")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR,"#messages .alert-info strong")
