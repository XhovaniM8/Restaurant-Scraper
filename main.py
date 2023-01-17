# Import the library Selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Make browser open in background
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Create the webdriver object
browser = webdriver.Chrome(
	executable_path="D:\chromedriver_win32\chromedriver.exe",
	options=options)

# Obtain the Google Map URL
url = ["https://www.google.com/maps/place/The+Smith/@40.755202,-73.9844665,15z/data=!4m10!1m2!2m1!1sRestaurants!3m6!1s0x89c2590246d9dfcd:0x4aa615566bd3359f!8m2!3d40.7552289!4d-73.9680559!15sCgtSZXN0YXVyYW50c1oNIgtyZXN0YXVyYW50c5IBE2FtZXJpY2FuX3Jlc3RhdXJhbnTgAQA!16s%2Fg%2F1tf_1_5y"]
# Initialize variables and declare it 0
i = 0

# Create a loop for obtaining data from URLs
for i in range(len(url)):

	# Open the Google Map URL
	browser.get(url[i])

	# Obtain the title of that place
	title = browser.find_element_by_class_name(
		"x3AX1-LfntMc-header-title-title")
	print(i+1, "-", title.text)

	# Obtain the ratings of that place
	stars = browser.find_element_by_class_name("aMPvhf-fI6EEc-KVuj8d")
	print("The stars of restaurant are:", stars.text)
	print("\n")
