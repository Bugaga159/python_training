import pytest
from fixture.application import Application
from model.new_user import NewUser


@pytest.fixture()
def app(request):
	fixture = Application()
	request.addfinalizer(fixture.destroy)
	return fixture


def test_addnewuser(app):
	app.login(user='admin', password='secret')
	app.add_new_user(NewUser(firstname="", lastname="", address=""))
	app.delete_user()
	app.logout()

def test_addnewuser_empy_data(app):
	app.login(user='admin', password='secret')
	app.add_new_user(NewUser(firstname="", lastname="", address=""))
	app.delete_user()
	app.logout()
