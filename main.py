import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from robota_ua_scraper.scraper_profiles import RabotaUA
from robota_ua_scraper.scraper_vacancy import RobotaUA_Vacancy

if __name__ == '__main__':
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('/home/nazim/PycharmProjects/Rabota.UA/chromedriver')

    # work = RobotaUA(driver)
    # work.start()

    work = RobotaUA_Vacancy(driver)
    work.start()

    time.sleep(1000)
