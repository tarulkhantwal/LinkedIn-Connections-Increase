from selenium import webdriver
from secret import lw
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
from selenium.webdriver.chrome.options import Options

tar=[]
driver = webdriver.Chrome(executable_path=r'F:/chromedriver_win32/chromedriver.exe')
# options=options()
# options.add_argument('--disable-infobars')

driver.get("https://linkedin.com")

# driver.maximize_window()
# sleep(10)
# pyautogui.moveTo(1880, 140)
# sleep(10)
# pyautogui.click(1880, 140)

sleep(2)
driver.find_element_by_xpath('/html/body/nav/a[3]').click()
sleep(2)
driver.find_element_by_id("username").send_keys("icda.you@gmail.com")
driver.find_element_by_id("password").send_keys(lw)
driver.find_element_by_xpath('//button[@type="submit"]').click()
sleep(2)
driver.find_element_by_id("mynetwork-tab-icon").click()
sleep(2)
driver.find_element_by_class_name("msg-overlay-bubble-header").click() #MEssage box pop-up
sleep(2)
driver.execute_script("window.scrollBy(0,500)","")
sleep(2)
driver.find_element_by_class_name('discover-person-card__name').click()
sleep(3)
driver.find_element_by_class_name("pv-s-profile-actions").click()
sleep(3)
driver.find_element_by_class_name('ml1').click()
sleep(3)
driver.execute_script("window.scrollBy(0,200)","")
sleep(10)


while True:	
	driver.find_element_by_xpath("//button[contains(@class,'full-width')]").click()
	sleep(2)
	driver.refresh()
	# driver.find_element_by_xpath("/button[contains(@class,'artdeco-button__icon')]").click()
	# sleep(2)
	
	

	# driver.execute_script("window.scrollBy(0,600)","")
	# driver.find_element_by_xpath("//button[contains(@class,'full-width')]").click()
	# sleep(3)
	# driver.refresh()	
	
	