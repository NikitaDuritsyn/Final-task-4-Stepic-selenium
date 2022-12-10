from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators

class MainPage(BasePage):
     def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
