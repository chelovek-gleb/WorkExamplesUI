from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class AuthorizationPage(Base):

    

    url = 'https://sam.big3.ru/admin/login/?next=/admin/'

    # Locators

    username_locator = "//input[@name='username']"
    password_locator = "//input[@name='password']"
    log_in_locator = "//input[@type='submit']"

    # Getters

    def get_username(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.username_locator)))

    def get_password(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.password_locator)))
    
    def get_log_in(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.log_in_locator)))
    
    # Actions

    def send_username(self, username):
        self.get_username().send_keys(username)
        print('Заполнили логин')
        
    def send_password(self, password):
        self.get_password().send_keys(password)
        print('Заполнили пароль')

    def click_log_in(self):
        self.get_log_in().click()
        print('Кликнули Log in')

    # Methods

    def authorization(self, username, password):
        self.driver.get(self.url)
        self.send_username(username)
        self.send_password(password)
        self.click_log_in()
        