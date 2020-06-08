from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()      

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('https://www.caliente.mx/')
        self.assertIn('Caliente.MX - Número 1 en apuestas en México', self.browser.title)

        registro = self.browser.find_element_by_id('regForm')
        self.assertTrue('REGISTRAR UNA CUENTA NUEVA', registro.find_element_by_class_name('regForm-no-reg-table-td-text'))

if __name__ == '__main__':
    unittest.main(warnings='ignore')
