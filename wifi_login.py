import sys
from time import sleep
from selenium import webdriver

USERNAME = 'your_user_name'
PASSWORD = 'your_password'
URL = '' # url of the login page

def login(username, password):
    usernameField = driver.find_element_by_xpath('//*[@id="ft_un"]')
    usernameField.send_keys(username)

    passwordField = driver.find_element_by_xpath('//*[@id="ft_pd"]')
    passwordField.send_keys(password)

    submitButton = driver.find_element_by_xpath('/html/body/div/div/form/div[3]/input')
    submitButton.click()


op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

try:
    driver.get(URL)
    sleep(2) # wait for the page to load
    login(USERNAME, PASSWORD)
except:
    driver.quit()
    sys.exit(1)
finally:
    driver.quit()