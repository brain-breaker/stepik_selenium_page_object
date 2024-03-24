from .pages.product_page import ProductPage
from pytest import mark, param


@mark.basket_guest
class TestBasketFromProductPage:
    @mark.parametrize('num_offer', [*range(7), param(7, marks=mark.xfail), *range(8, 10)])
    def test_guest_can_add_product_to_basket(self, browser, num_offer):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num_offer}'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()  # проверяем, что есть кнопка добавления в корзину
        page.add_product_to_basket()  # жмем кнопку добавить в корзину
        page.can_solve_quiz_and_get_code()  # проверяем, что можем решить задачу и получить код
        book_name = page.get_product_name()
        book_price = page.get_product_price()
        page.should_be_success_message_and_correct_book(book_name)  # проверяем, что есть сообщение с правильной книгой
        page.should_be_success_message_and_correct_price(book_price)  # проверяем, что есть сообщение с правильной ценой
