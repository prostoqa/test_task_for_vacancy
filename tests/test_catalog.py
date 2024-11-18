from pages.main_page import MainPage


def test_show_tablet_digma(driver):
    main = MainPage(driver)
    main.open_link()
    main.choose_digma_tablet()
    item_name = main.get_item_name()
    title_name = main.get_title_name()
    assert "Digma" in item_name, f"When Digma is selected, {item_name} is displayed"
    assert title_name == "Digma", f"{title_name} section is open instead of Digma"
    assert main.check_breadcrumb_digma(), "Digma is not found in the breadcrumbs"
