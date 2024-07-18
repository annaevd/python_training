from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def open_group_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def create_new_contact(self, contact):
        wd = self.wd
        # init contact creation
        wd.find_element(By.LINK_TEXT, "add new").click()
        # fill contact form
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(contact.tel_home)
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.tel_mobile)
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(contact.tel_work)
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(contact.tel_fax)
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        dropdown = wd.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, f"//select[@name='bday']/option[. = '{contact.bday}']").click()
        dropdown.find_element(By.XPATH, f"//select[@name='bmonth']/option[. = '{contact.bmonth}']").click()
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        dropdown.find_element(By.XPATH, f"//select[@name='aday']/option[. ='{contact.aday}']").click()
        dropdown.find_element(By.XPATH, f"//select[@name='amonth']/option[. = '{contact.amonth}']").click()
        wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        # submit contact creation
        wd.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        self.return_to_home_page()

    def destroy(self):
        self.wd.quit()
