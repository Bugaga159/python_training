from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from fixture.new_user import NewUserHelper
from fixture.session import SessionHelper



class Application:
	def __init__(self):
		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		self.driver.implicitly_wait(60)
		self.session = SessionHelper(self)
		self.new_user = NewUserHelper(self)

	def destroy(self):
		self.driver.quit()

	def open_page(self):
		# open site
		self.driver.get("http://localhost/addressbook/")
		self.driver.set_window_size(1025, 729)
