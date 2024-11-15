from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

link = "https://mega.readyscript.ru/"


def test_show_planshet_digma(driver):
    driver.get(link)
    catalog = driver.find_element(By.XPATH, '//span[text()="Каталог"]')
    catalog.click()
    elektronika = driver.find_element(By.XPATH, '//div[contains(@class, "head-dropdown-catalog")]'
                                                '/a[contains(@href, "/catalog/elektronika/")]')
    ActionChains(driver).move_to_element(elektronika).perform()
    planshety = driver.find_element(By.XPATH, '//div[contains(@class, "head-dropdown-catalog")]'
                                              '/a[contains(@href, "/catalog/planshety/")]')
    ActionChains(driver).move_to_element(planshety).perform()
    digma = driver.find_element(By.XPATH, '//a[contains(@href, "/catalog/digma/")]')
    ActionChains(driver).move_to_element(digma).click(digma).perform()
    item = driver.find_element(By.XPATH, '//a[contains(@class, "item-card__title")]')
    assert "Digma" in item.text, f"По фильтру Digma отображается {item.text}"
