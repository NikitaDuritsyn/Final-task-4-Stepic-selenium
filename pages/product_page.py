from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_be_add_product_button()
        add_button= self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()
        
    def should_be_add_product_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET),"Add button isn't displayed"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")    

    def get_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        return book_name
    
    def get_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        return book_price
    
    def compare_book_name_in_basket_and_in_cataloge(self, book_name):
        self.book_name = book_name
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET).get_attribute('textContent')
        assert book_name == book_name_in_basket, "Book name in basket isn't correct"

    def compare_price_in_basket_and_in_cataloge(self, book_price):
        self.book_price=book_price
        book_price_in_msg = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_MSG).text
        assert book_price == book_price_in_msg, "Book price isn't correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
               "Success message is presented, but should not be"

    def success_message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
               "Success message is not disappeared, but should be"





        
