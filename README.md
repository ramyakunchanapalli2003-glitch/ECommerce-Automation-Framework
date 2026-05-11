# E-Commerce Website Testing Framework

A simple, robust Selenium automation testing framework built using Python and pytest. This project demonstrates best practices in test automation, including the Page Object Model (POM) design pattern and the exclusive use of explicit waits for stability.

## Features
- **Login Automation**: Valid login and negative testing (invalid login with error message validation).
- **Cart Management**: Add products, verify dynamic cart badge updates, and remove products.
- **Cart Validation**: Verifies product presence and ensures the cart updates correctly when items are removed.
- **Race Condition Handling**: Custom `BasePage` methods that wait for elements to appear *and* disappear (e.g., waiting for cart items to vanish from the DOM).
- **Clean Architecture**: Strict adherence to the Page Object Model (POM) to keep tests decoupled from UI locators.
- **Explicit Waits**: 100% reliance on Selenium's `WebDriverWait` for fast, non-flaky test execution (Zero use of `time.sleep()`).

## Project Structure
- `pages/`: Contains the Page Object classes (`base_page.py`, `login_page.py`, `inventory_page.py`, `cart_page.py`) that abstract page-specific interactions.
- `tests/`: Contains the actual pytest test scripts (`test_shopping_flow.py`).
- `utils/`: Contains centralized locators (`locators.py`) for easy maintenance.
- `conftest.py`: Manages the setup and teardown of the Selenium WebDriver using `pytest` fixtures.
- `pytest.ini`: Configuration for test discovery and verbosity.

## Getting Started

### Prerequisites
Make sure you have Python installed. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Running the Tests Locally
To execute the automation framework, simply run the following command in the root directory of the project:

```bash
pytest -v
```
