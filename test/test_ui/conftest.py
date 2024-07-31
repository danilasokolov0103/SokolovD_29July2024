import allure
import pytest
from selenium import webdriver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        try:
            if "browser" in item.fixturenames:
                browser = item.funcargs["browser"]
                allure.attach(
                    browser.get_screenshot_as_png(),
                    name="Скриншот при падении",
                    attachment_type=allure.attachment_type.PNG,
                )

        except Exception:
            pass


@pytest.fixture
@allure.title("Запуск драйвера")
def browser():
    browser = webdriver.Chrome()

    browser.set_window_size(1920, 1080)

    yield browser

    browser.quit()
