import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select as SelectOptions

class Select(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()

        driver.get('https://www.seleniumeasy.com/test/jquery-dropdown-search-demo.html')


    def test_select_options(self):
        driver = self.driver

        select_country = SelectOptions(driver.find_element_by_id('country'))

        options_text = []

        for option in select_country.options:
            options_text.append(option.text)

        self.assertEqual('', select_country.first_selected_option.text)

        select_country.select_by_visible_text('Netherlands')

        

    def tearDown(self):
        self.driver.quit()

    

if __name__ == '__main__':
    unittest.main(verbosity=2)