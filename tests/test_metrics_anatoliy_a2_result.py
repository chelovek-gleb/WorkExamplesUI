import time
from pages.metrics_calculations import MetricsCalculations
from pages.authorization_page import AuthorizationPage
from pages.main_page import MainPage
import os
from dotenv import load_dotenv

load_dotenv()


"""https://testit.big3.ru/projects/13490/tests/24814
Должна собираться метрика "времени (скорости) ответа"
"""

"""Этот тест запускается отдельно через некоторе время после прохождения первого теста с запуском расчета метрик, 
    так как нужно чтобы метрики успели рассчитаться. Поэтому в этом тесте браузер открывается заново
    """

def test_metricstest_metrics_anatoliy_a2_result(browser):

    username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")

    #Объявление экземпляров класса
    metrics_page = MetricsCalculations(browser)
    authorization_page = AuthorizationPage(browser)
    main_page = MainPage(browser)

    #Авторизация
    authorization_page.authorization(username, password)

    #Главная страница
    main_page.click_metric_calculations()

    #Фильтруем по нужной метрике
    metrics_page.check_metrics()

    time.sleep(5)