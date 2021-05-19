from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.codechef.com")
username = browser.find_element_by_id("edit-name")
username.send_keys("thaakur_")
password = browser.find_element_by_id("edit-pass")
from getpass import getpass
password.send_keys(getpass("Enter Password : "))
browser.find_element_by_id("edit-submit").click()
browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()
problem = input()
browser.get("https://codechef.com/submit/" + problem)
with open("solution.cpp", 'r') as f:
    code = f.read()
coding = browser.find_element_by_id("edit-program")
coding.send_keys(code)
browser.find_element_by_xpath('//*[@id="edit-language"]/option[1]')
browser.find_element_by_id("edit-submission").click()

