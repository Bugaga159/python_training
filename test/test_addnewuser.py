import pytest
from fixture.application import Application
from model.new_user import NewUser


@pytest.fixture()
def app(request):
	fixture = Application()
	request.addfinalizer(fixture.destroy)
	return fixture


def test_addnewuser(app):
	app.session.login(user='admin', password='secret')
	app.new_user.add(NewUser(firstname="", lastname="", address=""))
	app.new_user.delete()
	app.session.logout()

def test_addnewuser_empy_data(app):
	app.session.login(user='admin', password='secret')
	app.new_user.add(NewUser(firstname="", lastname="", address=""))
	app.new_user.delete()
	app.session.logout()
