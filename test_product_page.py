from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from pytest import fixture, mark, param
from time import time


@mark.add_to_basket
class TestAddToBasketFromProductPage:
    @mark.need_review
    @mark.parametrize('num_offer', [*range(7), param(7, marks=mark.xfail), *range(8, 10)])
    def test_guest_can_add_product_to_basket(self, browser, num_offer):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num_offer}'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.add_product_to_basket()
        page.can_solve_quiz_and_get_code()
        book_name = page.get_product_name()
        book_price = page.get_product_price()
        page.should_be_success_message_and_correct_book(book_name)
        page.should_be_success_message_and_correct_price(book_price)

    @mark.xfail(reason='see step_4_3_6')
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link, 0)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link, 0)
        page.open()
        page.should_not_be_success_message()

    @mark.xfail(reason='see step_4_3_6')
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link, 0)
        page.open()
        page.add_product_to_basket()
        page.should_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_products()
        basket_page.should_be_message_about_basket_empty()


@mark.user_add_to_basket
class TestUserAddToBasketFromProductPage:
    @fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time()) + '@fakemail.org'
        password = str(time()) + 'fake-$[PASS]word'
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        product_page = ProductPage(browser, link, 0)
        product_page.open()
        product_page.should_not_be_success_message()

    @mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_add_to_basket_button()
        product_page.add_product_to_basket()
        product_page.can_solve_quiz_and_get_code()
        book_name = product_page.get_product_name()
        book_price = product_page.get_product_price()
        product_page.should_be_success_message_and_correct_book(book_name)
        product_page.should_be_success_message_and_correct_price(book_price)
