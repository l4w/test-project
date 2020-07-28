from selenium.webdriver.common.by import By

class MainPageLocators:
    
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:

    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators:

    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ITEM_NAME_IN_BASKET = (By.CSS_SELECTOR, '.alertinner strong')
    ITEM_PRICE_IN_BASKET = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    BASKET_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, '.alert-info')