from model.contact import Contakt
import random
import string

months = ( "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
           "November", "December")


def get_random_name():
    return "%s%s" % (get_random_string_uppercase(1), get_random_string_lowercase(3, 6))


def get_random_email():
    return "%s@%s.%s" % (get_random_string_lowercase(3, 6), get_random_string_lowercase(3, 6), get_random_string_lowercase(2, 4))


def get_random_address():
    return "%s%s" % (get_random_string_uppercase(1), get_random_string_lowercase(3, 6))


def get_random_text(max_len):
    symbols = string.ascii_letters + string.digits + " " * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(max_len))])

def get_random_string_lowercase(min_len, max_len):
    return "".join([random.choice(string.ascii_lowercase) for i in range(random.randrange(min_len, max_len))])


def get_random_string_uppercase(len):
    return "".join([random.choice(string.ascii_uppercase) for i in range(len)])


def get_random_string_digits(min_len, max_len):
    return "".join([random.choice(string.digits) for i in range(random.randrange(min_len, max_len))])


def get_random_day():
    return "".join(map(str, [random.randint(1,31)]))


def get_random_year():
    return "".join(map(str, [random.randint(1980, 2000)]))

def get_random_months():
    return "".join([random.choice(months)])


test_data = [Contakt(firstname=get_random_name(),midlname=get_random_name(),lastname=get_random_name(),
                     nickname=get_random_name(),titl=get_random_name(), company=get_random_name(),
                     adress=get_random_address(),home_num=get_random_string_digits(10, 11),
                     mob_nomber=get_random_string_digits(10, 11), work_num=get_random_string_digits(10, 11),
                     fax=get_random_string_digits(10, 11), mail1=get_random_email(), mail2=get_random_email(),
                     mail3=get_random_email(), homepage=get_random_email(), birthday_date=get_random_day(),
                     birthday_month=get_random_months(),beyer=get_random_year(), anniversary_date=get_random_day(),
                     anniversary_month=get_random_months(),ayer=get_random_year(),adress2=get_random_address(),
                     home2=get_random_string_digits(10, 11),notes=get_random_text(10)),

             Contakt(firstname="", lastname="", adress="", home_num="", work_num="",
                     mob_nomber="", home2="",
                     mail1="", mail2="", mail3="")]