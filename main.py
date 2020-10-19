from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui

opt = Options()
opt.add_argument("--start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("-–disable-notifications")
prefs = {"profile.default_content_setting_values.notifications" : 2}
opt.add_experimental_option("prefs",prefs)
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
})

# Write the path where you have kept your Chromedriver in executable_path
driver = webdriver.Chrome(chrome_options = opt, executable_path="E:\Py\chromedriver.exe")
Path = "https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=AddSession"
driver.get(Path)


email = driver.find_element_by_xpath('//*[@id="identifierId"]')
email.click()
email.send_keys('2018.neha.gupta@ves.ac.in')

next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
next.click()

time.sleep(3)
password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.click()
password.send_keys('krish02#')

next = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
next.click()

time.sleep(20)
classes = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[2]/div/ol/li[1]/div[1]/div[3]/h2/a[1]/div[1]')
classes.click()

time.sleep(5)
Meetlink = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/span/a/div')
Meetlink.click()

switch_tab = driver.window_handles[1]
driver.switch_to.window(switch_tab)

time.sleep(12)
pyautogui.moveTo(736, 224, 2)
pyautogui.click()
pyautogui.hotkey('ctrl', 'd')
pyautogui.hotkey('ctrl', 'e')

time.sleep(3)
join = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
join.click()
