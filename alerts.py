import unittest
from time import sleep
from selenium import webdriver

class AlertsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)

        driver.get('https://www.seleniumeasy.com/test/javascript-alert-box-demo.html')


    def test_basic_alert(self):
        driver = self.driver

        basic_alert_button = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/button')

        basic_alert_button.click()

        alert = driver.switch_to.alert

        alert.accept()


    def test_prompt_alert(self):
        driver = self.driver

        prompt_alert_button = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[3]/div[2]/button')

        prompt_alert_button.click()

        alert =  driver.switch_to.alert

        self.assertEqual(alert.text, 'Please enter your name')

        alert.send_keys('Ramdhei López Arcila')

        sleep(10)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)