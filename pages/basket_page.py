from .base_page import BasePage
from .locators import BasketPageLocators

languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida",
    "cs": "Váš košík je prázdný",
    "da": "Din indkøbskurv er tom",
    "de": "Ihr Warenkorb ist leer",
    "en": "Your basket is empty",
    "el": "Το καλάθι σας είναι άδειο",
    "es": "Tu carrito esta vacío",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide",
    "it": "Il tuo carrello è vuoto",
    "ko": "장바구니가 비었습니다",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty",
    "pt": "O carrinho está vazio",
    "pt-br": "Sua cesta está vazia",
    "ro": "Cosul tau este gol",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий",
    "zh-cn": "Your basket is empty",
}

class BasketPage(BasePage):
    
    def check_text_with_a_message_about_an_empty_basket(self):
        text = self.browser.find_element(
            *BasketPageLocators.BASKET_MESSAGE
        ).text
        text_lst = text.split('.')
        empty_text = text_lst[0]
        assert empty_text in languages.values(), \
            'Incorrect text with a message about an empty basket'

        
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS) == True,\
               "Items in basket are diplayed, but should not be"

    
