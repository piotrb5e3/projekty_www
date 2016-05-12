from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, string, random
from pkw_login_logout import login

def open_lubuskie(d):
    d.find_element_by_xpath('//*[@id="tabw"]/table/tbody/tr[7]/td[2]/a').click()
    e = d.find_element_by_xpath('//*[@id="ui-id-1"]')
    assert "Gminy w lubuskie, woj." in e.text


def open_lubuskie_edit(d):
    open_lubuskie(d)
    d.find_element_by_xpath('//*[@id="seemore"]/tbody/tr[3]/td[4]/a').click()
    e = d.find_element_by_xpath('//*[@id="edittab"]/tbody/tr[1]/th[1]')
    assert "Kandydat" in e.text


def editform_input(d, nk1, nk2):
    e = d.find_element_by_xpath('//*[@id="id_k1"]')
    e.clear()
    e.send_keys(nk1)
    e = d.find_element_by_xpath('//*[@id="id_k2"]')
    e.clear()
    e.send_keys(nk2)

def editform_submit(d):
    d.find_element_by_xpath('//*[@id="geditid"]/button[1]').click()

try:
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

   # Test for edit functionality

    login(driver, "alice", "bobbobbob")
    open_lubuskie(driver)
    e = driver.find_element_by_xpath('//*[@id="seemore"]/tbody/tr[3]/td[2]')
    k1 = e.text
    e = driver.find_element_by_xpath('//*[@id="seemore"]/tbody/tr[3]/td[3]')
    k2 = e.text
    driver.find_element_by_xpath('//*[@id="seemore"]/tbody/tr[3]/td[4]/a').click()
    editform_input(driver, k2, k1)
    editform_submit(driver)
    time.sleep(5)
    a = driver.switch_to_alert()
    a.accept()
    time.sleep(5)
    open_lubuskie(driver)
    e = driver.find_element_by_xpath('//*[@id="seemore"]/tbody/tr[3]/td[2]')
    assert k2 in e.text
    e = driver.find_element_by_xpath('//*[@id="seemore"]/tbody/tr[3]/td[3]')
    assert k1 in e.text
   
finally:
    driver.close()
