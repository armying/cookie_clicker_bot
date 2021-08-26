""" AUTOMATE COOKIE CLICKER GAME BOT"""

from selenium import webdriver
import time

CHROME_DRIVER_LOC = "C:/Users/Army/Desktop/Development/chromedriver.exe"
WEB_URL = "https://orteil.dashnet.org/cookieclicker/"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_LOC)
driver.get(WEB_URL)

cookie = driver.find_element_by_css_selector("#cookieAnchor #bigCookie")
timeout = time.time() + 60*5
next_five = time.time() + 5
upgrade = False
cursor = False
while True:

    if time.time() > timeout:
        break
    cookie.click()
    if time.time() > next_five:
        next_five = time.time() + 5

        products = driver.find_elements_by_css_selector(".enabled")
        prices = driver.find_elements_by_css_selector(".enabled .price")
        products.reverse()
        prices.reverse()
        cookies = driver.find_element_by_id("cookies").text.split(" ")[0]
        cookies = int(str(cookies).replace(",", ""))
        # Upgrade cursor
        if cursor is True:
            first_upgrade = driver.find_element_by_css_selector("#upgrades #upgrade0")
            first_upgrade.click()
        # Purchase Products
        for ind, p in enumerate(prices):
            price = int(str(p.text).replace(",", ""))
            if cookies > price:
                products[ind].click()
            cursor = True

cookie_per_sec = driver.find_element_by_id("cookies").text.split(" ")[1:]
message = "".join(cookie_per_sec)
print(message)

driver.quit()
