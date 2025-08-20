from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class MetricsCalculations(Base):
    """Класс страницы Metric Calculations - расчеты метрик"""

    filter = 'Anatoliy A2' # значение для фильтрации
    # Locators
    
    filter_locator = f"//details[@data-filter-title='service']//ul//li//a[text()='{filter}']" # локатор фильтра с подставляемым значением

    """Локаторы разделены по группам. Дата и результат относящиеся к Anatoliy A2 - correctness"""
    correctness_locator = "(//div[@class='results']//table//tbody//tr//th//a[text()='Anatoliy A2 - correctness'])[1]"
    correctness_date_locator = "(//div[@class='results']//table//tbody//tr//td[@class='field-calculation_date nowrap'])[1]"
    correctness_result_locator = "(//div[@class='results']//table//tbody//tr//td[@class='field-get_result_preview']//span)[1]"

    """ Дата и результат относящиеся к Anatoliy A2 - quckness"""
    quckness_locator = "(//div[@class='results']//table//tbody//tr//th//a[text()='Anatoliy A2 - quickness'])[1]"
    quckness_date_locator = "(//div[@class='results']//table//tbody//tr//td[@class='field-calculation_date nowrap'])[2]"
    quckness_result_locator = "(//div[@class='results']//table//tbody//tr//td[@class='field-get_result_preview']//span)[2]"

    """ Дата и результат относящиеся к Anatoliy A2 - executed"""
    executed_locator = "(//div[@class='results']//table//tbody//tr//th//a[text()='Anatoliy A2 - executed'])[1]"
    executed_date_locator = "(//div[@class='results']//table//tbody//tr//td[@class='field-calculation_date nowrap'])[3]"
    executed_result_locator = "(//div[@class='results']//table//tbody//tr//td[@class='field-get_result_preview']//span)[3]"


    # Getters
    """Применяется явное ожидание к элементам по локатору"""
    def get_filter(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_locator)))
    
    #correctness
    """Аналогично локаторам, геттеры разделены по группам"""
    def get_correctness(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.correctness_locator)))
    
    def get_correctness_date(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.correctness_date_locator)))
    
    def get_correctness_result(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.correctness_result_locator)))
    
    #quckness
    def get_quckness(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.quckness_locator)))
    
    def get_quckness_date(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.quckness_date_locator)))
    
    def get_quckness_result(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.quckness_result_locator)))
    
    #executed
    def get_executed(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.executed_locator)))
    
    def get_executed_date(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.executed_date_locator)))
    
    def get_executed_result(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.executed_result_locator)))
    
    # Actions

    def click_filter(self):
        self.get_filter().click()
        print(f'Кликнули по фильтру {self.filter}')


    # correctness
    """Методы проверки наименования метрики, даты и результата"""
    def get_text_correctness(self):
        info = self.get_correctness().text
        print(f'Метрика: {info}')
        assert info == 'Anatoliy A2 - correctness', 'Наименование метрики не совпадает!'

    def get_text_correctness_date(self):
        info = self.get_correctness_date().text
        print(f'Дата: {info}')

    def get_text_correctness_result(self):
        info = self.get_correctness_result().text
        print(f'Результат: {info}\n')


    # quckness
    def get_text_quckness(self):
        info = self.get_quckness().text
        print(f'Метрика: {info}')
        assert info == 'Anatoliy A2 - quickness', 'Наименование метрики не совпадает!'

    def get_text_quckness_date(self):
        info = self.get_quckness_date().text
        print(f'Дата: {info}')

    def get_text_quckness_result(self):
        info = self.get_quckness_result().text
        print(f'Результат: {info}\n')


    # executed
    def get_text_executed(self):
        info = self.get_executed().text
        print(f'Метрика: {info}')
        assert info == 'Anatoliy A2 - executed', 'Наименование метрики не совпадает!'

    def get_text_executed_date(self):
        info = self.get_executed_date().text
        print(f'Дата: {info}')

    def get_text_executed_result(self):
        info = self.get_executed_result().text
        print(f'Результат: {info}\n')


    # Methods
    """Метод запуска всех проверок по выбранному фильтру"""
    def check_metrics(self):
        self.click_filter()
        self.get_text_correctness()
        self.get_text_correctness_date()
        self.get_text_correctness_result()

        self.get_text_quckness()
        self.get_text_quckness_date()
        self.get_text_quckness_result()

        self.get_text_executed()
        self.get_text_executed_date()
        self.get_text_executed_result()