import random
import string
from model.group import Group




def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


test_data = [Group(name=name, header=header, footer=footer)
             for name in ["", random_string('name', 10)]
             for header in ["", random_string('header', 10)]
             for footer in ["", random_string('footer', 10)]
             ]
