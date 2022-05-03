import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/koledavis/Coding/chromedriver 2"
driver = webdriver.Chrome(PATH)
driver.get("https://www.nba.com/schedule")

time.sleep(10)

#class = ScheduleDay_sdDay__nM9By
search = driver.find_elements_by_class_name("ScheduleDay_sdDay__nM9By")
print(search.text)


time.sleep(5)

driver.quit()
    

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    
    user = "koliosis.bot@gmail.com"
    msg['from'] = user
    password = "cgbofymeeievfolt"
    
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    
    
    server.quit()


reminder_list = ["8017252172@vtext.com"]

    
# if __name__ == '__main__':
    # print(OW_schedule())
    # for member in reminder_list:
    #     email_alert("Hey", "Hello World", member)