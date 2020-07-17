from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
from datetime import datetime
from faker import Faker
fake = Faker()
import random





dir_path = os.path.dirname(os.path.realpath(__file__))
chrome_path = str(dir_path + "/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--lang=en")
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)

driver.get("https://www.mycfavisit.com/Index.aspx")

receipt = input("Receipt Code w/ spaces: ")
useemail = input("Email: ")

cn1 = receipt.split(' ')[0]
cn2 = receipt.split(' ')[1]
cn4 = "0523"
cn5 = "96"

with open("CodeNumbers.txt", "r") as f:
    lines = f.read().split('\n')

introlist = ["0001", "0002", "0003", "0004", "0005", "0006", "0007", "0008", "0009"]
for number in introlist:
    url = 'https://www.mycfavisit.com/Index.aspx?c=583214&AllowCapture=&CN1=' + cn1 + '&CN2=' + cn2 + '&CN3=' + number + '&CN4=' + cn4 + '&CN5=' + cn5
    driver.get(url)

    if 'Block' in driver.current_url:
        print(driver.current_url)
        driver.quit()
        driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
        driver.get(url)
        
    driver.find_element_by_name("NextButton").click()
    if 'we are unable to' in driver.page_source:
        print("Failed with: " + number)
    else:
        print("Success with: " + number)
        for line in lines:
            if line == number:
                ind = lines.index(line)
                break
        while True:
            ind = ind + 1
            num = lines[ind]
            if len(num) < 3:
                break
            if 'hange' in num:
                pass

            url = 'https://www.mycfavisit.com/Index.aspx?c=583214&AllowCapture=&CN1=' + cn1 + '&CN2=' + cn2 + '&CN3=' + num + '&CN4=' + cn4 + '&CN5=' + cn5
            driver.get(url)

            if 'Block' in driver.current_url:
                print(driver.current_url)
                driver.quit()
                driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
                driver.get(url)

            driver.find_element_by_name("NextButton").click()
            if 'we are unable to' in driver.page_source:
                print("Failed with: " + num)
            else:
                print("Success with: " + num)

                try:
                    for x in range(1):
                        x = x+1
                        idname = driver.page_source.split('<tr id="')[x].split('"')[0]
                        xpath = '//*[@id="' + idname + '"]/td[6]/span'
                        driver.find_element_by_xpath(xpath).click()
                        
                    driver.find_element_by_id("NextButton").click()

                    for x in range(4):
                        x = x+1
                        idname = driver.page_source.split('<tr id="')[x].split('"')[0]
                        xpath = '//*[@id="' + idname + '"]/td[6]/span'
                        driver.find_element_by_xpath(xpath).click()
                        
                    driver.find_element_by_id("NextButton").click()

                    for x in range(4):
                        x = x+1
                        idname = driver.page_source.split('<tr id="')[x].split('"')[0]
                        xpath = '//*[@id="' + idname + '"]/td[6]/span'
                        driver.find_element_by_xpath(xpath).click()

                    driver.find_element_by_id("NextButton").click()

                    for x in range(2):
                        x = x+1
                        idname = driver.page_source.split('<tr id="')[x].split('"')[0]
                        xpath = '//*[@id="' + idname + '"]/td[6]/span'
                        driver.find_element_by_xpath(xpath).click()

                    driver.find_element_by_id("NextButton").click()

                    for x in range(1):
                        x = x+1
                        idname = driver.page_source.split('<tr id="')[x].split('"')[0]
                        xpath = '//*[@id="' + idname + '"]/td[3]/span'
                        driver.find_element_by_xpath(xpath).click()

                    driver.find_element_by_id("NextButton").click()

                    responses = [
                        'I love my local chick fil a. ',
                        'the fries are so good. ',
                        'i enjoyed the time there, very clean. ',
                        'I wish you guys opened up on sundays. ',
                        'My daughter loves your guys breakfast. ',
                        'A friend of mines daughter also just got hired by you guys, so i come frequently. ',
                        'the chocolate shakes are the best. ',
                        'Appreciate the help, they did forget a fry but they came with an extra one at the end. ',
                        'very tasty chicken sandwich. ',
                        ]

                    randomMessage = random.sample(responses, 3)
                    randomMessage = randomMessage[0] + randomMessage[1] + randomMessage[2]
                    idname = driver.page_source.split('inputtypetxt" id="')[1].split('"')[0]
                    xpath = '//*[@id="' + idname + '"]"'
                    driver.find_element_by_name(idname.replace("FNS", "")).send_keys(randomMessage)

                    driver.find_element_by_id("NextButton").click()

                    idname = driver.page_source.split('inputtyperblv" id="')[1].split('"')[0]
                    xpath = '//*[@id="' + idname + '"]/div[2]/div/div[1]/span/span'
                    driver.find_element_by_xpath(xpath).click()

                    driver.find_element_by_id("NextButton").click()

                    for x in range(1):
                        x = x+1
                        idname = driver.page_source.split('<tr id="')[x].split('"')[0]
                        xpath = '//*[@id="' + idname + '"]/td[6]/span'
                        driver.find_element_by_xpath(xpath).click()

                    driver.find_element_by_id("NextButton").click()

                    responses = [
                        'The people are so nice. ',
                        'you guys gave me an extra fry. ',
                        'you guys clean up well. ',
                        'and you never fail to say my please. ',
                        'always good service. ',
                        'A friend of mines daughter also just got hired by you guys, so i come frequently. ',
                        'i come to chick fila for the service. ',
                        'Appreciate the help, they did forget a fry but they came with an extra one at the end. ',
                        'you guys always attempt to make the best of a situation. ',
                        ]

                    randomMessage = random.sample(responses, 3)
                    randomMessage = randomMessage[0] + randomMessage[1] + randomMessage[2]
                    idname = driver.page_source.split('inputtypetxt" id="')[1].split('"')[0]
                    xpath = '//*[@id="' + idname + '"]"'
                    driver.find_element_by_name(idname.replace("FNS", "")).send_keys(randomMessage)

                    driver.find_element_by_id("NextButton").click()

                    for x in range(4):
                        x = x+1
                        idname = driver.page_source.split('<tr id="')[x].split('"')[0]
                        xpath = '//*[@id="' + idname + '"]/td[2]/span'
                        driver.find_element_by_xpath(xpath).click()

                    driver.find_element_by_id("NextButton").click()

                    for x in range(2):
                        x = x+1
                        idname = driver.page_source.split('<tr id="')[x].split('"')[0]
                        xpath = '//*[@id="' + idname + '"]/td[6]/span'
                        driver.find_element_by_xpath(xpath).click()

                    driver.find_element_by_id("NextButton").click()

                    for x in range(2):
                        x = x+1
                        idname = driver.page_source.split('<select id="')[x].split('"')[0]
                        select = Select(driver.find_element_by_id(idname))
                        select.select_by_value('4')

                    driver.find_element_by_id("NextButton").click()

                    for x in range(1):
                        x = x+1
                        idname = driver.page_source.split('<tr id="')[x].split('"')[0]
                        xpath = '//*[@id="' + idname + '"]/td[3]/span'
                        driver.find_element_by_xpath(xpath).click()

                    driver.find_element_by_id("NextButton").click()

                    for x in range(1):
                        x = x+1
                        idname = driver.page_source.split('<tr id="')[x].split('"')[0]
                        xpath = '//*[@id="' + idname + '"]/td[3]/span'
                        driver.find_element_by_xpath(xpath).click()

                    driver.find_element_by_id("NextButton").click()

                    emailnum = str(random.randint(1111111, 999999999))
                    email = useemail.split('@')[0] + '+' + emailnum + '@' + useemail.split('@')[1]

                    for x in range(4):
                        x = x+1
                        idname = driver.page_source.split('type="text" name="')[x].split('"')[0]
                        if x == 1:
                            message = fake.name().split(' ')[0]
                        elif x == 2:
                            message = fake.name().split(' ')[0]
                        elif x == 3:
                            message = email
                        elif x == 4:
                            message = email
                        else:
                            message = "this cant happen"
                            
                        
                        driver.find_element_by_name(idname).send_keys(message)

                    driver.find_element_by_id("NextButton").click()
                    print("Submitted survey!")
                except:
                    print("Error completing survey, please help complete this one and press ENTER when finished with survey: ")
                
            