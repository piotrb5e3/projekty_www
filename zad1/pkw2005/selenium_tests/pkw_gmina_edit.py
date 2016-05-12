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

try:
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

    driver.get("http://localhost:8000")

    # Test seemore modal window

    open_lubuskie(driver)

    # Test for login prompt when you try to edit without login:

    driver.find_element_by_xpath('//*[@id="seemore"]/tbody/tr[3]/td[4]/a').click()
    e = driver.find_element_by_xpath('//*[@id="content-main"]/p[1]')
    assert "Please login to see this page" in e.text

    # Test for no login prompt when you try to edit as a logged user

    login(driver, "alice", "bobbobbob")
    open_lubuskie_edit(driver)
  
finally:
    driver.close()

