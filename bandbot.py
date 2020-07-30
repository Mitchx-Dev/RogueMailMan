# imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import *
from selenium.webdriver.common.by import By
from datetime import datetime
import os
import time
from faker import Faker
fake = Faker()
import random
import sys
from myconfig import *

# chrome options
dir_path = os.path.dirname(os.path.realpath(__file__))
chrome_path = str(dir_path + "/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--lang=en")

if (show_chrome_window == False):
    chrome_options.add_argument('--headless')

chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--ignore-certificate-errors")
experimentalFlags = ['same-site-by-default-cookies@1','cookies-without-same-site-must-be-secure@1']
chromeLocalStatePrefs = { 'browser.enabled_labs_experiments' : experimentalFlags}
chrome_options.add_experimental_option('localState',chromeLocalStatePrefs)
driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
driver.header_overrides = {'SameSite=None': 'Secure',}

url = "https://" + artist + ".bandcamp.com"

print("Running Main")

driver.get(url)

def find_album():
    try:
        album_link = driver.find_element_by_partial_link_text(album)
        album_link.click()
    except Exception:
        pass

def add_to_cart():
    links = len(driver.find_elements_by_xpath("//button[contains(text(), 'Buy Record/Vinyl')]"))

    # Adds Vinyl Items Into Cart
    for i in range(links):
        # finds each button class
        button = driver.find_elements_by_xpath("//button[contains(text(), 'Buy Record/Vinyl')]")[i]
        button.click()
        print("button clicked")

        # finds price
        amount = driver.find_element_by_class_name('nyp-summary-price').text    #Finds Price
        amount = amount[1:]                                                    #Removes Currency Symbol
        print(amount) 

        # sends price to the price input
        price_input = driver.find_element_by_css_selector('#userPrice')
        price_input.send_keys(amount)


        # add item to cart
        driver.find_element_by_xpath('//*[@id="downloadButtons_paypal"]/div/div[4]/button').click() #Add Item To Cart

        # close window
        #driver.find_element_by_class_name('ui-dialog-titlebar-close ui-corner-all').click()
        #time.sleep(0.23)

        print("For Loop Done")

    time.sleep(0.5)

    num_cart_items = len(driver.find_elements_by_class_name('item'))
    print(num_cart_items)

    #verifies cart has items we want
    for i in range(1, num_cart_items + 1):
        cart_item = driver.find_element_by_xpath("//*[@id='item_list']/div[" + str(i) +"]")

        if (cart_item.find_element_by_xpath("//*[contains(text(), " + str(keyword) +")]")):
            print("keyword item in cart")
        else:
            del_btn = cart_item.find_element_by_class_name('delete notSkinnable')
            del_btn.click()
            print("deleted from cart")    

def checkout_shipping_info():
    # fills out shipping info

    # Name
    driver.find_element_by_css_selector('#pgBd > div.content.loading > div.body.shipping-address > div > form > div:nth-child(2) > label > input[type=text]').send_keys(name)
    time.sleep(0.234)
    
    # Country
    selectOption = Select(driver.find_element_by_name('country'))
    option_selected = selectOption.select_by_visible_text(country_shipping)


    # address
    try:
        driver.find_element_by_css_selector('#pgBd > div.content.loading > div.body.shipping-address > div > form > div.address.generic > div:nth-child(1) > label > input[type=text]').send_keys(address)
    except Exception:
        driver.find_element_by_css_selector('#pgBd > div.content.loading > div.body.shipping-address > div > form > div.address.united-states > div.field.address1 > label > input').send_keys(address)

    # state
    try:
        driver.find_element_by_css_selector('#pgBd > div.content.loading > div.body.shipping-address > div > form > div.address.generic > div.field.state > label > input[type=text]').send_keys(state_province_region)
    except Exception:
        driver.find_element_by_xpath("//*[@id='pgBd']/div[1]/div[2]/div/form/div[4]/div[4]/label/select[@name='state']/option[text()="+ state_province_region + "]")
        pass

    # postal code
    try:
        driver.find_element_by_css_selector('#pgBd > div.content.loading > div.body.shipping-address > div > form > div.address.generic > div.zip-code.field > label > input[type=text]').send_keys(postal_code)
    except Exception:
        print("postal code failed")
        pass

    # city
    shipping_city_field = driver.find_element_by_xpath('//*[@id="pgBd"]/div[1]/div[2]/div/form/div[7]/div[3]/label/input')
    shipping_city_field.send_keys(shipping_city)
    
	# shipping continue button
    continue_button = driver.find_element_by_xpath('//*[@id="pgBd"]/div[1]/div[2]/div/form/button')
    continue_button.click()
    
    time.sleep(1)
	
    # review and confirm order continue
    proceed_button = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[1]/div[2]/div[2]/div[3]/button')
    proceed_button.click()
    
    time.sleep(1)

    # Checks out as guest and fills out payment info
    if (checkout_as_guest_paypal == True):
        driver.find_element_by_link_text('Pay with Debit or Credit Card').click()
        time.sleep(2.5)
        # country menu
        time.sleep(2)
        country_field = Select(driver.find_element_by_name('countryName'))
        option_selected = country_field.select_by_visible_text(country_billing)
        
        time.sleep(1.5)
        
        # card number
        card_field = driver.find_element_by_id('cc')
        card_field.send_keys(int(card_no))
        
        time.sleep(0.3)
        # exp date
        exp_field = driver.find_element_by_id('expiry_value')
        exp_field.send_keys(int(exp_date))
        
        time.sleep(0.3)
        # Name
        b_first_name_field = driver.find_element_by_name('firstName')
        b_last_name_field = driver.find_element_by_name('lastName')
        b_first_name_field.clear()
        b_first_name_field.send_keys(billing_first_name)
        b_last_name_field.clear()
        b_last_name_field.send_keys(billing_last_name)
        
        time.sleep(0.3)
        # accept cookies button
        accept_button = driver.find_element_by_id('acceptAllButton')
        accept_button.click()
        
        time.sleep(0.3)
        # phone number
        phone_field = driver.find_element_by_id('telephone')
        phone_field.send_keys(int(phone_no))
        time.sleep(0.3)
        
        # Address
        address_line1 = driver.find_element_by_id('billingLine1')
        address_line2 = driver.find_element_by_id('billingLine2')
        address_line1.clear()
        address_line2.clear()
        address_line1.send_keys(billing_street_address)
        address_line2.send_keys(billing_street_address_2)
        
        time.sleep(0.3)
        
        # City
        billing_city_field = driver.find_element_by_name('billingCity')
        billing_city_field.clear()
        billing_city_field.send_keys('billingCity')
        
        time.sleep(0.3)
        
        # Postal Code
        postal_code_field = driver.find_element_by_name('billingPostalCode')
        postal_code_field.clear()
        postal_code_field.send_keys(billing_postal_code)
        
        time.sleep(0.3)
        
        # State / Province / Region
        try:
            state_field = Select(driver.find_element_by_name('billingState'))
            option_selected = state_field.select_by_visible_text(billing_state_province_district)
        except Exception:
            state_field = driver.find_element_by_id('billingState')
            state_field.clear()
            state_field.send_keys()  
        
        time.sleep(0.3)
        
        # Billing Email
        billing_email_field = driver.find_element_by_id('email')
        billing_email_field.send_keys(billing_email)
        
        time.sleep(0.3)
        
        # csc number
        csc_field = driver.find_element_by_id('cvv')
        csc_field.send_keys(int(cvc_no))
        
        time.sleep(1.5)
        
        # Pay Now Button
        pay_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/main/div/div/div/section/div[1]/div[1]/xo-onboard-payment/div/div/form/div/div/div[4]/button')
        pay_btn.click()
    else:
        # Paypal Login
        paypal_mail_field = driver.find_element_by_id('email')
        paypal_mail_field.send_keys(paypal_email)
        time.sleep(0.5)
        try:
            driver.find_element_by_id('password').send_keys(paypal_password)
        except Exception:
            pass
        time.sleep(0.5)
        driver.find_element_by_id('btnNext').click()
        time.sleep(1.5)
        try:
            driver.find_element_by_id('password').send_keys(paypal_password)
        except Exception:
            pass
        driver.find_element_by_id('btnLogin').click()
        time.sleep(1.5)
        driver.find_elements_by_xpath('//*[@id="challenges"]/div/div[2]/button').click()
        time.sleep(1.5)
        security_code = input("Input 2FA Code: ")
        time.sleep(0.1)
        driver.find_element_by_id(int(security_code))
        driver.find_element_by_id('securityCodeSubmit').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="button"]/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div/div/div/div/section/div[1]/div[1]/form/div[4]/div/input').click()
        #SEND DISCORD WEBHOOK
        
        

find_album()
add_to_cart()

# clicks checkout button
time.sleep(0.5)
driver.find_element_by_id('sidecartCheckout').click()

checkout_shipping_info()