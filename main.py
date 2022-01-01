from selenium import webdriver
from selenium.webdriver.common.by import By
import time
userName = "miladlahooti71@gmail.com"
password = "1371Ml71"
driver = webdriver.Firefox()
driver.get("https://www.digikala.com")
driver.find_element(By.CLASS_NAME, "c-header__btn-login").click()
driver.find_element(By.NAME, "login[email_phone]").send_keys(userName)
driver.find_element(By.CLASS_NAME, "c-login__form-action").click()
time.sleep(2)
driver.find_element(By.NAME, "login[password]").send_keys(password)
driver.find_element(By.CLASS_NAME, "o-btn--contained-red-lg").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "c-header__btn-profile").click()
time.sleep(2)
driver.close()
