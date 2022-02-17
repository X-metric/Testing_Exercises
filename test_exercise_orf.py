import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="module")
def brave_driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    settings = webdriver.ChromeOptions()
    settings.binary_location = brave_path
    settings.add_argument("--incognito")
    # settings.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=settings)

    yield driver

    driver.quit()

def test_first(brave_driver):
    # Arrange
    brave_driver.get("https://radiothek.orf.at/search")
    search_bar = brave_driver.find_element(By.CSS_SELECTOR, "input[type=search]")
    confirm_button = brave_driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    result_is_present = EC.presence_of_element_located((By.CSS_SELECTOR, "h2.results-title"))
    search_text = "Nachmittag"

    # Act
    search_bar.send_keys(search_text)
    confirm_button.click()
    result_text = WebDriverWait(brave_driver, 10).until(result_is_present)
    # print(brave_driver.get_cookies())

    # Assert
    assert result_text.text == f'Suchergebnis für "{search_text}"'


def test_second(brave_driver):
    # Arrange
    # brave_driver.get("https://radiothek.orf.at/search")
    # search_bar = brave_driver.find_element(By.CSS_SELECTOR, "input.search-input")
    # confirm_button = brave_driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # search_text = "Nachmittag"
    span_results = brave_driver.find_elements(By.XPATH, "//span[@class='type']")
    dict_span_results = {}

    # Act
    # search_bar.send_keys(search_text)
    # confirm_button.send_keys(Keys.RETURN)
    for i in span_results:
        if i.text in dict_span_results:
            dict_span_results[i.text] += 1
        else:
            dict_span_results[i.text] = 1
    print(dict_span_results)
    # result_is_present = EC.presence_of_element_located((By.CSS_SELECTOR, "h2.results-title"))
    # result_text = WebDriverWait(brave_driver, 10).until(result_is_present)

    # Assert
    assert len(dict_span_results) >= 1

def test_third(brave_driver):
    # Arrange
    search_option = brave_driver.find_element(By.CSS_SELECTOR,"span[title='Alle Sender']")

    # Act
    search_option.click()
    search_option.location_once_scrolled_into_view
    result_is_present = EC.presence_of_element_located((By.CSS_SELECTOR, "li[value=vbg]"))
    search_location = WebDriverWait(brave_driver, 10).until(result_is_present)
    search_location.click()
    time.sleep(2)
    new_results = brave_driver.find_elements(By.XPATH, "//span[@class='type']")
    dict_new_results = {}

    for i in new_results:
        if i.text in dict_new_results:
            dict_new_results[i.text] += 1
        else:
            dict_new_results[i.text] = 1

    print(dict_new_results)

    # Assert
    assert len(dict_new_results) == 1
