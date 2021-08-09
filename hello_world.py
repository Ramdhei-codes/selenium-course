import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)
    

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_real_python(self):
        self.driver.get('https://realpython.com/')


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='report', report_name='hola-mundo'))