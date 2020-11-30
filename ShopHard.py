from selenium import webdriver as wd
from webdriver_manager.chrome import ChromeDriverManager as CDM


browser = wd.Chrome(CDM().install())
browser.maximize_window()
browser.get("https://www.playstation.com/en-us/")
browser.find_element_by_class_name('sb-skeleton-signin-button').click()
i = 15000000
while i != 0:
	i-=1
browser.find_element_by_id("ember20").send_keys("riverax34@yahoo.com")
i = 15000000
while i != 0:
	i-=1
browser.find_element_by_class_name("primary-button.row-button.text-button").click()
browser.find_element_by_id("ember37").send_keys("Saphire16")
i = 15000000
while i != 0:
	i-=1
browser.find_element_by_class_name("primary-button.row-button.text-button").click()
i = 15000000
while i != 0:
	i-=1
#browser.get("https://direct.playstation.com/en-us/consoles/console/playstation5-console.3005816")
browser.get("https://direct.playstation.com/en-us/games/game/marvels-spider-man-miles-morales-launch-edition-ps5.3006168")
i = 15000000
while i != 0:
	i-=1
	
while i != 0:
	i-=1

browser.find_element_by_class_name("btn.transparent-orange-button.js-analyitics-tag.add-to-cart").click()
