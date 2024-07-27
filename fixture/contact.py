from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        self.return_to_home_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def change_dropdown_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            dropdown = wd.find_element(By.NAME, field_name)
            dropdown.find_element(By.XPATH, f".//option[. = '{text}']").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.tel_home)
        self.change_field_value("mobile", contact.tel_mobile)
        self.change_field_value("work", contact.tel_work)
        self.change_field_value("fax", contact.tel_fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("ayear", contact.ayear)
        self.change_dropdown_value("bday", contact.bday)
        self.change_dropdown_value("bmonth", contact.bmonth)
        self.change_dropdown_value("aday", contact.aday)
        self.change_dropdown_value("amonth", contact.amonth)

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # select first group for editing
        wd.find_element(By.XPATH, "// img[ @ title = 'Edit']").click()
        self.fill_contact_form(contact)
        # submit contact update
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.open_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()