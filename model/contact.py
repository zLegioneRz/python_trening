from sys import maxsize

class Contakt:

    def __init__(self, firstname= None, midlname= None, lastname= None, nickname= None,
        titl= None, company= None, adress= None, home_num= None,
        mob_nomber= None, work_num= None, fax= None, mail1= None,
        mail2= None, mail3= None, homepage= None, beyer= None, ayer= None,
        adress2= None, home2= None, notes= None, id= None, all_phones_from_home_page= None,
                 all_emails_from_home_page= None, birthday_month= None, year = None,
                 anniversary_date =None, anniversary_month =None, birthday_date=None, all_phones_from_view_page=None):

        self.firstname = firstname
        self.midlname = midlname
        self.lastname = lastname
        self.nickname = nickname
        self.titl = titl
        self.company = company
        self.adress = adress
        self.home_num = home_num
        self.mob_nomber = mob_nomber
        self.work_num = work_num
        self.fax = fax
        self.mail1 = mail1
        self.mail2 = mail2
        self.mail3 = mail3
        self.homepage = homepage
        self.beyer = beyer
        self.ayer = ayer
        self.adress2 = adress2
        self.home2 = home2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.birthday_month = birthday_month
        self.year =  year
        self.anniversary_date = anniversary_date
        self.anniversary_month = anniversary_month
        self.birthday_date = birthday_date
        self.all_phones_from_view_page = all_phones_from_view_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "[lastname= %s ; firstname= %s ; id= %s]" % (self.lastname, self.firstname, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname \
               and self.firstname == other.firstname
