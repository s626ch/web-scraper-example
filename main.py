from selenium import webdriver # actually tell chromedriver what to do, and programmaticaly operate it.
from selenium.webdriver.common.by import By # to find elements "By" 
import os

def scrapeInfo():
    currentdirectory = os.getcwd()
    driverpath = os.path.join(currentdirectory, 'chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--log-level=3')
    browser = webdriver.Chrome(executable_path=driverpath, chrome_options=options)
    # ^ browser setup
    # v navigation and scraping
    browser.get("https://www.google.com/search?q=ohio+weather")
    temperature = browser.find_element(By.XPATH, '//*[@id="wob_tm"]').get_attribute("textContent")
    precipitation = browser.find_element(By.XPATH, '//*[@id="wob_pp"]').get_attribute("textContent")
    humidity = browser.find_element(By.XPATH, '//*[@id="wob_hm"]').get_attribute("textContent")
    wind = browser.find_element(By.XPATH, '//*[@id="wob_ws"]').get_attribute("textContent")
    city = browser.find_element(By.XPATH, '//*[@id="wob_loc"]').get_attribute("textContent")
    day_time = browser.find_element(By.XPATH, '//*[@id="wob_dts"]').get_attribute("textContent")
    status = browser.find_element(By.XPATH, '//*[@id="wob_dc"]').get_attribute("textContent")
    # print to console
    print(f"""
    Temperature: {temperature} deg F
    Precipitation: {precipitation}
    Humidity: {humidity}
    Wind: {wind}
    Location: {city}
    Day and time: {day_time}
    Status: {status}
    """)

scrapeInfo()
