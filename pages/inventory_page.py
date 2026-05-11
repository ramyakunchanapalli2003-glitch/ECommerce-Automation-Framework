from pages.base_page import BasePage
from utils.locators import InventoryPageLocators

class InventoryPage(BasePage):
    def add_backpack_to_cart(self):
        self.click(InventoryPageLocators.ADD_TO_CART_BACKPACK)

    def go_to_cart(self):
        self.click(InventoryPageLocators.CART_ICON)
        
    def get_cart_badge_count(self):
        if self.is_element_visible(InventoryPageLocators.CART_BADGE):
            return self.get_text(InventoryPageLocators.CART_BADGE)
        return "0"
