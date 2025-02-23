# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 11:56:55 2021

@author: zwilliams
"""


from datetime import datetime
import csv
from time import sleep
import krakenex
from pykrakenapi import KrakenAPI
api = krakenex.API()
kraken = KrakenAPI(api)

data = kraken.get_asset_info()
data


with open('RecordData.csv', mode='w', newline='') as RecordData:
    employee_writer = csv.writer(RecordData, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['Date', 'Price',])



while True:
    
        BTC_old = float((kraken.get_ticker_information('ETHGBP'))['b'][0][0])
        print(BTC_old)
        
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)
        
        with open('RecordData.csv', mode='a', newline='') as RecordData:
            employee_writer = csv.writer(RecordData, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow([dt_string, BTC_old,])
           
        sleep(60)
        
        
