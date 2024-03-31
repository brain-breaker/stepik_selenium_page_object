from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, 'basket')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p a')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#content_inner h3 a')


class LoginPageLocators:
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[value="Register"]')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BOOK_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, 'div.alertinner strong')
    MESSAGE_BOOK_PRICE = (By.CSS_SELECTOR, 'div.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success:nth-child(1)')
