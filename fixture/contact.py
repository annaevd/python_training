from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
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
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        dropdown.find_element(By.XPATH, f"//select[@name='aday']/option[. ='{contact.aday}']").click()
        dropdown.find_element(By.XPATH, f"//select[@name='amonth']/option[. = '{contact.amonth}']").click()
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        # submit contact creation
        wd.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        self.return_to_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # select first group for editing
        wd.find_element(By.XPATH, "// img[ @ title = 'Edit']").click()
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
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        dropdown.find_element(By.XPATH, f"//select[@name='aday']/option[. ='{contact.aday}']").click()
        dropdown.find_element(By.XPATH, f"//select[@name='amonth']/option[. = '{contact.amonth}']").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        # submit contact update
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first group
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.open_home_page()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()