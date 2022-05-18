import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup
from pip import main
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from apscheduler.schedulers.background import BackgroundScheduler
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib3
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import sched




PATH = "/Users/koledavis/Coding/chromedriver 2"
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.nba.com/schedule")
get_source = driver.page_source

# time.sleep(10)
def main():
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Block_blockContainer__2tJ58"))
        )
        date = main.find_elements_by_class_name("ScheduleDay_sdDay__nM9By")
        time_copy = []
        for time in date:
            time_copy.append(time.text)
        # for time in time_copy:
        #     time = datetime.datetime.strptime(time, '%A, %b %d').strftime("%d/%Y")
        # print(time_copy)
        s = sched.scheduler(time.time, time.sleep)
        s.enterabs(datetime(2022, 5, 10, 15, 0, 0, 0).timestamp(), 1, job())
        s.enterabs(datetime(2022, 5, 10, 15, 0, 0, 500000).timestamp(), 1, job())
        s.run()
        game_time = main.find_elements_by_class_name("ScheduleStatusText_base__R5PI0")
        game_copy = []
        for time in game_time:
            game_copy.append(time.text)
        teams = main.find_elements_by_class_name("text-cerulean")
        teams_copy = []
        for team in teams:
            teams_copy.append(team.text)
    finally:
        driver.quit()


schedule_dict = {
    
}
def scheduleDict(date, team, time):
    if date and team and time in schedule_dict:
        pass
    schedule_dict["team"] = team
    schedule_dict["team"]["date"] = date
    schedule_dict["team"]["time"] = time
    
    
def dateClean(date):
    for day in date:
        datetime.datetime.strptime(date, '%a %b %d').strftime("%d/%Y")
    return date

#class = ScheduleDay_sdDay__nM9By
# search = driver.find_elements(by=By.CSS_SELECTOR, value="h4.ScheduleDay_sdDay__nM9By")
# search = driver.find_element_by_class_name("ScheduleDay_sdDay__nM9By")
# search_text = "Friday"



# time.sleep(5)

# driver.quit()
# print(search)
    

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    
    user = "koliosis.bot@gmail.com"
    user1 = "kstevendavis@gmail.com"
    msg['from'] = user
    password = "cgbofymeeievfolt"
    password1 = "vktmbsuisxgxgeky"
    
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    
    
    server.quit()


reminder_list = ["8017252172@vtext.com"]

def job():
    print("I'm working...")
    email_alert("Hey", "Hello World", reminder_list[0])
    

if __name__ == '__main__':
    main()
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    # print(OW_schedule())
    # for member in reminder_list:
    #     email_alert("Hey", "Hello World", member)