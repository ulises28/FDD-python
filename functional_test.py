from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def SetUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #There is a fantastic new website who has incredible new features. 
        # So Edith as a new costumer opens it to check it out the homepage.
        self.browser.get('http://localhost:8000')

        #There is a huge title in the home page with the brand name
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

#She is invited to enter a to-do item straight away

#Customer types "Buy peacock feathers" into the text box 

#When the customer press 'enter' , the page updates, and now the page lists
#"1. Buy peacock feathers" as an item in a to-do list
#There is still a text box inviting customer to add another item. 

#Customer enters "Use peacock feathers to make a fly"

#The page updates again, and now shows both items on Customer list

#Customer wonders whether the site will remember his list. Then he sees
#That the site has generated a unique URL for him -- there is some
# Explanatory text to that effect

#Customer visits that URL - His to-do list is still there.

#Customer is satisfied and closes the browser

if __name__ == '__main__':
    unittest.main(warnings='ignore')