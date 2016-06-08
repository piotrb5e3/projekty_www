from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, string, random
from pkw_login_logout import login

def open_lubuskie(d):
    time.sleep(2)
    d.find_element_by_xpath('//*[@id="tabwoj"]/tr[4]/td[2]/a').click()
    time.sleep(2)
    e = d.find_element_by_xpath('//*[@id="ui-id-1"]')
    assert "lubuskie, woj." in e.text


def open_lubuskie_edit(d):
    open_lubuskie(d)
    time.sleep(2)
    d.find_element_by_xpath('//*[@id="listbody"]/tr/td[4]/a').click()
    time.sleep(2)
    e = d.find_element_by_xpath('//*[@id="edittab"]/tbody/tr[1]/th[1]')
    assert "Kandydat" in e.text

try:
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    time.sleep(2)

    driver.get("http://localhost:8000")

    # Test seemore modal window

    open_lubuskie(driver)

    # Test for login prompt when you try to edit without login:

    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="listbody"]/tr/td[4]/a').click()
    time.sleep(2)
    e = driver.find_element_by_xpath('//*[@id="login-form"]/table/tbody/tr[1]/td[1]/label')
    assert "name" in e.text

    # Test for no login prompt when you try to edit as a logged user

    login(driver, "alice", "bobbobbob")
    time.sleep(2)
    driver.get("http://localhost:8000")
    open_lubuskie_edit(driver)
  
finally:
    driver.close()

