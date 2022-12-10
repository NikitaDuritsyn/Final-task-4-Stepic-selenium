from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR,".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR,".product_main > h1")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR,"#messages > div:nth-child(1) .alertinner strong")  
    BOOK_PRICE = (By.CSS_SELECTOR,".product_main .price_color")        
    BOOK_PRICE_IN_MSG =  (By.CSS_SELECTOR,".alert-info .alertinner strong")        
    SUCCESS_MESSAGE =(By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) > .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    BASKET_MESSAGE=(By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS=(By.CSS_SELECTOR, ".basket-items")
   
class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
