import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
print(f'This script is for "test automation" of  "wikipedia web-page" using selenium tool in python. \n Start test at : {datetime.datetime.now()}')
print(f'----------------*&*--------------')


# 1. Using Selenium WebDriver, open the web browser.
s = Service(executable_path='/Users/reza/PycharmProjects/pythonProject/chromedriver')
driver = webdriver.Chrome(service = s)
driver.implicitly_wait(30)
print(' Chrome web browser was opened')
time.sleep(.25)

# 2. Maximize the browser window.
driver.maximize_window()

# 3. Navigate to https://en.wikipedia.org/ (Links to an external site.) web URL
driver.implicitly_wait(30)
driver.get('https://en.wikipedia.org/wiki/Main_Page')
print(' The wikipedia page is shown')


# 4. Check URL and title are as expected.
if driver.current_url == 'https://en.wikipedia.org/wiki/Main_Page' and driver.title == 'Wikipedia, the free encyclopedia':
    print(f'we are at {driver.current_url} site with the title: {driver.title}')

else :
    print(f' Something is wrong. check the URL and the title')


# 5 In a search field, find Python (programming language) and click on it.
driver.find_element(By.ID, 'searchInput').send_keys('Python')
time.sleep(5)
driver.find_element(By.XPATH, '//span[contains(.,"Python")]').click()
time.sleep(2)


# 6. Check that the title Python (programming language) is displayed.
assert driver.title == 'Python - Wikipedia'
print(f'The new web page with title : {driver.title}  is displayed' )


# 7. Click by the Wikipedia main image (logo) to navigate back to the home page and close the browser.
driver.find_element(By.ID, 'p-logo').click()
time.sleep(2)
print(f'----------------*&*--------------')
print(f' The search was finished at : {datetime.datetime.now()}')
driver.close()
driver.quit()