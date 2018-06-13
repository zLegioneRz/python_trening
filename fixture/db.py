import pymysql
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        result_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                (id, name, header, footer) = row
                result_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            self.connection.commit()
            cursor.close()
        return result_list

    def get_contact_list(self):
        result_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, firstname, lastname, address, email, email2, email3,'
                           'home, mobile, work, fax, phone2 from addressbook where deprecated="0000-00-00 00:00:00"')
            for row in cursor:
                (id, first_name, last_name, address, email, email2, email3, home, mobile, work, fax, phone2) = row
                result_list.append(Contact(id=str(id), firstname=first_name, lastname=last_name, address=address,
                                           email=email, email2=email2, email3=email3, home_phone=home,
                                           mobile_phone=mobile, work_phone=work, fax=fax, secondary_phone=phone2))
        finally:
            cursor.close()
        return result_list