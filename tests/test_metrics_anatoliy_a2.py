import time
from pages.calculation_schedule_page import CalculationSchedulePage
from pages.authorization_page import AuthorizationPage
from pages.main_page import MainPage
import os
from dotenv import load_dotenv

load_dotenv()

"""https://testit.big3.ru/projects/13490/tests/24814
Должна собираться метрика "времени (скорости) ответа"
"""

def test_metricstest_metrics_anatoliy_a2(driver):

    username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")

    #Объявление экземпляров класса
    calc_page = CalculationSchedulePage(driver)
    authorization_page = AuthorizationPage(driver)
    main_page = MainPage(driver)

    #Авторизация
    authorization_page.authorization(username, password)

    #Главная страница
    main_page.click_calculation_schedule()

    #Фильтруем по нужной метрике
    calc_page.click_filter()
    calc_page.start_metric_calculation()

    time.sleep(5)