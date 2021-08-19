import unittest
from selenium import webdriver
class SearchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)

        driver.get('https://platzi.com')
        


    def test_search_course(self):
        """Finding a course by its name"""
        driver = self.driver

        search_field = driver.find_element_by_name('search')
        search_field.clear()

        search_field.send_keys('Curso profesional de python')
        search_field.submit()

    def test_search_topic(self):
        """Finding the list of elements of a certain topic"""
        driver = self.driver

        search_field = driver.find_element_by_name('search')
        search_field.clear()

        search_field.send_keys('backend python')
        search_field.submit()

        results = driver.find_element_by_class_name('SearcherMaterial-list')
        results_list = results.find_elements_by_tag_name('li')

        self.assertEqual(15, len(results_list))


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
        unittest.main(verbosity=2)