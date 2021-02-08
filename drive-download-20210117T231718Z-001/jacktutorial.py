from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from trendsearchdownload import downloadfile
from trendsearchdownload import renamefile
from trendsearchdownload import check
from threading import Thread
from selenium.webdriver.common.keys import Keys


ticks=[]
for i in open('C:/Users/18awh/Downloads/moreshit.txt'):
    ticks.append(i.strip('\n'))

driver_path =("C://Users/18awh/geckodriver.exe")
profile = "C:/Users/18awh/AppData/Roaming/Mozilla/Firefox/Profiles/k52cvmgk.default-release"
driver = webdriver.Firefox(executable_path=driver_path,firefox_profile=profile)
ticks=sorted(ticks)
f=open('C:/Users/18awh/Downloads/15dollars.txt', 'w')

for i in ticks:
    try:
        driver.get("https://robinhood.com/stocks/"+i)
        name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                             "/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/header/h1")))
        price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                             "/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[1]")))
        volume = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                             "_1OFbcHb21BVF-HUMyM5v7i")))
        tradeable = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"_1z8yT9GFo6Q8b6BYdF8vjw")))

        if float(price.text[1:])<12 and int(volume.text.replace(",",""))>1000 and len(tradeable)>0:
            if "ETF" not in name.text and "Trust" not in name.text and "Bond" not in name.text:
                f.write("%s\n" % name.text)
                print(name.text)
    except:
        print("error at "+ i)