from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver

def add_todo(driver, item_text):
    input_box = driver.find_element(By.CLASS_NAME, "new-todo")
    input_box.clear()
    input_box.send_keys(item_text)
    input_box.send_keys(Keys.ENTER)

def get_todos(driver):
    return driver.find_elements(By.CSS_SELECTOR, ".todo-list li")

def filter_selector(driver, filter_name):
    return driver.find_element(By.LINK_TEXT, filter_name)