import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)

        driver.get('http://demo-store.seleniumacademy.com')

    def test_cart_link(self):
        """Waiting for the cart element to appear and clicking it"""
        cart = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header"]/div/div[2]/div/div/a')))
        cart.click()

    
    def test_search_tee(self):
        """Adding an element to cart using waits"""

        search_field = self.driver.find_element_by_name('q')
        search_field.send_keys('tee')
        search_field.submit()

        view_details_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/a')))
        view_details_button.click()

        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '.button .btn-cart')))
        add_to_cart_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)