from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, home=None, mobile=None, work=None,
                 fax=None, all_phones_from_home_page=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s%s:%s%s:%s" % (self.id, self.lastname, self.firstname, self.home, self.mobile, self.work, self.fax)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
                self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
