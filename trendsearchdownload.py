from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil
from selenium.webdriver.common.keys import Keys
import datetime
import smtplib
#import pyautogui

import threading

import smtplib
from email.mime.text import MIMEText

import signal
import sys
from selenium.common.exceptions import StaleElementReferenceException

import csv

import os
import glob
import time

import mechanize
import http.cookiejar
import json
import requests
#driver_path =("C://Users/18awh/geckodriver.exe")
#profile = "C:/Users/18awh/AppData/Roaming/Mozilla/Firefox/Profiles/k52cvmgk.default-release"
#driver2 = webdriver.Firefox(executable_path=driver_path,firefox_profile=profile)


trenddata={}
br = None

def trendcheck(stockname,drive, num):
    global t
    """
    if os.path.exists("C:/Users/18awh/Downloads/multiTimeline("+str(num)+").csv"):
        os.remove("C:/Users/18awh/Downloads/multiTimeline("+str(num)+").csv")
    """
    try:
        drive.get("https://trends.google.com/trends/explore?date=now 7-d&geo=US&q=" + stockname)
        load = WebDriverWait(drive, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]")))
        load.click()
        #pyautogui.write(str(stockname),0.1)
        #pyautogui.press('enter')

        date = str(datetime.datetime.now())[8:10]
        curhour = str(datetime.datetime.now())[11:13]
        time.sleep(1.5)

        """
        list_of_files = glob.glob('C:/Users/18awh/Downloads/*')  # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)
        """

        with open("C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/Trends/multiTimeline(1).csv",'r') as f:
            rank={}
            counter=0
            reader = csv.reader(f,delimiter=',')
            next(reader)
            for row in reader:
                if any(row):
                    if row[1].isdigit():
                        num = int(row[1])
                        rank[row[0]]=num
                            
            ranklist = sorted(rank.items(), reverse =True , key=lambda x: int(x[1]))
            sortrank={}
            zeros=0
            for elem in ranklist:
                if int(elem[1])<15:
                    zeros+=1
        

            if zeros>(0.85*len(ranklist)):
                if int(ranklist[1][1])<50:
                    t = ranklist[0][0][11:16]
                    hour = t[0:2]
                    
                    if int(hour)>=int(curhour)-6:
                        if int((ranklist[0][0][8:10])) == int(date) and int((ranklist[1][0][8:10])) == int(date):
                            print(stockname)

                else:
                    t = ranklist[0][0][11:16]
                    hour = t[0:2]

                    t2 = ranklist[1][0][11:16]
                    hour2 = t2[0:2]

                    if(int(hour2)==int(hour)+1 or int(hour2)==int(hour)-1 or int(hour2)==int(hour)+2 or int(hour2)==int(hour)-2):
                        if int(hour)>=int(curhour)-6:
                            if int((ranklist[0][0][8:10])) == int(date) and int((ranklist[1][0][8:10])) == int(date):
                                print(stockname)

            try:
                f.close()
                os.remove("C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/Trends/multiTimeline(1).csv")
            except:
                print("oof")
    except:
        pass




#trendcheck("XpresSpa", driver2,1)

def switch(p):
    return (not p)

def downloadfile(stockname,drive, numlist,x):
    try:

        if drive.find_elements_by_id("af-error-container"):
            numlist.append(x)
            drive.quit()
        drive.get("https://trends.google.com/trends/explore?date=now 7-d&geo=US&q=" + stockname)
        load = WebDriverWait(drive, 5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]")))
        load.click()

    except:
        pass

def renamefile():
    lst=os.listdir("C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/Trends/")
    for f in lst:
        file = open("C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/Trends/"+f,'r')
        reader = csv.reader(file, delimiter=',')
        try:
            next(reader)
            next(reader)
            for n in reader:
                name = n[1].split(":",1)[0]
                break
            file.close()
            try:
                shutil.move("C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/Trends/"+f, "C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/Renamed/"+name+".csv")
            except:
                os.remove("C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/Trends/"+f)
        except:
            os.remove("C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/Trends/" + f)
            print("h2")

def check(thelist):
    lst = os.listdir("C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/Renamed")
    rank={}
    date = str(datetime.datetime.now())[8:10]
    curhour = str(datetime.datetime.now())[11:13]
    for f in lst:
        try:
                file = open("C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/Renamed/" + f, 'r')
                reader = csv.reader(file, delimiter=',')
                next(reader)
                next(reader)
                next(reader)
                for row in reader:
                    if row[1]=="<1":
                        num=1
                    else:
                        num = int(row[1])
                    rank[row[0]] = num
                ranklist = sorted(rank.items(), reverse=True, key=lambda x: int(x[1]))
                zeros = 0
                for elem in ranklist:
                    if int(elem[1]) < 15:
                        zeros += 1

                if zeros > (0.85 * len(ranklist)):
                    if int(ranklist[1][1]) < 50:
                        t = ranklist[0][0][11:16]
                        hour = t[0:2]

                        if int(hour) >= int(curhour) - 6:
                            if int((ranklist[0][0][8:10])) == int(date) and int((ranklist[1][0][8:10])) == int(date):
                                thelist.append(f[0:-4])
                                print(thelist)


                    else:
                        t = ranklist[0][0][11:16]
                        hour = t[0:2]

                        t2 = ranklist[1][0][11:16]
                        hour2 = t2[0:2]

                        if (int(hour2) == int(hour) + 1 or int(hour2) == int(hour) - 1 or int(hour2) == int(hour) + 2 or int(
                                hour2) == int(hour) - 2):
                            if int(hour) >= int(curhour) - 6:
                                if int((ranklist[0][0][8:10])) == int(date) and int((ranklist[1][0][8:10])) == int(date):
                                    thelist.append(f[0:-4])
                                    print(thelist)
        except:
            pass
        file.close()
        os.remove("C:/Users/C24Andrew.Wheatley/PycharmProjects/pythonProject/Stock Stuff/Renamed/"+f)

def setup_mechanize():
    global br
    br = mechanize.Browser()
    cj = http.cookiejar.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Chrome')]
    
def downloadfile2(keyword):
    #get token
    global br
    if br is None:
        setup_mechanize()
    
    url = 'https://trends.google.com/trends/api/widgetdata/multiline/csv'
    #time = get_time()
    try:    
        x = br.open('https://trends.google.com/trends/api/explore?hl=en-US&tz=420&req=%7B%22comparisonItem%22:%5B%7B%22keyword%22:%22' + keyword + '%22,%22geo%22:%22US%22,%22time%22:%22now+7-d%22%7D%5D,%22category%22:0,%22property%22:%22%22%7D&tz=420')
    except:
        x = br.open('https://trends.google.com/trends/api/explore?hl=en-US&tz=420&req=%7B%22comparisonItem%22:%5B%7B%22keyword%22:%22' + keyword + '%22,%22geo%22:%22US%22,%22time%22:%22now+7-d%22%7D%5D,%22category%22:0,%22property%22:%22%22%7D&tz=420')
    string = x.read().decode('utf-8')
    token = string[string.index('token')+8:string[string.index('token')+8:].index('\"')+string.index('token')+8]
    time = string[string.index('time')+7:string[string.index('time')+7:].index('\"')+string.index('time')+7]
    time = time.replace('\\\\','\\')
    req = {'time': time, 'resolution': 'HOUR', 'locale': 'en-US', 'comparisonItem': [{'geo': {'country': 'US'}, 'complexKeywordsRestriction': {'keyword': [{'type': 'BROAD', 'value': keyword}]}}], 'requestOptions': {'property': '', 'backend': 'CM', 'category': 0}}
    tz = 420
    
    parameters = {'req': req, 'token':token, 'tz':tz}
    print(parameters)
    r = br.open(mechanize.Request(url, data = parameters, method='GET'))
    
    return r.read().decode('utf-8')
    
#trendcheck("Arbutus Biopharma", driver2, 1)

