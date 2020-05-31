from selenium import webdriver

browser = webdriver.Firefox()

#There is a fantastic new website who has incredible new features. 
# So Customer as a new costumer opens it to check it out the homepage
browser.get('http://localhost:8000')

#There is a huge title in the home page with the brand name
assert 'Villa Mascota' in browser.title

#Customer is invited to enter a to-do item straight away

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

browser.quit()