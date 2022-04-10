import time

from selenium import webdriver


driver = webdriver.Chrome('/home/nazim/PycharmProjects/Rabota.UA/chromedriver')  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/');

time.sleep(500) # Let the user actually see something!

driver.quit()