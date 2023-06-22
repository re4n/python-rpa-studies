from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
import os

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

## Start Website
driver.get('https://coinmarketcap.com/')


for z in range(10):
    #Date
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    docName = now.strftime("[%H-%M-%S]")

    
    with open('C:/Users/ryanr/OneDrive/Área de Trabalho/Python-RPA/CoinMarket/Logs/' + docName + '.txt', 'w', encoding='utf-8') as file:

## GET Specs
        for x in range(1,11):
            getNameCoin = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{x}]/td[3]/div/a/div/div/p').text
            getPriceCoin = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{x}]/td[4]/div/a/span').text
            get24hrPercent = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{x}]/td[6]/span').text
            get7dPercent = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{x}]/td[7]/span').text

            file.write(f'[TIME: {time}] -- Coin: {getNameCoin} |  C Price: {getPriceCoin} | 24Hr %: {get24hrPercent} | 7D %: {get7dPercent}\n')
    file.close()

    ## timeout
    sleep(60)


