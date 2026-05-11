import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

class TestShoppingFlow:
    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        
        # 1. Attempt login with invalid credentials
        login_page.login("invalid_user", "wrong_password")
        
        # 2. Verify error message appears
        error_text = login_page.get_error_message()
        assert "Epic sadface" in error_text, "Error message should contain 'Epic sadface'"

    def test_add_product_to_cart(self, driver):
        # 1. Login with valid credentials
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        # 2. Add one product to cart
        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()
        
        # 3. Verify cart badge updates correctly
        assert inventory_page.get_cart_badge_count() == "1", "Cart badge should be 1"
        
        # 4. Navigate to cart page
        inventory_page.go_to_cart()
        
        # 5. Verify product is present in cart
        cart_page = CartPage(driver)
        cart_item = cart_page.get_cart_item_name()
        
        assert cart_item == "Sauce Labs Backpack", f"Expected 'Sauce Labs Backpack' but found '{cart_item}'"

    def test_remove_product_from_cart(self, driver):
        # Setup: Login and add item to cart
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()
        inventory_page.go_to_cart()
        
        # 1. Remove product from cart
        cart_page = CartPage(driver)
        cart_page.remove_backpack()
        
        # 2. Verify cart is empty
        assert cart_page.is_cart_empty(), "Cart should be empty after removing the item"
