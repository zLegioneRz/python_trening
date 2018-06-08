import pytest
from fixture.application import Application
import json
import jsonpickle
import os.path
import importlib

fixture = None
target = None

# создание фикстуры
@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as file:
            target = json.load(file)
    if fixture is None or not fixture.is_vald():
        fixture = Application(browser=browser, baseurl=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


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