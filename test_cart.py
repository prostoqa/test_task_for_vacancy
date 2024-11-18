from pages.main_page import MainPage
from pages.cart_page import CartPage

link = "https://mega.readyscript.ru/"


def test_add_item_to_cart(driver):
    main = MainPage(driver)
    main.open_link(link)
    item_name = main.get_item_name()
    item_price = main.get_item_price() + " р."
    main.add_item_to_cart()
    cart = CartPage(driver)
    modal_window = cart.check_cart_modal_window()
    assert modal_window == (item_name, item_price, "1"), "Wrong item data in the modal window after adding to cart"
    # cart_on_main_page = main.get_items_and_price_on_cart()
    # assert cart_on_main_page == (1, item_price), "Wrong item data on main page cart after adding to cart"
    cart.go_to_cart_from_modal_window()
    cart_page = cart.check_cart_page()
    assert cart_page == ("Корзина:", item_name, item_price, "1"), "Wrong item data in the cart page after adding to cart"
    cart.delete_item_from_cart()
    # cart_on_main_page = main.get_items_and_price_on_cart()
    # assert cart_on_main_page == (0, "0 р."), "Wrong item data on main page cart after deleting from cart"
    main.go_to_cart_from_main_page()
    assert cart.get_empty_cart_title() == "Корзина пуста", "Cart isn't empty"