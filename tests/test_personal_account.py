from config import USER_LOGIN, USER_PASSWORD
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_user_login(driver):
    main = MainPage(driver)
    main.open_link()
    main.go_to_personal_account_to_login()
    auth = LoginPage(driver)
    auth.clear_authorization_data()
    auth.enter_authorization_data(USER_LOGIN, USER_PASSWORD)
    assert main.check_successful_login(), "User is not authorized"
