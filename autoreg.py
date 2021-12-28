from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def main(log, pswd):
	# log = 'test'
	# em = 'teeeessts@gmail.com'
	# pswd = 'killnixgers'
	driver = webdriver.Firefox(executable_path=r'C:\Users\crja73\geckodriver.exe')
	driver.get("https://accederz.tech/login/")
	text = "Log in"

	xpath = "/html[@id='XF']/body/div[@id='top']/div[@class='p-body']/div[@class='p-body-inner']/div[@class='p-body-main  ']/div[@class='p-body-content']/div[@class='p-body-pageContent']/div[@class='blocks']/form[@class='block']/div[@class='block-container']/dl[@class='formRow formSubmitRow']/dd/div[@class='formSubmitRow-main']/div[@class='formSubmitRow-controls']/button[@class='button--primary button button--icon button--icon--login']"
	element2 = driver.find_element_by_name('login')
	element2.send_keys(log)

	element3 = driver.find_element_by_name('password')
	element3.send_keys(pswd)


	element4 = driver.find_element_by_xpath(xpath)

	#driver.execute_script("arguments[0].click();", element4)
	element4.click()


	try:
		driver.find_element_by_xpath("/html[@id='XF']/body/div[@id='top']/div[@class='p-body']/div[@class='p-body-inner']/div[@class='p-body-main p-body-main--withSidebar ']/div[@class='p-body-sidebar']/div[@class='block'][1]/div[@class='block-container']/div[@class='block-body block-row']")
		return True
	except:
		return False


	driver.close()