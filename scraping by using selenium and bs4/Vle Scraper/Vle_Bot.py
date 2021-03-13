#importing all required modules/libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
from datetime import date
from check import user_info
import sys
import os
import json


#content will download all ppt/pdf and word files
def content(each_file):
            try:
                driver.find_element_by_xpath(f"(//div[@class='course-content']/ul/li[{week+1}]/div[@class='content']/ul/li[@class='activity resource modtype_resource ']/div/div/div/div[@class='activityinstance']/a)[{each_file}]").click()
                sleep(3)
            except:
                print(f"\nDownloadable content of Week-{week} not uploaded yet!\n")

#course will click on each courses
def course(each_sub):  
        driver.find_element_by_xpath(f"(//nav[@aria-label='Site']/ul/li)[{each_sub}]").click()
        sleep(5)
        
#nav_menue will open nav menue if not opened
def nav_menue():
    try:
        if driver.find_element_by_xpath("//button[@aria-expanded='false']") is not None:
            driver.find_element_by_xpath("//button[@aria-controls='nav-drawer']").click()
    except:
        pass
        
#id_pass will pass username and password to login
def id_pass(userinfo):
    username = driver.find_element_by_xpath("//input[@id='username']")
    username.send_keys(userinfo[0])
    password = driver.find_element_by_xpath("//input[@id='password']")
    password.send_keys(userinfo[1])
    driver.find_element_by_xpath("//button[@type='submit']").click()

   
def chrome_driver():
    path = os.path.join(os.getcwd(), f'Downloads\\Week-{week}')
    try:  
        os.makedirs(path)  
    except OSError as error:  
        print(error) 
    download_dir= path
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {
    "download.default_directory": download_dir, #Change default directory for downloads
    "download.prompt_for_download": False, #To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
    })
    return webdriver.Chrome("chromedriver.exe", options=options)

#program starting point
userinfo = user_info(json,os)

print("\n     Schedule")
print(' -------------------')
print("|15-21 feb: Week-01 |\n|22-28 feb: Week-02 |\n|01-07 Mar: Week-03 |\n|08-14 Mar: Week-04 |\n|15-21 Mar: Week-05 |\n|22-28 Mar: Week-06 |\n|29-04 Apr: Week-07 |\n|05-11 Apr: Week-08 |\n|12-18 Apr: Week-09 |\n|19-25 Apr: Week-10 |\n|26-02 May: Week-11 |\n|03-09 May: Week-12 |\n|10-16 May: Week-13 |\n|24-30 May: Week-14 |\n|31-06 Jun: Week-15 |\n|07-13 Jun: Week-16 |\n|14-20 Jun: Week-17 |\n|21-27 Jun: Week-18 |\n|28-04 Jul: Week-19 |")
print(' -------------------\n')

today = date.today()

d2 = today.strftime("%B %d, %Y")
print("\nCurrent Date : ", d2,"\n")

while True:
    try:
        week = int(input("Enter Week no. : "))
        if week > 0 and week<20:
            break
        else:
            print('\nYou Entered wrong week number!\n')
    except ValueError:
        print('\nOnly Numbers are allowed, try again!\n')

driver = chrome_driver()
driver.get('https://ssuet.org/login/')
sleep(3)
id_pass(userinfo)
sleep(3)
nav_menue()
sub = driver.find_elements_by_xpath("//nav[@aria-label='Site']/ul/li")
for each_sub in range(6,len(sub)+1):
    course(each_sub)
    #print(driver.find_element_by_xpath("//div[@class='course-content']//li[2]//span/a").text)
    files = driver.find_elements_by_xpath(f"//div[@class='course-content']/ul/li[{week+1}]/div[@class='content']/ul/li[@class='activity resource modtype_resource ']/div/div/div/div[@class='activityinstance']/a")
    #print(len(files))
    for each_file in range(1,len(files)+1):
        content(each_file)
    nav_menue()
driver.close()