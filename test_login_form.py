from pages.main_page import MainPage
from pages.login_page import LoginPage

link = "https://mega.readyscript.ru/"


def test_user_login(driver):
    main = MainPage(driver)
    main.open_link(link)
    main.go_to_personal_account_to_login()
    auth = LoginPage(driver)
    auth.clear_authorization_data()
    auth.enter_authorization_data('test123@example.com', 'test123')
    assert main.check_successful_login(), "User is not authorized"
