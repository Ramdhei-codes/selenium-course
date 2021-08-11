import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class RealPythonTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver

        driver.get('https://realpython.com')
        driver.maximize_window()
        driver.implicitly_wait(15)

    
    def test_search_text_field(self):
        """Finding an element by its name"""
        self.driver.find_element_by_name('q')
    
    def test_card_body_element(self):
        """Finding an element by its class name"""
        self.driver.find_element_by_class_name('card-body')

    def test_list_of_tutorials(self):
        """Finding the list of tutorials from the realpython homepage"""
        resources_list = self.driver.find_element_by_css_selector('div.row')
        resource = resources_list.find_elements_by_class_name('col-12 col-md-6 col-lg-4 mb-5')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='report', report_name='tests-real-python'))