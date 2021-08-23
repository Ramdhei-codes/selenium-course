import unittest
from time import sleep
from selenium import webdriver


class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)

        driver.get('https://www.google.com')

    def test_navigation(self):

        driver = self.driver

        search_field = driver.find_element_by_name('q')

        search_field.clear()
        search_field.send_keys('Backend challenges')

        search_field.submit()

        sleep(7)

        driver.back()
        sleep(3)
        driver.refresh()
        sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)