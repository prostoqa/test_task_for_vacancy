from pages.favorite_page import FavoritePage
from pages.main_page import MainPage


def test_add_item_to_favorite_and_delete(driver):
    main = MainPage(driver)
    main.open_link()
    item_name = main.get_item_name()
    main.add_item_to_favorite()
    assert main.get_amount_on_favorite_icon() == "1", "Doesn't have amount 1 on favorite icon after adding the item"
    main.go_to_favorite_page()
    favorite = FavoritePage(driver)
    assert favorite.get_favorite_page_title() == "Избранное", "It isn't favorite page"
    assert favorite.get_favorite_item_name() == item_name, "Favorite item doesn't match with added to favorite"
    favorite.delete_item_from_favorite()
    assert favorite.get_empty_favorite() == "Нет товаров в избранном", "Favorite isn't empty"
    assert main.get_no_amount_on_favorite_icon(), "Favorite icon amount isn't empty"
