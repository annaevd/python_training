class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # fill contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contactlist_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contactlist_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # popup close
        wd.switch_to_alert().accept()
        self.open_contactlist_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_contactlist_page()
        # open edit form for first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact edit form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()