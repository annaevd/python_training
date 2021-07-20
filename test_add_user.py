# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_users_page(wd)
        self.create_user(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_user(self, wd):
        # fill user form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Anna")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Evdokimova")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Saint-Petersburg")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("+79211111111")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("test@test.ru")
        # submit user creation
        wd.find_element_by_name("submit").click()

    def open_users_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
