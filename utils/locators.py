from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

class InventoryPageLocators:
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

class CartPageLocators:
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
