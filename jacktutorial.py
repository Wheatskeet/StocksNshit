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
for i in open('C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/moreshit.txt'):
    ticks.append(i.strip('\n'))

driver_path = (
    "C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/geckodriver-v0.29.0-win64/geckodriver.exe")
profile = "C:/Users/C24Andrew.Wheatley/AppData/Roaming/Mozilla/Firefox/Profiles/1nnutf8b.Profile3"
driver = webdriver.Firefox(executable_path=driver_path,firefox_profile=profile)
ticks=sorted(ticks)
f=open('C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/revised.txt', 'w')

for i in ticks:
    try:
        driver.get("https://robinhood.com/stocks/"+i)
        name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                             "Jo5RGrWjFiX_iyW3gMLsy")))

        price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                             "/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[1]")))

        volume = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                             "/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[2]/div[2]/div[8]/div[2]")))

        tradeable = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[2]/div/div[1]/form/div[2]/div/div[2]")))
        if "K" in volume.text:
            v = float(volume.text[0:-1])*1000

        elif "M" in volume.text:
            v = float(volume.text[0:-1])*1000000

        else:
            v = int(float(volume.text))

        n = name.text.split("\n")[0]
        if int(v)>1000 and len(tradeable)>0:
            if "ETF" not in n and "Trust" not in n and "Bond" not in n:
                f.write("%s\n" % name.text.split("\n")[0])
                print(name.text.split("\n")[0])
    except Exception as e:
        print(e,"error message")

f.close()