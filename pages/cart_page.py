from pages.base_page import BasePage
from utils.locators import CartPageLocators

class CartPage(BasePage):
    def get_cart_item_name(self):
        return self.get_text(CartPageLocators.CART_ITEM_NAME)
        
    def is_product_in_cart(self, product_name):
        item_name = self.get_cart_item_name()
        return product_name in item_name

    def remove_backpack(self):
        self.click(CartPageLocators.REMOVE_BACKPACK)
        
    def is_cart_empty(self):
        # Wait for the cart item to be removed from the DOM
        return self.is_element_invisible(CartPageLocators.CART_ITEM)
