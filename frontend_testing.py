import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def check_user(user_id):
    driver = webdriver.Chrome(service=Service("/Users/anwarakram/Downloads/chromedriver_mac64/chromedriver"))
    driver.implicitly_wait(10)
    url = f"http://127.0.0.1:5001/get_user_name/{user_id}"
    driver.get(url)

    print(driver.current_url)

    element = driver.find_element(By.ID,value="user")
    print(element.text)

    return(element.text)
