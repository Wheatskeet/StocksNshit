
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import cryptocompare
#from Monitor import login
import datetime
import matplotlib.pyplot
import time
import numpy as np

"""
driver_path = (
    "C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/geckodriver-v0.29.0-win64/geckodriver.exe")
profile = "C:/Users/C24Andrew.Wheatley/AppData/Roaming/Mozilla/Firefox/Profiles/1nnutf8b.Profile3"
driver = webdriver.Firefox(executable_path=driver_path,firefox_profile=profile)
"""



def buy(name,amount):
    driver.get("https://robinhood.com/crypto/"+str(name))
    price = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "SUec6aNMcmnDnn5Cv2Ruj")))
    price.send_keys(amount)
    button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button")))
    button.click()
    button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button")))
    button.click()
    button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div[1]/button")))
    button.click()
    button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div/div/footer/div/button")))
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
    button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/header/div/div[1]/div/div[2]")))
    button.click()
    button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div[1]/div[1]/label/a")))
    button.click()
    button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div[1]/div[1]/label/a")))
    button.click()
    price = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "SUec6aNMcmnDnn5Cv2Ruj")))
    price.send_keys(amount)
    button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button")))
    button.click()
    button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button")))
    button.click()
    button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button")))
    button.click()
    button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div/div/footer/div/button")))
    button.click()

    

"""
start=time.time()
buy("LTC","1.50")
sell("LTC","1.40")
print("--- %s seconds ---" %(time.time()-start))
driver.close()
"""


def ema(s, n):
    """
    returns an n period exponential moving average for
    the time series s

    s is a list ordered from oldest (index 0) to most
    recent (index -1)
    n is an integer

    returns a numeric array of the exponential
    moving average
    """

    ema = []
    j = 1

    #get n sma first and calculate the next n period ema
    sma = sum(s[:n]) / n
    multiplier = 2 / float(1 + n)
    ema.append(sma)

    #EMA(current) = ( (Price(current) - EMA(prev) ) x Multiplier) + EMA(prev)
    ema.append(( (s[n] - sma) * multiplier) + sma)

    #now calculate the rest of the values
    for i in s[n+1:]:
        tmp = ( (i - ema[j]) * multiplier) + ema[j]
        j = j + 1
        ema.append(tmp)

    return ema


lst=[]
time=[]
t=datetime.datetime.now().strftime('%H:%M:%S')
j=1000
for i in (cryptocompare.get_historical_price_minute('BTC', 'USD', limit=j, exchange='CCCAGG', toTs=datetime.datetime.now())):
    print(((i['low'])+i["high"])/2)
    if j% 5 == 0:
        lst.append(((i['low'])+i["high"])/2)
        time.append(datetime.datetime.now() - datetime.timedelta(minutes=j))
    j-=1

print(time)
lst2 = []
k=0


e=ema(lst,12)
e1=ema(lst,26)
e2=ema(lst,50)



a=[]
for i in range(len(e2)):
    a.append(e[i] - e2[i])

zero_crossings = np.where(np.diff(np.sign(a)))[0]
for i in zero_crossings:
    print(time[i-(len(time)-len(e2))])

"""
matplotlib.pyplot.plot(time[0:999],e,label = "3")
matplotlib.pyplot.plot(time[0:997],e1,label = "5")
matplotlib.pyplot.plot(time[0:994],e2,label = "8")
matplotlib.pyplot.plot(time,lst,label = "price")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
"""