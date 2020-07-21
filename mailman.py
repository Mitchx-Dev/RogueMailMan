"""

            Author: Mitch
            Made for: Mitch
            Date:   7/19/2020
            Version: 1.0
            Tested w/ Python3.7.8

"""

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
import sys
from colorama import *
from termcolor import colored
init()

#Chrome Options
dir_path = os.path.dirname(os.path.realpath(__file__))
chrome_path = str(dir_path + "/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--lang=en")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--ignore-certificate-errors")



experimentalFlags = ['same-site-by-default-cookies@1','cookies-without-same-site-must-be-secure@1']
chromeLocalStatePrefs = { 'browser.enabled_labs_experiments' : experimentalFlags}
chrome_options.add_experimental_option('localState',chromeLocalStatePrefs)
driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
driver.header_overrides = {'SameSite=None': 'Secure',}



print(Fore.CYAN + Style.BRIGHT + """\n\n\n\n\n\n\n\n\n\n\n\n
 ____   ____   ____   _  _   ___          _   _    _     ___   _      _   _    _    _  _  
/  _ \ / __ \ ).-._( ) () ( ) __(        ) \_/ (  )_\   )_ _( ) |    ) \_/ (  )_\  ) \/ ( 
)  ' / ))__(( |( ,-. | \/ | | _)         |  _  | /( )\  _| |_ | (__  |  _  | /( )\ |  \ | 
|_()_\ \____/ )_`__( )____( )___(  _____ )_( )_()_/ \_()_____()____( )_( )_()_/ \_()_()_( 
                                  )_____(                                                 
                                                        created by Mitch :)\n\n\n


""")



#Input Variables
email = input("Please Enter Email To Bomb: ")
fname = input("First Name To Use (press enter for random): ")
lname = input("Last Name to Use (press enter for random): ")

#driver.get("https://www.google.com")  #browser init
driver.implicitly_wait(1)

#generates fake user if left blank
if (fname == ""):
    fullname = fake.name()
    a = fullname.split()
    fname = a[0]
if (lname == ""):
    fullname = fake.name()
    a = fullname.split()
    lname = a[1]
print(Fore.WHITE + Style.BRIGHT + "Email : " + email + "\nName : " + fname + lname + "\n")
#print("Email: ", email, "\nName = ",fname, " ",lname )
print("Loading Modules")




#test Module
def testmodule():  
    try:   #working
        url = 'http://www.donaldjtrump.com/media'
        driver.get(url)
        print(Fore.YELLOW + "testmodule starting" + Fore.WHITE)
        driver.find_element_by_xpath("/html/body/footer/div/div[1]/div[1]/div/form/input[1]").send_keys(email)
        driver.find_element_by_xpath('/html/body/footer/div/div[1]/div[1]/div/form/input[2]').send_keys(fake.postcode())
        driver.find_element_by_xpath('/html/body/footer/div/div[1]/div[1]/div/form/input[3]').click()
        print(Fore.GREEN + "testmodule succeeded")
        #driver.close()
    except Exception:
        pass
        print(Fore.RED + "Module Failed - Contact Mitch")

#theskimm module            in-progress
def theskimm():
    try:
        url = 'https://www.theskimm.com/daily-skimm'
        print(Fore.YELLOW + "Starting theskimm module" + Fore.WHITE)
        driver.get(url)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/form/label/input').send_keys(email)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/form/button').click()
        print(Fore.GREEN + "Module 'theskimm' success")
        #driver.close()
    except Exception:
        pass
        print(Fore.RED + "Module Failed - Contact Mitch")

#cambridge_history module   in-progress
def cambridge_history():
    try:
        url = 'https://cambridgehistory.org/about/newsletters/'
        print(Fore.YELLOW + "Starting Cambridge_History Module" + Fore.WHITE)
        driver.get(url)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/aside/div[1]/div/div/form/p[1]/input').send_keys(email)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/aside/div[1]/div/div/form/p[5]/input').click()
        #driver.close()
        print(Fore.GREEN + "cambridge_history module success")
    except Exception:
        pass
        print(Fore.RED + "Module Failed - Contact Mitch")

#smithsonian_hist module        in progres
def smithsonian_hist():
    try:
        url = 'https://www.smithsonianmag.com/category/today-in-history/'
        print(Fore.YELLOW + "tarting smithsonian module." + Fore.WHITE)
        driver.get(url)
        driver.find_element_by_xpath('/html/body/div[15]/div[1]/div/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/div/input[2]').send_keys(email)
        driver.find_element_by_xpath('/html/body/div[15]/div[1]/div/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/div/button').click()
        #time.sleep(0.23923)
        driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/form/fieldset/div/input').send_keys(email)
        #driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/form/p[2]/button').click()
        #driver.close()
        print(Fore.GREEN + "Module Smithsonian Success")
    except Exception:
        pass
        print(Fore.RED + "Module Failed - Contact Mitch")


def hnnet():                #In-Progress
    try:
        url = 'https://historynewsnetwork.org/newsletter.html'
        print(Fore.YELLOW + "Starting hnnnet module" + Fore.WHITE)
        driver.get(url)
        driver.find_element_by_xpath('/html/body/section/header/div/nav/div/form/div[1]/input[1]').send_keys(email)
        driver.find_element_by_xpath('/html/body/section/header/div/nav/div/form/div[1]/input[2]').click()
        time.sleep(0.239)
        #driver.dispose()
        print(Fore.GREEN + "Module hnnet success")
        #driver.close()
    except Exception:
        pass
        print(Fore.RED + "Module Failed - Contact Mitch")

def mailbait(): #in progress
    try:
        url = 'http://mailbait.info/run.html'
        print(Fore.YELLOW + "Starting Mailbait Module" + Fore.WHITE)
        driver.get(url)
        time.sleep(1)
        #print(Fore.CYAN + "Mailbait Module Working...")
        driver.find_element_by_xpath('/html/body/div/section[2]/div[2]/input').send_keys(email)
        driver.find_element_by_xpath('/html/body/div/section[2]/div[2]/div[1]/input').click()
        driver.find_element_by_xpath("/html/body/div/section[2]/div[2]/div[2]/select[@name='speed']/option[text()='60 per minute']")
        print(Fore.MAGENTA + "Generating Emails... This script will stay on for 5 minutes and then exit.")
        time.sleep(300)
        #driver.close()
        print(Fore.GREEN + "Finished mailbait module")
    except Exception:
        pass
        print(Fore.RED + "Module Failed - Contact Mitch")

def rvrepairclub():      #test
    try:
        url = 'https://go.rvrepairclub.com/a14585/?gclid=Cj0KCQjw3s_4BRDPARIsAJsyoLOcXWq-HUbUcZa1dEFvE0DdX9j7QdfVhfofNX7eRRHgnhES-SWNYKEaAjXLEALw_wcB'
        print(Fore.YELLOW + "rvrepairclub module starting" + Fore.WHITE)
        driver.get(url)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[9]/div[3]/form/div/div/input").send_keys(email)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[9]/div[3]/form/button").click()
        #driver.close()
        print(fore.GREEN + "finished rvrepairclub module")
    except Exception:
        pass
        print(Fore.RED + "Module Failed - Contact Mitch")


def crosswalk():
    try:
        print(Fore.YELLOW + "crosswalk module starting" + Fore.WHITE)
        driver.get('https://www.crosswalk.com/newsletters/')
        #driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[1]/input[2]").send_keys(email)

        #crosswalk
        for i in range(2, 18, 1):
            driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[1]/div[" + str(i) +"]/input").click()

        #Family
        for i in range(2, 20,1):
            driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[2]/div[" + str(i) + "]/input").click()
        
    #single
        driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[3]/div[2]/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[3]/div[3]/input").click()
    
    #News and Community
        driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[4]/div[2]/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[4]/div[3]/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[4]/div[4]/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[4]/div[5]/input").click()

    #International
        driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[5]/div[2]/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[5]/div[3]/input").click()

    #Entertainment
        driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[6]/div[2]/input").click()

    #Lifestyle
        for i in range(2, 6,1):
            driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[7]/div[" + str(i) +"]/input").click()

    #Work
        for i in range(2, 4,1):
            driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[8]/div[" + str(i) +"]/input").click()        

    #Newsletters from out partner sites
        for i in range(2, 6,1):
            driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[9]/div[" + str(i) + "]/input").click()

    #Weekly Devotions
        for i in range(2, 14,1):
            driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[10]/div[" + str(i) + "]/input").click()

    #worldview and culture
        for i in range(2, 4,1):
            driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[11]/div[" + str(i) + "]/input").click()

    #Devotions for Spiritual Growth
        for i in range(2, 8,1):
            driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[12]/div[" + str(i) + "]/input").click()
    
    #For Pastors
        for i in range(2, 6,1):
            driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[2]/div[1]/div[" + str(i) + "]/input").click()
    
    #For Women
        for i in range(2, 17,1):
            driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[2]/div[2]/div[" + str(i) + "]/input").click()

    #For Men
        for i in range(2, 6,1):
            driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[2]/div[3]/div[" + str(i) + "]/input").click()

    #Espanola
        for i in range(2, 15,1):
            driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[2]/div[4]/div[" + str(i) + "]").click()

    #Daily Devotions
        for i in range(2, 59,1):
            driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[2]/div[5]/div[59]/input").click()

        print(Fore.GREEN + "Module 'crosswalk' success")
         
    except Exception:
        pass
        print(Fore.RED + "Module Failed - Contact Mitch")


    driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[7]/input[2]").send_keys(email)
    driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[7]/a").click()
testmodule()            #working
theskimm()              #working
cambridge_history()     #working
#smithsonian_hist()      #Fail
hnnet()                 #Success
#rvrepairclub()          #Fail
#mailbait()              #Fail
crosswalk()             #working

driver.quit()
print(Fore.GREEN + """

        Rogue_Mailman Finished
        Email Will not be sent instantly, but over-time.add()


        coded by: Mitch for HF
        Github: https://github.com/Mitchx-Dev
                
""")
