
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import collections
from trendsearchdownload import trendcheck
from trendsearchdownload import check
from trendsearchdownload import downloadfile
from trendsearchdownload import renamefile
from threading import Thread
from datetime import datetime, timedelta
from threading import Timer

from multiprocessing import Process
import sys
import os
import schedule
import smtplib
from shutil import copyfile



#driver_path =("C://Users/18awh/geckodriver.exe")
#rofile = "C:/Users/18awh/AppData/Roaming/Mozilla/Firefox/Profiles/k52cvmgk.default-release"
#driver1 = webdriver.Firefox(executable_path=driver_path,firefox_profile=profile)




"""
with open('C:/Users/User/Downloads/goodprice.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 


data = [i.strip('\n').split('\t') for i in open('C:/Users/User/Downloads/allnames.txt')]
f=open('C:/Users/User/Downloads/finalshit.txt', 'w')

for x in data:
    if x[0] in content:
        f.write("%s\n" % x[1])
        print(x[1])
"""












"""
data = [i.strip('\n').split('\t') for i in open("C:/Users/User/Downloads/allnames.txt")]
f=open('C:/Users/User/Downloads/we-out-here.txt', 'w')

x=5
while x < len(data):
    try:
        driver.get("https://robinhood.com/stocks/"+str(data[x][0]))
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[2]/div/div[1]/form/div[2]/div/div[1]")))
        name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/header/h1")))
        price = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[1]")))
        if float(price.text[1:])<5:
            print(name.text)
            f.write("%s\n" % name.text)
    except:
        #print(data[x][0]+ ' bad')
        pass
    x=x+1
"""

thelist = []
numlist=[]
startnum=0
redo1 =False
redo2 =False
redo3 =False
zero1 = False
zero2 = False
zero3 = False
def func1():
    global key
    global startnum
    global redo1
    global zero1
    driver_path = ("C://Users/18awh/geckodriver.exe")
    profile = "C:/Users/18awh/AppData/Roaming/Mozilla/Firefox/Profiles/k52cvmgk.default-release"
    driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile)
    with open('C:/Users/18awh/Downloads/we-out-here.txt') as f:
        content = f.readlines()
    x=startnum
    while x < len(content):
        if redo1 == True:
            driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile)
            redo1=False

        if key == True:
            downloadfile(content[x], driver, numlist, x)
            x = x + 3

            if x>=len(content):
                zero1=True
                driver.quit()
        else:
            time.sleep(30)



def func2():
    global key
    global redo2
    global zero2
    driver_path = ("C://Users/18awh/geckodriver.exe")
    profile = "C:/Users/18awh/AppData/Roaming/Mozilla/Firefox/Profiles/kgc1b13i.profile2"
    driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile)
    with open('C:/Users/18awh/Downloads/we-out-here.txt') as f:
        content = f.readlines()
    x=startnum+1
    while x < len(content):
        if redo2 == True:
            driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile)
            redo2 = False
        if key == True:
            downloadfile(content[x], driver, numlist, x)
            x = x + 3

            if x>=len(content):
                zero2=True
                driver.quit()
        else:
            time.sleep(30)

def func3():
    global key
    global redo3
    global zero3
    driver_path = ("C://Users/18awh/geckodriver.exe")
    profile = "C:/Users/18awh/AppData/Roaming/Mozilla/Firefox/Profiles/9mw41wzh.profile3"
    driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile)
    with open('C:/Users/18awh/Downloads/we-out-here.txt') as f:
        content = f.readlines()
    x=startnum+2
    while x < len(content):
        if redo3 == True:
            driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile)
            redo3 = False
        if key == True:
            downloadfile(content[x], driver, numlist, x)
            x = x + 3
            if x>=len(content):
                zero3=True
                driver.quit()
        else:
            time.sleep(10)


"""
def func4():
    global key
    driver_path = ("C://Users/18awh/geckodriver.exe")
    profile = "C:/Users/18awh/AppData/Roaming/Mozilla/Firefox/Profiles/k52cvmgk.default-release"
    driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile)
    with open('C:/Users/18awh/Downloads/we-out-here.txt') as f:
        content = f.readlines()
    x=startnum+3
    while x < len(content):
        if key == True:
            if p == True:
                driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile)
                p = False
            downloadfile(content[x], driver, numlist, x, p)
            x = x + 3
            if p == True:
                driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile)
                p = False
        else:
            time.sleep(30)

def func5():
    global key
    driver_path = ("C://Users/18awh/geckodriver.exe")
    profile = "C:/Users/18awh/AppData/Roaming/Mozilla/Firefox/Profiles/k52cvmgk.default-release"
    driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile)
    with open('C:/Users/18awh/Downloads/we-out-here.txt') as f:
        content = f.readlines()
    x=startnum+4
    while x < len(content):
        if key == True:
            downloadfile(content[x],driver,thelist)
            x = x + 5
        else:
            time.sleep(30)
"""


timer = True
def func6():
    global key
    global thelist
    global numlist
    global startnum
    global weeklylist
    global redo1
    global redo2
    global redo3
    global timer
    global zero1
    global zero2
    global zero3
    while True:
        time.sleep(20)
        key = False
        if len(numlist)>=3:
            startnum = min(numlist)-6
            numlist=[]
            pause=False

            checks = []
            for i in open('C:/Users/18awh/Downloads/weeklylist.txt'):
                checks.append(i.strip('\n'))
            for g in thelist:
                if g in checks:
                    thelist.remove(g)
            fromaddr = '18awheatley@gmail.com'
            #,'michaelwheatley@comcast.net','zmullins97@gmail.com'
            toaddresses = ['18awheatley@gmail.com']
            username = "18awheatley@gmail.com"
            password = "Blackerr1!"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(username, password)
            s = '\n '.join(thelist)
            msg = "\r\n".join([
                "From: 18awheatley@gmail.com",
                'To: 18awheatley@gmail.com',
                "Subject: Stock Review For The Day",
                "",
                s
            ])

            joinedlist = checks + thelist
            f = open('C:/Users/18awh/Downloads/templist.txt', 'w')
            for i in joinedlist:
                f.write("%s\n" % i)
            copyfile('C:/Users/18awh/Downloads/templist.txt','C:/Users/18awh/Downloads/weeklylist.txt')

            for i in toaddresses:
                server.sendmail(fromaddr, i, msg)
            server.quit()
            if zero1 == True and zero2 == True and zero3 == True:
                print("all done for today")
                time.sleep(5400)
                startnum=0
                pause = True
                redo1 = True
                redo2 = True
                redo3 = True
            #print("Switch google accounts, then type s to start again: ")
            if pause==False:
                time.sleep(5400)
                pause=True
                redo1=True
                redo2=True
                redo3=True


        try:
            renamefile()
            check(thelist)
        except:
            print("error message")
        key = True


key = True

def run():
    #start_time = time.time()
    Thread(target=func1).start()
    Thread(target=func2).start()
    Thread(target=func3).start()
    #Thread(target=func4).start()
    Thread(target=func6).start()


with open('C:/Users/18awh/Downloads/we-out-here.txt') as f:
    content = f.readlines()

"""
y=946
while y <len(content):
    trendcheck(content[y],drive1,1)
    y=y+1
"""

"""
x=datetime.today()
y = x.replace(day=x.day, hour=5, minute=30, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x

secs=delta_t.total_seconds()

t = Timer(secs, run)
t.start()
"""
run()


"""
schedule.every(6).hours.do(run)
while True:
    schedule.run_pending()
    time.sleep(1)
"""















#OPEN FIVE PAGES, DOWNLOAD FIVE FILES, OPEN FIVE NEW PAGES WHILE READING THOSE FILES





