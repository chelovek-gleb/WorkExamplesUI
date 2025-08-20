from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class MainPage(Base):
    """Класс главной страницы в админке sam"""

    # Locators

    calculation_schedule_locator = "//tr[@class='model-calculationschedule']//th//a" # кнопка перехода в расписание расчетов
    metric_calculations_locator = "//tr[@class='model-metriccalculation']//th//a" # кнопка перехода в metric calculations

    # Getters
    """Применяется явное ожидание к элементам по локатору"""
    def get_calculation_schedule(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.calculation_schedule_locator)))
    
    def get_metric_calculations(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.metric_calculations_locator)))
    
    # Actions
    """Методы перехода на страницы"""
    
    def click_calculation_schedule(self):
        self.get_calculation_schedule().click()
        print('Кликнули на расписания расчетов')

    def click_metric_calculations(self):
        self.get_metric_calculations().click()
        print('Кликнули на расчеты метрик')
        
