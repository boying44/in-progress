from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

board = "https://www.pinterest.com/1374552818qq/fashion/"
pin_builder = "https://www.pinterest.com/pin-builder/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=chrome_options)
upload_folder = r"C:\Users\Boying\Desktop\looks\\"
cookie_file = r"C:\Users\Boying\Desktop\cookies.pkl"

def get_session():
    driver.get(board)
    driver.find_element_by_xpath("//*[@id='HeaderContent']/div/div[1]/div/div/div[2]").click() #login
    driver.find_element_by_id("email").send_keys("1374552818qq@gmail.com")
    driver.find_element_by_id ("password").send_keys("1141998")
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[4]/div/div/div/div/div/div[3]/form/div[5]/button/div").click()
    time.sleep(10) #for me to click login
    print(driver.get_cookies())
    pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))
    

def login():
    driver.get(board)
    cookies = pickle.load(open(cookie_file, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

def upload(img):
    driver.get(pin_builder)
    upload = driver.find_element_by_id("media-upload-input")
    upload.send_keys(upload_folder + img)
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[2]/div").click()
    fashion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div[1]/div[2]/div[3]")))
    fashion.click()
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[2]/div").click()


# login()
get_session()
imgs = os.listdir(upload_folder)
# for img in imgs:
#     try:
#         upload(img)
#         time.sleep(5)
#     except:
#         pass
