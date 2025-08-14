import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
    # Настраиваем headless-режим
    options = Options()
    options.add_argument("--headless=new")  # для новых версий Chrome
    options.add_argument("--no-sandbox") # нужно для тестов В изолированных средах (Docker, GitLab CI,
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument("--disable-dev-shm-usage") # нужно для тестов В изолированных средах (Docker, GitLab CI,

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver  # Передаём управление в тест

    # После завершения теста
    driver.quit()