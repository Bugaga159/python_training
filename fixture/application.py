from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from fixture.session import SessionHelper
from model.new_user import NewUser


class Application:
	def __init__(self):
		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		self.driver.implicitly_wait(60)
		self.session = SessionHelper(self)

	def destroy(self):
		self.driver.quit()

	def go_home_page(self):
		# go home page
		self.driver.find_element(By.LINK_TEXT, "home").click()

	def delete_user(self):
		self.go_home_page()
		self.driver.find_element(By.XPATH, "//td/input").click()
		self.driver.find_element(By.CSS_SELECTOR, ".left:nth-child(8) > input").click()
		self.driver.switch_to.alert.accept()

	def add_new_user(self, new_user: NewUser):
		self.driver.find_element(By.LINK_TEXT, "add new").click()
		self.driver.find_element(By.NAME, "firstname").click()
		self.driver.find_element(By.NAME, "firstname").send_keys("%s" % new_user.firstname)
		self.driver.find_element(By.NAME, "lastname").click()
		self.driver.find_element(By.NAME, "lastname").send_keys("%s" % new_user.lastname)
		self.driver.find_element(By.NAME, "address").click()
		self.driver.find_element(By.NAME, "address").send_keys("%s" % new_user.address)
		self.driver.find_element(By.NAME, "submit").click()

	def open_page(self):
		# open site
		self.driver.get("http://localhost/addressbook/")
		self.driver.set_window_size(1025, 729)
