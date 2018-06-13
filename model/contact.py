from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None,
                 title=None, company=None, address=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None,
                 email=None, email2=None, email3=None, homepage=None,
                 birthday_date=None, birthday_month=None, anniversary_date=None, anniversary_month=None,
                 byear=None, ayear=None, address2=None, secondary_phone=None, notes=None, id=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None, all_phones_from_view_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday_date = birthday_date
        self.birthday_month = birthday_month
        self.anniversary_date = anniversary_date
        self.anniversary_month = anniversary_month
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.secondary_phone = secondary_phone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_view_page = all_phones_from_view_page

    def __repr__(self):
        return "[lastname= %s ; firstname= %s ; id= %s]" % (self.lastname, self.firstname, self.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname \
               and self.firstname == other.firstname
