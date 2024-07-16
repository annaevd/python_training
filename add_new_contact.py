# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from contact import Contact
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestAddContact():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_add_contact(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.create_new_contact(Contact(
            firstname="Anna", middlename="Maria", lastname="Tener", nickname="annate",
            title="Title Anna", company="Company Anna", address="Address Anna",
            tel_home="+79215674523", tel_mobile="+79991111111", tel_work="+7888222222", tel_fax="+77773333333",
            email="anna@test.ru",email2="anna2@test.ru", email3="anna3@test.ru",
            homepage="http://localhost/addressbook/",
            bday="1", bmonth="January", byear="2002", aday="7", amonth="June", ayear="2021"))
        self.return_to_home_page()
        self.logout()

    def return_to_home_page(self):
        self.driver.find_element(By.LINK_TEXT, "home page").click()

    def create_new_contact(self, contact):
        # init contact creation
        self.driver.find_element(By.LINK_TEXT, "add new").click()
        # fill contact form
        self.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.driver.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        self.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        self.driver.find_element(By.NAME, "title").send_keys(contact.title)
        self.driver.find_element(By.NAME, "company").send_keys(contact.company)
        self.driver.find_element(By.NAME, "address").send_keys(contact.address)
        self.driver.find_element(By.NAME, "home").send_keys(contact.tel_home)
        self.driver.find_element(By.NAME, "mobile").send_keys(contact.tel_mobile)
        self.driver.find_element(By.NAME, "work").send_keys(contact.tel_work)
        self.driver.find_element(By.NAME, "fax").send_keys(contact.tel_fax)
        self.driver.find_element(By.NAME, "email").send_keys(contact.email)
        self.driver.find_element(By.NAME, "email2").send_keys(contact.email2)
        self.driver.find_element(By.NAME, "email3").send_keys(contact.email3)
        self.driver.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        dropdown = self.driver.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, f"//select[@name='bday']/option[. = '{contact.bday}']").click()
        dropdown.find_element(By.XPATH, f"//select[@name='bmonth']/option[. = '{contact.bmonth}']").click()
        self.driver.find_element(By.NAME, "byear").send_keys(contact.byear)
        dropdown.find_element(By.XPATH, f"//select[@name='aday']/option[. ='{contact.aday}']").click()
        dropdown.find_element(By.XPATH, f"//select[@name='amonth']/option[. = '{contact.amonth}']").click()
        self.driver.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        # submit contact creation
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def login(self, username, password):
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()



