import pytest
from fixture.application import Application
import json
import jsonpickle
import os.path
import importlib
from fixture.db import Dbfixture

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

# создание фикстуры
@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_vald():
        fixture = Application(browser=browser, baseurl=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture

@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = Dbfixture(host=db_config['host'], name= db_config['name'], user = db_config['user'],password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture



@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def end():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(end)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption('--target', action='store', default='target.json')

def load_from_module(module):
    return importlib.import_module('data.%s' % module).test_data

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return  jsonpickle.decode(f.read())

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            test_data = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        elif fixture.startswith('json_'):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])