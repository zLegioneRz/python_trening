import jsonpickle
import getopt
import sys
import os
import random
import string
from model.group import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/groups.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


# testdata
test_data = [Group(group_name="", header="", footer="")] + [Group(group_name=random_string('name', 10),
                                                            header=random_string('header', 20), footer=random_string('footer', 20)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)
with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))