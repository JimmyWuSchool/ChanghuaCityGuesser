from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time

link = 'https://www.start-point.net/map_quiz/nihonchizu/'

a = [
    '北海道', 
    '青森', 
    '岩手',
    '宮城',
    '秋田',
    '山形',
    '福島',
    '茨城',
    '栃木',
    '群馬',
    '埼玉',
    '千葉',
    '東京',
    '神奈川',
    '新潟',
    '富山',
    '石川',
    '福井', 
    '山梨',
    '長野',
    '岐阜',
    '静岡',
    '愛知',
    '三重',
    '滋賀',
    '京都',
    '大阪',
    '兵庫',
    '奈良',
    '和歌山',
    '鳥取',
    '島根',
    '岡山',
    '広島',
    '山口',
    '徳島',
    '香川',
    '愛媛',
    '高知',
    '福岡',
    '佐賀',
    '長崎',
    '熊本',
    '大分',
    '宮崎',
    '鹿児島',
    '沖縄'
]

driver = webdriver.Chrome()
driver.get(link)

time.sleep(1)
# time.sleep(1)

# Use JavaScript to set all values at once
script = """
for (let i = 0; i < 47; i++) {
    document.getElementById('ken_' + String(i + 1).padStart(2, '0')).value = arguments[0][i];
}
"""
driver.execute_script(script, a)

b = driver.find_element(By.XPATH, '//*[@id="form1"]/button')
b.click()

# time.sleep(15)
time.sleep(5)
