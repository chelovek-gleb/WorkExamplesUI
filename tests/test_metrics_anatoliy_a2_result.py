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
    metrics = metrics_page.check_metrics()

    metric_info = str(metrics) # из списка делаем строку

    assert "correctness" in metric_info, "Значения correctness нет в строке" #Проверяем что в строке есть значения
    assert "executed" in metric_info, "Значения executed нет в строке"
    assert "quickness" in metric_info, "Значения quickness нет в строке"
    

    time.sleep(5)