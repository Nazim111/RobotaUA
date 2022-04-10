import sys
import time

from selenium.webdriver.common.by import By

from robota_ua_scraper.data_profiles import URL, login_button, email_field, email_field_1, password_field, \
    password_field_1, \
    login_button_1, opened_contacts_button, open_contacts_button, name_t, age_t, vacancy_t, number_t, email, password, \
    search_link


class RabotaUA:
    def __init__(self, driver):
        self.driver = driver

    def parse_profiles(self):

        #self.driver.get(URL)
        # email = input("email: ")
        # password = input("password: ")
        # search_link = input("Insert link: ")
        try:
            # self.driver.find_element(By.CLASS_NAME, login_button).click()
            # f1 = self.driver.find_element(By.CLASS_NAME, email_field)
            # f1.find_element(By.CLASS_NAME, email_field_1).send_keys(email)
            # f2 = self.driver.find_element(By.CLASS_NAME, password_field)
            # f2.find_element(By.CLASS_NAME, password_field_1).send_keys(password)
            # self.driver.find_element(By.TAG_NAME, login_button_1).click()
            # print("login")
            # time.sleep(2)

            self.driver.get(search_link)
            time.sleep(2)

            cvc = self.driver.find_elements(By.TAG_NAME, 'alliance-employer-cvdb-cv-list-card')
            print(len(cvc))

            cv_list = []
            x = 1
            for cv in range(len(cvc)):
                cv = self.driver.find_elements(By.XPATH, f"/html/body/app-root/div["
                                                         f"1]/alliance-cv-list-page/main/article/div/div/alliance"
                                                         f"-employer-cvdb-cv-list/div/div/alliance-employer-cvdb-cv"
                                                         f"-list-card["
                                                         f"{x}]/section/div/alliance-shared-link-wrapping/a")
                for link in cv:
                    cand = [link.get_attribute('href')]
                    cand_str = '\n'.join(cand)
                    cv_list.append(cand_str)
                x += 1

            self.parse_profile_page(cv_list)
            self.pagination(search_link)
        except Exception as e:
            print(e)
            sys.exit()

    def parse_profile_page(self, cv_list):
        for i in cv_list:
            try:
                self.driver.get(i)
                time.sleep(2)
            except Exception as e:
                print("Cant get link. Error: ", e)
            try:
                element_2 = self.driver.find_element(By.CLASS_NAME, opened_contacts_button)
                if element_2.text == "Предложить вакансию":
                    print("Contacts was opened")
                    time.sleep(2)
                    pass
            except:
                time.sleep(2)
                try:
                    element_1 = self.driver.find_element(By.TAG_NAME, open_contacts_button)
                    if element_1.text == "Открыть контакты":
                        print("Click on: 'Открыть контакты'", element_1.text)
                        element_1.click()
                        time.sleep(2)
                except:
                    print("Cant find button")
                    try:
                        name = self.driver.find_element(By.CLASS_NAME, name_t).text
                        print(name)
                        time.sleep(2)
                    except:
                        print("Cant parse name")
                    try:
                        age_form = self.driver.find_elements(By.TAG_NAME, age_t)
                        for age in age_form:
                            age = age.text
                            if age.endswith('года') or age.endswith('лет'):
                                print(age)
                                time.sleep(2)
                    except:
                        print("Cant parse age")
                    try:
                        vacancy = self.driver.find_element(By.CLASS_NAME, vacancy_t).text
                        print(vacancy)
                        time.sleep(2)
                    except:
                        print("Cant parse vacancy")
                    try:
                        number = self.driver.find_element(By.CLASS_NAME, number_t).text
                        print(number)
                        time.sleep(2)
                    except:
                        print("Cant parse number")
            print('\n')

    def pagination(self):
        global i
        self.driver.get(search_link)

        pgn = self.driver.find_elements(By.XPATH,
                                        "/html/body/app-root/div[1]/alliance-cv-list-page/main/article/div[1]/div/alliance-employer-cvdb-cv-list/div/nav/santa-pagination/div/div")
        print(len(pgn))

        pgg = self.driver.find_element(By.TAG_NAME, "div.side-btn.next")
        pgg.click()








# "/html/body/app-root/div[1]/alliance-cv-list-page/main/article/div/div/alliance-employer-cvdb-cv-list/div/nav/santa-pagination/div/div[5]"   ------   list







    def start(self):
        self.parse_profiles()
        self.parse_profile_page()
        self.pagination()
