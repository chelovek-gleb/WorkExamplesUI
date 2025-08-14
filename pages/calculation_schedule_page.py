from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CalculationSchedulePage(Base):
    """Класс продуктов представленных на странице"""

    # Locators
    filter = 'Anatoliy A2'

    search_bar_locator = "//input[@id='searchbar']"
    search_button_locator = "//input[@value='Search']"
    filter_locator = f"//details[@data-filter-title='service']//ul//li//a[text()='{filter}']"
    checkbox_all_locator = "//input[@id='action-toggle']"
    actions_locator = "//select[@name='action']"
    run_calculation_locator = "//option[@value='run_calculation']"
    go_button_locator = "//button[@title='Run the selected action']"

    # Getters

    def get_search_bar(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.search_bar_locator)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.search_button_locator)))
    
    def get_filter(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_locator)))
    
    def get_checkbox_all(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_all_locator)))
    
    def get_actions(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.actions_locator)))
    
    def get_run_calculation(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.run_calculation_locator)))
    
    def get_go_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.go_button_locator)))
    
    # Actions

    """ def click_search_button(self):
        self.get_search_button().click()
        print('Кликнули кнопку поиска')"""

    def click_filter(self):
        self.get_filter().click()
        print(f'Кликнули по фильтру {filter}')

    def click_checkbox_all(self):
        self.get_checkbox_all().click()
        print(f'Кликнули по всем чекбоксам')

    def click_actions(self):
        self.get_actions().click()
        print(f'Кликнули раскрыть действия')

    def click_calculation(self):
        self.get_run_calculation().click()
        print(f'Кликнули запустить расчет метрики в фильтре')

    def click_go_button(self):
        self.get_go_button().click()
        print(f'Кликнули кнопку Go')
    

    # Methods

    """def execute_search(self, text):
        self.get_search_bar().send_keys(text)
        print('Заполнили поле поиска')
        self.click_search_button()"""

    def start_metric_calculation(self):
        self.click_checkbox_all()
        self.click_actions()
        self.click_calculation()
        self.click_go_button()

        


        