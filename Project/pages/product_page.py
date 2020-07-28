from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        basket_button.click()

    def should_be_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_MESSAGE), 'There is no message about adding the item to basket.'

    def should_be_basket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), 'There is no message with basket price.'
    
    def should_add_correct_item_to_basket(self):
        item = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        item_in_basket = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_BASKET)

        assert item.text == item_in_basket.text, 'Item name in the basket doesnt match the product name.'
    
    def should_be_correct_price_in_basket(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_IN_BASKET)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)

        assert item_price.text == basket_price.text, 'Item cost doesnt match the number in the basket.'

        

    