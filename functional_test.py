from selenium import webdriver
from selenium.webdriver.common import keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()      

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # There is a fantastic new website who has incredible new features.
        # So Edith as a new costumer opens it to check it out the homepage.
        self.browser.get('http://localhost:8000')

        # There is a huge title in the home page with the brand name
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_elements_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into the text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits 'enter', the page updates, and now the page lists
        # "1. Buy peacock feathers" as an item in a to-do list table
        input.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_elements_by_id('id_lisy_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # There is still a text box inviting she to add another item.
        # She enters "Use peacock feathers to make a fly"
        self.fail('Finish the test!')    

# The page updates again, and now shows both items on Customer list

# Customer wonders whether the site will remember his list. Then he sees
# That the site has generated a unique URL for him -- there is some
# Explanatory text to that effect

# Customer visits that URL - His to-do list is still there.
# Customer is satisfied and closes the browser
if __name__ == '__main__':
    unittest.main(warnings='ignore')
