
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time


driver_path =("C://Users/18awh/geckodriver.exe")
profile = "C:/Users/18awh/AppData/Roaming/Mozilla/Firefox/Profiles/k52cvmgk.default-release"
driver = webdriver.Firefox(executable_path=driver_path,firefox_profile=profile)




def buy(name,amount):
    driver.get("https://robinhood.com/crypto/"+str(name))
    price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "SUec6aNMcmnDnn5Cv2Ruj")))
    price.send_keys(amount)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button")))
    button.click()
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button")))
    button.click()
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div/div/footer/div/button")))
    button.click()
    


"""
def sell(name):
    driver.get("https://robinhood.com/crypto/"+str(name))
    time.sleep(5)
    
    driver.find_element_by_xpath("/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/header/div/div[1]/div/div[2]/div/h3").click()
    driver.find_element_by_xpath("/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div[1]/div[1]/label/a").click()
    account=driver.find_element_by_xpath("/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/footer")
    quant= account.text.split(" ",1)
    tosell=(quant[0])
    price = driver.find_element_by_xpath("/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div[1]/div[1]/div/input")
    price.send_keys(tosell)
    driver.find_element_by_xpath("/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button").click()
    driver.find_element_by_xpath("/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button").click()
    driver.find_element_by_xpath("/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div[1]/button").click()
    
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

"""


def sell(name,amount):
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/header/div/div[1]/div/div[2]/div/h3/span/span")))
    button.click()
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div[1]/div[1]/label/a")))
    button.click()
    price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "SUec6aNMcmnDnn5Cv2Ruj")))
    price.send_keys(amount)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button")))
    button.click()
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button")))
    button.click()
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div/div/footer/div/button")))
    button.click()


    

driver.get("https://www.google.com/")
start=time.time()
buy("DOGE","0.50")
sell("DOGE","15")
print("--- %s seconds ---" %(time.time()-start))
driver.close()


