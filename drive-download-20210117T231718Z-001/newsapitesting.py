from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from trendsearchdownload import downloadfile
from trendsearchdownload import renamefile
from trendsearchdownload import check
from threading import Thread




import smtplib
fromaddr = '18awheatley@gmail.com'
toaddresses  = ['18awheatley@gmail.com', 'amw8zp@virginia.edu']
username = "18awheatley@gmail.com"
password = "Blackerr1!"
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(username,password)
lst=["hello there","cowabunga"]
s=' '.join(lst)
msg = "\r\n".join([
  "From: 18awheatley@gmail.com",
  'To: 18awheatley@gmail.com, amw8zp@virginia.edu',
  "Subject: Stock Review For The Day",
  "",
  s
  ])
for i in toaddresses:
  server.sendmail(fromaddr, i, msg)
server.quit()