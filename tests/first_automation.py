from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

driver = webdriver.Firefox()

driver.get("127.0.0.1:5000")
#assert "Python" in driver.title
driver.close()







# https://www.geeksforgeeks.org/locating-single-elements-in-selenium-python/