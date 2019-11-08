from selenium import webdriver
from selenium.webdriver.common.keys import Keys

site = "https://www.supremenewyork.com/shop/"

driver = webdriver.Chrome()
driver.get(site)
links = driver.find_element_by_tag_name("a")

print(links)