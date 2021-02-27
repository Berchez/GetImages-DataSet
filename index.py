from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import urllib.request
import math


imageToBeDonwloaded = input('What Image you want to download ?')
numberOfImages = input('How many images you want to download ?')

options = webdriver.ChromeOptions() 

options.add_argument("user-data-dir=C:\\Users\\Berchez\\AppData\\Local\\Google\\Chrome\\AutoBot2") #Path to your chrome profile
options.add_argument('--profile-directory=Profile 2')
options.add_argument("start-maximized")
driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver.exe", chrome_options=options)

imagemNum = 0

for y in range(30, 80):
    driver.get(f'https://www.gettyimages.com.br/fotos/{imageToBeDonwloaded}?page={y}&phrase={imageToBeDonwloaded}&sort=mostpopular')
    sleep(10)
    content = driver.find_elements_by_class_name('gallery-asset__thumb')
    for x in range(1, (len(content) - 1)):
        imagemNum = imagemNum + 1
        #urllib.request.urlretrieve(content[x].get_attribute("src"), f'./image-{(imagemNum)}.jpg')
        #sleep(3)




print(len(content))


# for x in range(0, (len(content) - 1)):
#     print(f'{content[x]}\n')


# urllib.request.urlretrieve({content[0]}, 'image-.jpg')

# for x in range(0, (len(content) - 1)):
#     urllib.request.urlretrieve(content[x], f'./image-{x}.jpg')
#     sleep(15)