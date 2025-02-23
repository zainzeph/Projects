# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 23:20:30 2024

@author: zakwi
"""

import logging
import sys
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


Date = "2025-02-25"

#Takes user input and puts it in to a list to compare against later
#Date = input("Date of game e.g. 2024-04-27 ")
Range1 = int(input("Select start time range e.g. 08 "))
Range2 = int(input("Select End time range e.g. 17 "))
TimeTennis = list()
AvailibleTime = list()
Booking = False
Logedin = False

while Range1 <= Range2:
    if Range1 < 10: 
        Range3 = "0" + str(Range1)   
        if Range1 == 9:
            TimeTennis.append("Book at " + str(Range3) + ":00 - " + str((Range1 + 1)) + ":00")
        else:
            TimeTennis.append("Book at " + str(Range3) + ":00 - " + "0" + str((Range1 + 1)) + ":00")        
    else:
        TimeTennis.append("Book at " + str(Range1) + ":00 - " + str((Range1 + 1)) + ":00")
    Range1 = Range1 + 1
    
#print(TimeTennis)
    
#Opens booking page
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://clubspark.lta.org.uk/ArchbishopsParkLambethNorth/Booking/BookByDate#?date="+Date + "&role=guest")
driver.implicitly_wait(2)


#Extracts availible times to list
elems = driver.find_elements(By.XPATH, "//span[contains(@class, 'available-booking-slot')]") 
if not elems:
        print ("No availible slots")      
for e in elems:
    AvailibleTime.append(e.get_attribute('innerHTML'))

#print(AvailibleTime)


#Comparing scraped list against users list
same_values = set(TimeTennis) & set(AvailibleTime)
print (same_values)

#Close cookie bar
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/button") .click()

#Pop off the dates one by one and attempt booking until booking confirmed
for i in same_values:
    if Booking == False:
        
        print (str(i))
        
        
        
        time.sleep(2)
        #Selelct time
        
        driver.find_element(By.XPATH, "//a[contains(@class, 'book-interval not-booked')and contains(., '"+ i +"')]") .click()
        time.sleep(2)
        driver.find_element(By.ID, "submit-booking").click()
        time.sleep(2)
        
        #Logs in automaticly on further iterations
        if Logedin == False:
            driver.find_element(By.XPATH, "//button[contains(@class, 'cs-btn primary med fw')]").click()
            time.sleep(1)
            driver.find_element (By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div[2]/div[1]/div/span/div/input").send_keys("")
            driver.find_element (By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/span/lightning-input/lightning-primitive-input-simple/div/div/input").send_keys("")
            driver.find_element (By.XPATH, "//button[contains(@type, 'button') and contains(., 'Log in')]").click()
            Logedin = True

    
        time.sleep(2)
        
        driver.find_element(By.ID, "paynow").click()
        print("Pay")
        time.sleep(2)
        
        
        
        #driver.find_element (By.XPATH, "//input[contains(@class, '/html/body/div[7]/div/div/div/div[1]/form/div[1]/div/div/div[1]/div/input')]").send_keys("1234123412341234")
        #driver.find_element (By.XPATH, "//input[contains(@class, '/html/body/div[7]/div/div/div/div[1]/form/div[2]/div[1]/div/div[1]/div/input')]").send_keys("1124")
        #driver.find_element (By.XPATH, "//input[contains(@class, '/html/body/div[7]/div/div/div/div[1]/form/div[2]/div[2]/div/div[1]/div/input')]").send_keys("911")
        
        driver.find_element (By.XPATH, "//input[contains(@class, '__PrivateStripeElement-input')]").send_keys("1234123412341234")
        driver.find_element (By.XPATH, "//input[contains(@class, '__PrivateStripeElement-input') and not(contains(., 'data-gtm-form-interact-field-id=""0""')) ]").send_keys("1124")
        #driver.find_element (By.XPATH, "//input[contains(@class, '__PrivateStripeElement-input')]").send_keys("911")
        
        #driver.find_element(By.ID, "cs-stripe-elements-submit-button").click()
        
        #DO NOT DELETE
        #confirmation = driver.find_element(By.XPATH, "//h1[contains(@class, 'success')]")
        #if confirmation == "success":
            #Booking = True
        #driver.get("https://clubspark.lta.org.uk/ArchbishopsParkLambethNorth/Booking/BookByDate#?date="+Date + "&role=guest")
        print("Back to start")
        time.sleep(2)
        
        


