

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

import threading



import signal
import sys


import time


"""
driver_path =("C://Users/18awh/geckodriver.exe")
profile = "C:/Users/18awh/AppData/Roaming/Mozilla/Firefox/Profiles/k52cvmgk.default-release"
driver = webdriver.Firefox(executable_path=driver_path,firefox_profile=profile)
"""

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C://Users/18awh/AppData/Local/Google/Chrome/User Data") #Path to your chrome profile
driver_path=r"C:/Users/18awh/chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

def login(name, pword,x):
    x.get("https://robinhood.com/login")
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    time.sleep(1)

    username.send_keys(name)
    password.send_keys(pword)

    x.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/form/footer/div/button/span").click()
    time.sleep(5)

driverlist={}
values={}
slopes={}
owned={}
bprices={}
waitperiod={}
watchlist=[]
account=10
mn = 7.0
mnname =""
mx = 0.0
mxname = ""
mxchange = 0.0
mxchangename = ""
mntime = datetime.datetime.now()
mxtime= datetime.datetime.now()
mxchangetime = datetime.datetime.now()








def createdrivers():
    global driverlist
    driver.get("https://robinhood.com/lists/custom/5c2212ac-15a8-4d54-b13b-257e49049bbc")
    time.sleep(5)
    price = driver.find_elements_by_class_name("css-1go3qce-Row")
    for n in price:
        info = n.text.splitlines()
        driverlist[info[1]]=webdriver.Chrome(executable_path=driver_path)
        login("andrewwheatley@comcast.net", "Blackerr1!",driverlist[info[1]])
    for p in driverlist:
        driverlist[p].get("https://robinhood.com/crypto/"+str(p))




def buy(name,dict):
    global account
    if account>0 and owned[name]==0:
        price = dict[name][-1]
        bought = 0.50/price
        account=account-0.50
        owned[name]=owned[name]+bought
        bprices[name]=price

        thisdriver = driverlist[name]

        enter = WebDriverWait(thisdriver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "SUec6aNMcmnDnn5Cv2Ruj")))
        enter.send_keys("0.50")
        button = WebDriverWait(thisdriver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                 "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button")))
        button.click()
        button = WebDriverWait(thisdriver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                          "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button")))
        button.click()
        button = WebDriverWait(thisdriver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                 "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div/div/footer/div/button")))
        button.click()

        print("BOUGHT "+name+ " AT "+ str(dict[name][-1]))
        print(owned)
        print(account)
        print(datetime.datetime.now())
        print("")
        
    
    


def sell(name,amount):

    thisdriver = driverlist[name]

    button = WebDriverWait(thisdriver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/header/div/div[1]/div/div[2]/div/h3/span/span")))
    button.click()
    button = WebDriverWait(thisdriver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div[1]/div[1]/label/a")))
    button.click()
    price = WebDriverWait(thisdriver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "SUec6aNMcmnDnn5Cv2Ruj")))
    price.send_keys(amount)
    button = WebDriverWait(thisdriver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button")))
    button.click()
    button = WebDriverWait(thisdriver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/button")))
    button.click()
    button = WebDriverWait(thisdriver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div/div/footer/div/button")))
    button.click()
    
    

def monitor():
    global account
    global values
    global mx 
    global mnname 
    global mn 
    global mxname 
    global mxchange 
    global mxchangename 
    global mntime 
    global mxtime
    global mxchangetime

    price = driver.find_elements_by_class_name("css-1go3qce-Row")
    for n in price:
        info = n.text.splitlines()
        num =(info[2][1:])
        if "," in num:
            num= num.replace(",","")
        num =float(num)
        if(num>mx):
            mx = num
            mxname = info[1]
            mxtime = datetime.datetime.now()

        if(num<mn):
            mn = num
            mnname = info[1]
            mntime = datetime.datetime.now()

        if info[1] not in values:
            values[info[1]]=[num]
        else:
            values[info[1]].append(num)

        if info[1] not in owned:
            owned[info[1]]=0

        if info[1] not in waitperiod:
            waitperiod[info[1]]=0
        

    for v in values:

        if((len(values[v]))>20):
            values[v].pop(0)

        if((len(values[v])>2 and len(values[v])<=20 )):
            length = len(values[v])
            percentchange = (values[v][length-1]-values[v][length-2])/(values[v][length-1])
            
            if (abs(percentchange)>mxchange):
                mxchange = percentchange
                mxchangename = v
                mxchangetime = datetime.datetime.now()

            if v not in slopes:
                slopes[v]=[percentchange]
            else:
                slopes[v].append(percentchange)

            if (len(slopes[v])>21):
                slopes[v].pop(0)
        
            #print(" ")
            #print(v+":")
            #print(values[v])
            #print(slopes[v][0])
            

    for x in slopes:
        if len(slopes[x])>18:
            a=0
            b=15
            while b <(len(slopes[x])-1):
                if slopes[x][b]<0:
                    a=a+1
                    b=b+1
                else:
                    b=b+1
            b=15
            if(slopes[x][-1]<0 and slopes[x][-2]<0 and slopes[x][-3]<0):
                if x not in watchlist:
                    watchlist.append(x)
                #print(watchlist)
                a=0

            if(slopes[x][-1]<0 and slopes[x][-2]<0):
                for x in owned:
                    if(owned[x]>0 and (values[x][-1]>bprices[x]) and waitperiod[x]==0):
                        sell(x,owned[x])
                        account=account + owned[x]*(values[x][-1])
                        owned[x]=0
                        print("SOLD: "+x+" AT "+ str(values[x][-1]))
                        print(account)
                        print(owned)
                        print(datetime.datetime.now())
                        print("")
                    a=0

            if(waitperiod[x]>0):
                waitperiod[x]-=1
            a=0

    for x in slopes:
        if len(slopes[x])>18:
            """
            a=0
            b=15
            while b <(len(slopes[x])-1):
                avg=0
                avg=slopes[x][b]+avg
                if slopes[x][b]>0:
                    a=a+1
                    b=b+1
                else:
                    b=b+1
            avg=avg/(b-15)
            """
            #print(x+" "+str(avg*100))
            #print(datetime.datetime.now())
            #print()
            b=15
            if(slopes[x][-1]>0 and slopes[x][-2]>0):
                if x in watchlist:
                    watchlist.remove(x)
                    buy(x,values)
                    waitperiod[x]=1
                a=0
            a=0
            

        
def openpage():
    driver.get("https://robinhood.com/lists/custom/5c2212ac-15a8-4d54-b13b-257e49049bbc")
    time.sleep(5)


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    for x in owned:
        if owned[x]>0:
            sell(x)
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


def run():
    threading.Timer(4.0,run).start()
    monitor()

login("andrewwheatley@comcast.net","Blackerr1!",driver)
createdrivers()
#openpage()
run()




