from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BOOK_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, 'div.alertinner strong')
    MESSAGE_BOOK_PRICE = (By.CSS_SELECTOR, 'div.alertinner p strong')
