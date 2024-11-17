from pages.main_page import MainPage

link = "https://mega.readyscript.ru/"


def test_show_tablet_digma(driver):
    main = MainPage(driver)
    main.open_link(link)
    main.choose_digma_tablet()
    item_name = main.get_item_name()
    assert "Digma" in item_name, f"По фильтру Digma отображается {item_name}"
    #ToDo: add title digma and path
