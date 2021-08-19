import unittest
from selenium import webdriver

class BuyArticles(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()

        driver.get('https://www.saucedemo.com/')

    
    def test_buy_product(self):

        """Buying a product in the demo website"""

        driver = self.driver

        username_input = driver.find_element_by_id('user-name')
        username_input.send_keys('standard_user')

        password_input = driver.find_element_by_id('password')
        password_input.send_keys('secret_sauce')

        login_button = driver.find_element_by_id('login-button')
        login_button.click()

        self.assertEqual(driver.current_url, 'https://www.saucedemo.com/inventory.html')

        add_backpack_to_cart_button = driver.find_element_by_id('add-to-cart-sauce-labs-backpack')
        add_red_tshirt_to_cart_button = driver.find_element_by_id('add-to-cart-test.allthethings()-t-shirt-(red)')

        self.assertTrue(add_backpack_to_cart_button.is_displayed() and add_backpack_to_cart_button.is_enabled() and
        add_red_tshirt_to_cart_button.is_displayed() and add_red_tshirt_to_cart_button.is_enabled())

        add_backpack_to_cart_button.click()
        add_red_tshirt_to_cart_button.click()

        shopping_cart = driver.find_element_by_class_name('shopping_cart_link')
        shopping_cart.click()

        self.assertEqual(driver.current_url, 'https://www.saucedemo.com/cart.html')

        checkout_button = driver.find_element_by_id('checkout')

        self.assertTrue(checkout_button.is_enabled())

        checkout_button.click()

        self.assertEqual(driver.current_url, 'https://www.saucedemo.com/checkout-step-one.html')

        first_name = driver.find_element_by_id('first-name')
        last_name = driver.find_element_by_id('last-name')
        postal_code = driver.find_element_by_id('postal-code')

        first_name.send_keys('test')
        last_name.send_keys('test')
        postal_code.send_keys('17011')

        continue_button = driver.find_element_by_id('continue')

        continue_button.click()

        total = driver.find_element_by_class_name('summary_total_label')

        self.assertEqual(total.text, 'Total: $49.66')

        finish_purchase = driver.find_element_by_id('finish')

        finish_purchase.click()


    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)