from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time

profile =("C:/Users/18awh/AppData/Roaming/Mozilla/Firefox/Profiles/k52cvmgk.default-release")
driver_path = 'C://Users/18awh/geckodriver.exe'
driver = webdriver.Firefox(executable_path=driver_path,firefox_profile=profile)

def login(name, pword):
    driver.get("https://robinhood.com/login")
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    time.sleep(1)

    username.send_keys(name)
    password.send_keys(pword)

    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/form/footer/div/button/span").click()
    time.sleep(5)


def monitor():
    driver.get("https://robinhood.com/lists/custom/3cb74356-f1a8-47bb-9910-0bdd206ca7ea")
    time.sleep(5)
    price = driver.find_elements_by_class_name("css-1go3qce-Row")
    for n in price:
        print(n)

monitor()

"""
rh-hyperlink _2uFNhgQu5JhaCtiNU8posI _2fax8HRY62uCbHnshxhsBl
rh-hyperlink _2uFNhgQu5JhaCtiNU8posI _2fax8HRY62uCbHnshxhsBl
rh-hyperlink _2uFNhgQu5JhaCtiNU8posI _2fax8HRY62uCbHnshxhsBl
"""