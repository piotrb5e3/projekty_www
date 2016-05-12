from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, string, random

try:
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000")
    assert "Wybory" in driver.title
    driver.get("http://127.0.0.1:8000/admin")
    e = driver.find_element_by_id("id_username")
    e.send_keys("admin")
    e = driver.find_element_by_id("id_password")
    e.send_keys("adminadmin")
    e = driver.find_element_by_xpath("//input[@type='submit']")
    e.click()
    e = driver.find_element_by_xpath("//*[@id='content']/h1").text 
    assert "Site administration" in e
    driver.get("http://127.0.0.1:8000/admin/election/kandydat/5/change/")
    e = driver.find_element_by_xpath("//*[@id='id_imiona']")
    e.clear()
    ss = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
    e.send_keys(ss)
    e = driver.find_element_by_xpath("//*[@id='kandydat_form']/div/div/input[1]")
    e.click()
    driver.find_element_by_link_text("LOG OUT").click()
    driver.get("http://127.0.0.1:8000")
    e = driver.find_element_by_xpath("//*[@id='panel_final']/p[2]/a")
    assert ss in e.text
    time.sleep(1)
finally:
    driver.close()

