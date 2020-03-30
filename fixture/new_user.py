from selenium.webdriver.common.by import By
from model.new_user import NewUser


class NewUserHelper:
	def __init__(self, app):
		self.app = app

	def go_home_page(self):
		# go home page
		self.app.driver.find_element(By.LINK_TEXT, "home").click()

	def delete(self):
		self.go_home_page()
		self.app.driver.find_element(By.XPATH, "//td/input").click()
		self.app.driver.find_element(By.CSS_SELECTOR, ".left:nth-child(8) > input").click()
		self.app.driver.switch_to.alert.accept()

	def add(self, new_user: NewUser):
		self.app.driver.find_element(By.LINK_TEXT, "add new").click()
		self.app.driver.find_element(By.NAME, "firstname").click()
		self.app.driver.find_element(By.NAME, "firstname").send_keys("%s" % new_user.firstname)
		self.app.driver.find_element(By.NAME, "lastname").click()
		self.app.driver.find_element(By.NAME, "lastname").send_keys("%s" % new_user.lastname)
		self.app.driver.find_element(By.NAME, "address").click()
		self.app.driver.find_element(By.NAME, "address").send_keys("%s" % new_user.address)
		self.app.driver.find_element(By.NAME, "submit").click()