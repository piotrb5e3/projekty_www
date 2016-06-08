from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, string, random
from pkw_login_logout import login

def open_lubuskie(d):
    d.find_element_by_xpath('//*[@id="tabwoj"]/tr[4]/td[2]/a').click()
    time.sleep(2)
    e = d.find_element_by_xpath('//*[@id="ui-id-1"]')
    assert "lubuskie, woj." in e.text


def open_lubuskie_edit(d):
    open_lubuskie(d)
    d.find_element_by_xpath('//*[@id="listbody"]/tr/td[4]/a').click()
    time.sleep(2)
    e = d.find_element_by_xpath('//*[@id="edittab"]/tbody/tr[1]/th[1]')
    assert "Kandydat" in e.text


def editform_input(d, nk1, nk2):
    time.sleep(2)
    e = d.find_element_by_xpath('//*[@id="K1input"]')
    e.clear()
    e.send_keys(nk1)
    time.sleep(2)
    e = d.find_element_by_xpath('//*[@id="K2input"]')
    e.clear()
    e.send_keys(nk2)

def editform_submit(d):
    time.sleep(2)
    d.find_element_by_xpath('//*[@id="gobutton"]').click()

try:
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

   # Test for edit functionality

    login(driver, "alice", "bobbobbob")
    open_lubuskie(driver)
    time.sleep(2)
    e = driver.find_element_by_xpath('//*[@id="listbody"]/tr/td[2]')
    k1 = e.text
    time.sleep(2)
    e = driver.find_element_by_xpath('//*[@id="listbody"]/tr/td[3]')
    k2 = e.text
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="listbody"]/tr/td[4]/a').click()
    editform_input(driver, k2, k1)
    editform_submit(driver)
    time.sleep(5)
    a = driver.switch_to_alert()
    a.accept()
    time.sleep(5)
    open_lubuskie(driver)
    time.sleep(2)
    e = driver.find_element_by_xpath('//*[@id="listbody"]/tr/td[2]')
    assert k2 in e.text
    time.sleep(2)
    e = driver.find_element_by_xpath('//*[@id="listbody"]/tr/td[3]')
    assert k1 in e.text
   
finally:
    driver.close()

