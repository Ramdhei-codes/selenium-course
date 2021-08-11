import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver

        driver.get('https://platzi.com/clases/inversion-bolsa/')
        driver.maximize_window()
        driver.implicitly_wait(30)
    
    def test_course_details(self):
        self.assertTrue(self.is_element_present(By.CLASS_NAME, 'CourseDetail-top'))

    def test_header_v2(self):
        self.assertTrue(self.is_element_present(By.ID, 'header-v2'))

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as exception:
            return False
        
        return True


if __name__ == '__main__':
        unittest.main(verbosity=2)
