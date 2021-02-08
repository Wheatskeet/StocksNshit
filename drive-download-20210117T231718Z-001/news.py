from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from trendsearchdownload import downloadfile
from trendsearchdownload import renamefile
from trendsearchdownload import check
from threading import Thread





def newssearch(name, driver,lst):
    try:
        driver.get("https://news.google.com/search?q="+name)
        article = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,"/html/body/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]")))
        n=article.text.splitlines()
        x=0
        while x < len(n):
            if "minute" in n[x] or "1 hour" or "2 hours" or "3 hours" in n[x]:
                lst.append(name)
                #print(name)
                break
            x=x+1
    except:
        driver.refresh()
        pass


def newssearch2(name, driver,lst):
    try:
        driver.get("https://www.google.com/search?q="+name+"&source=lnms&tbm=nws")
        articles = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"WG9SHc")))
        for n in articles:
            if ("minute" in n.text or "1 hour" in n.text or "2 hours" in n.text):
                lst.append(name)
                break
    except:
        driver.refresh()
        pass







with open('C:/Users/18awh/Downloads/we-out-here.txt') as f:
    content = f.readlines()


k1 =True
k2 = True
k3 = True

def func1():
    global k1
    lst1=[]
    driver_path = ("C://Users/18awh/geckodriver.exe")
    profile = "C:/Users/18awh/AppData/Roaming/Mozilla/Firefox/Profiles/k52cvmgk.default-release"
    driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile)
    x=0
    while x < len(content):
        if k1 == True:
            name = content[x].strip("\n")
            newssearch2(name,driver,lst1)
            x=x+3
            if x>=len(content):
                for i in lst1:
                    downloadfile(i,driver)
                lst1=[]
                x=0
                k1 = False


def func2():
    global k2
    lst2=[]
    driver_path = ("C://Users/18awh/geckodriver.exe")
    profile = "C:/Users/18awh/AppData/Roaming/Mozilla/Firefox/Profiles/k52cvmgk.default-release"
    driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile)
    x=1
    while x < len(content):
        if k2 == True:
            name = content[x].strip("\n")
            newssearch2(name,driver,lst2)
            x=x+3
            if x>=len(content):
                for i in lst2:
                    downloadfile(i,driver)
                lst1=[]
                x=1
                k2 = False


def func3():
    global k3
    lst3=[]
    driver_path = ("C://Users/18awh/geckodriver.exe")
    profile = "C:/Users/18awh/AppData/Roaming/Mozilla/Firefox/Profiles/k52cvmgk.default-release"
    driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile)
    x=2
    while x < len(content):
        if k3 == True:
            name = content[x].strip("\n")
            newssearch2(name,driver,lst3)
            x=x+3
            if x>=len(content):
                for i in lst3:
                    downloadfile(i,driver)
                lst3=[]
                x=2
                k3 = False


key = True


def func4():
    global k1
    global k2
    global k3
    global key
    if k1 == False and key == True:
        print("made it here 1")
        key = False
        renamefile()
        check()
        k1 = True
        key = True
    if k2 == False and key == True:
        print("made it here 2")
        key = False
        renamefile()
        check()
        k2 = True
        key = True
    if k3 == False and key == True:
        print("made it here 3")
        key = False
        renamefile()
        check()
        k3 = True
        key = True



if __name__=='__main__':
    #start_time = time.time()
    Thread(target=func1).start()
    Thread(target=func2).start()
    Thread(target=func3).start()
    Thread(target=func4).start()



