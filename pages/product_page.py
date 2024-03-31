from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            'Add to basket button is not presented'

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def can_solve_quiz_and_get_code(self):
        assert self.solve_quiz_and_get_code(), \
            'Quiz not solved and code not received'

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

    def should_be_success_message_and_correct_book(self, correct_book):
        assert (correct_book ==
                self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_NAME).text), \
            'Book is not correct'

    def should_be_success_message_and_correct_price(self, correct_price):
        assert (correct_price ==
                self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_PRICE).text), \
            'Price is not correct'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is presented, but should not be'

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is presented, but should disappeared'
