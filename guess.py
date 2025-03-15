from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get('https://chrysalis.tw/taiwan-map-quiz/changhua')

time.sleep(1)

for i in range(0, 10):
    for i in range(0, 26):
        problem = driver.find_element(By.ID, 'problem').text
        print(problem)

        answer = driver.find_element(By.ID, problem)
        answer.click()

    # time.sleep(2.5)

    restart_btn = driver.find_element(By.ID, "restart")
    restart_btn.click()

time.sleep(4)