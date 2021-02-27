from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import urllib.request
import math

imageToBeDonwloaded = input('What Image you want to download ?\n')
numberOfImages = input('\nHow many images you want to download ?\n')
numberOfImages = int(numberOfImages)

linkPart1 = imageToBeDonwloaded.replace(" ", "-")
linkPart2 = imageToBeDonwloaded.replace(" ", "%20")


numberOfPages = int(numberOfImages / 60)
RestOfImages = numberOfImages - (numberOfPages * 60)

options = webdriver.ChromeOptions() 

options.add_argument("user-data-dir=C:\\Users\\Berchez\\AppData\\Local\\Google\\Chrome\\AutoBot2") #Path to your chrome profile
options.add_argument('--profile-directory=Profile 2')
options.add_argument("start-maximized")
options.add_argument('headless')
driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver.exe", chrome_options=options)

imagemNum = 0

for y in range(1, (numberOfPages + 1)): 
    driver.get(f'https://www.gettyimages.com.br/fotos/{linkPart1}?page={y}&phrase={linkPart2}&sort=mostpopular')
    sleep(10)
    content = driver.find_elements_by_class_name('gallery-asset__thumb')
    for x in range(0, (len(content))):
        imagemNum = imagemNum + 1
        urllib.request.urlretrieve(content[x].get_attribute("src"), f'./imagens/image-{(imagemNum)}.jpg')

driver.get(f'https://www.gettyimages.com.br/fotos/{imageToBeDonwloaded}?page={numberOfPages + 1}&phrase={imageToBeDonwloaded}&sort=mostpopular')
sleep(10)
content = driver.find_elements_by_class_name('gallery-asset__thumb')
for z in range(0, RestOfImages):
    imagemNum = imagemNum + 1
    urllib.request.urlretrieve(content[z].get_attribute("src"), f'./imagens/image-{(imagemNum)}.jpg')

driver.quit()
