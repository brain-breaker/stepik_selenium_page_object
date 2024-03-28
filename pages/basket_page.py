from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_about_basket_empty(self):
        message = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET)
        assert message.get_attribute('href') in self.browser.current_url, \
            'Message about basket empty is not presented'

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Product in basket, but should not be"
