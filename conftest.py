import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Описываем, что ключ language обязателен для запуска данного теста
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")
# Описываем, фикстуру в которой будем открывать браузер с учетом языка, введенного пользователем
@pytest.fixture(scope="function")
def browser(request):
# Получаем значение параметра language из командной строки
    user_language = request.config.getoption("language")
    options = Options()
    # Запуск браузера с указанным языком пользователя
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
