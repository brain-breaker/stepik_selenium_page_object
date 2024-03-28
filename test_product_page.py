from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from pytest import mark, param


@mark.basket_guest
class TestBasketFromProductPage:
    @mark.parametrize('num_offer', [*range(7), param(7, marks=mark.xfail), *range(8, 10)])
    def test_guest_can_add_product_to_basket(self, browser, num_offer):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num_offer}'
        page = ProductPage(browser, link)
        page.open()
        # page.should_not_be_success_message()  # ожидаем, что там нет сообщения об успешном добавлении в корзину
        page.should_be_add_to_basket_button()  # проверяем, что есть кнопка добавления в корзину
        page.add_product_to_basket()  # жмем кнопку добавить в корзину
        page.can_solve_quiz_and_get_code()  # проверяем, что можем решить задачу и получить код
        book_name = page.get_product_name()
        book_price = page.get_product_price()
        page.should_be_success_message_and_correct_book(book_name)  # проверяем, что есть сообщение с правильной книгой
        page.should_be_success_message_and_correct_price(book_price)  # проверяем, что есть сообщение с правильной ценой
        # page.should_disappeared_success_message()  # сообщение об успешном добавлении в корзину должно исчезнуть

    @mark.smoke
    @mark.xfail(reason='see step_4_3_6')
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link, 0)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()

    @mark.smoke
    def test_guest_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link, 0)
        page.open()
        page.should_not_be_success_message()

    @mark.smoke
    @mark.xfail(reason='see step_4_3_6')
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link, 0)
        page.open()
        page.add_product_to_basket()
        page.should_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
