from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, string, random

def login(d, uname, passwd):
    d.get("http://localhost:8000")
    assert "Wybory" in d.title
    e = d.find_element_by_xpath('//*[@id="uname"]/a') # Link 'Zaloguj'
    if "Zaloguj" not in e.text:
        return
    e.click()


    e = d.find_element_by_xpath('//*[@id="id_username"]') # Username field
    e.send_keys(uname)

    e = d.find_element_by_xpath('//*[@id="id_password"]') # Passwd field
    e.send_keys(passwd)

    e = d.find_element_by_xpath('//*[@id="login-form"]/input[2]') # Submit button
    e.click()

    assert "Wybory" in d.title
    e = d.find_element_by_xpath('//*[@id="uname"]') # Div #uname
    assert uname in e.text

try:
    driver = webdriver.Firefox()

    login(driver, "alice", "bobbobbob")

    e = driver.find_element_by_xpath('//*[@id="uname"]/a') # Link 'Wyloguj'
    assert "Wyloguj" in e.text
    e.click()
    
    driver.get("http://127.0.0.1:8000")
    assert "Wybory" in driver.title
    e = driver.find_element_by_xpath('//*[@id="uname"]/a') # Link 'Zaloguj'
    assert "Zaloguj" in e.text

finally:
    driver.close()

