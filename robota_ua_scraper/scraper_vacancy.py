import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from robota_ua_scraper.data_vacancy import URL, login_button, email_field, email_field_1, password_field, \
    password_field_1, login_button_1, email, password, search_link


class RobotaUA_Vacancy:
    def __init__(self, driver):
        self.driver = driver

    def parse_profiles(self):
        self.driver.get(URL)
        # email = input("email: ")
        # password = input("password: ")
        # search_link = input("Insert link: ")
        try:
            self.driver.find_element(By.CLASS_NAME, login_button).click()
            f1 = self.driver.find_element(By.CLASS_NAME, email_field)
            f1.find_element(By.CLASS_NAME, email_field_1).send_keys(email)
            f2 = self.driver.find_element(By.CLASS_NAME, password_field)
            f2.find_element(By.CLASS_NAME, password_field_1).send_keys(password)
            self.driver.find_element(By.TAG_NAME, login_button_1).click()
            print("login")
            time.sleep(2)

            self.driver.get(search_link)
            time.sleep(5)

            vc = self.driver.find_elements(By.CLASS_NAME, 'card')
            print(len(vc))

            vac_list = []
            for vac in vc:
                vac = [vac.get_attribute('href')]
                vac_str = '\n'.join(vac)
                vac_list.append(vac_str)
            print(vac_list)

            # self.parse_vacancy_page(vac_list)

        except Exception as e:
            print(e)
            sys.exit()

    # def parse_vacancy_page(self, vac_list):
    #     for i in vac_list:
    #         try:
    #             self.driver.get(i)
    #             time.sleep(2)
    #         except Exception as e:
    #             print("Cant get link. Error: ", e)

    def pagination(self):
        self.driver.get(search_link)

        pgn = self.driver.find_elements(By.CLASS_NAME, "ng-star-inserted")
        print(len(pgn))

        # pgg = self.driver.find_element(By.TAG_NAME, "div.side-btn.next")
        # pgg.click()

    # "/html/body/app-root/div[1]/alliance-cv-list-page/main/article/div/div/alliance-employer-cvdb-cv-list/div/nav/santa-pagination/div/div[5]"   ------   list

    def start(self):
        self.parse_profiles()
        # self.parse_vacancy_page()
        self.pagination()
