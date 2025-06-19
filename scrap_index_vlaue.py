from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from datetime import datetime
import smtplib


#SET driver settings and open it in Chrome browser. 
def get_driver():

  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  
  return driver


def save_to_csv(index_value, btc_price,vwce_price,btce_price,ssln_price):

  # Define the file name
  file_name = "fear_greed_index.csv"
  
  # Check if the file already exists
  try:
      with open(file_name, "r", encoding="utf-8") as file:
          header_exists = file.readline()
  except FileNotFoundError:
      header_exists = False

  # Open the file in append mode
  with open(file_name, mode="a", newline="", encoding="utf-8") as file:
      writer = csv.writer(file, delimiter=";")
      
      # Write header if it's a new file
      if not header_exists:
          writer.writerow(["DateOfMeasuring", "Index Value", "Bitcoin Value ($)", "VWCE Value (EUR)", "BTCE Value (EUR)", "SSLN Value (EUR)"])
      
      # Write the data row
      writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), index_value, btc_price, vwce_price,btce_price,ssln_price])


def send_email(index_value, btc_price, vwce_price,btce_price,ssln_price):
    sender_email = "" #Enter your mail
    receiver_email = "" # #Enter reciver your mail
    password = ""  #Use mail application password for sending mail on SMTP server 

    message = f"Subject: Warring for Market!\n\nThe index values ​​indicate how the market will behave. If the index falls below 25, it means that there is a crisis and it is an excellent opportunity to buy. If the index value is above 75, it means that the market is at its peak and that a correction and a fall in prices will follow due to greed. \nCurrent values: \n - Fear&Greed Index: {index_value} \n - Bitcoin price [$]: {btc_price} \n - VWCE price [EUR]: {vwce_price}\n - BTCE price[EUR]: {btce_price} \n - SSLN price [EUR]: {ssln_price}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)



def fear_greed_index(driver):
  driver.get("https://edition.cnn.com/markets/fear-and-greed")
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/section[4]/section[1]/section[1]/div/section/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[4]")
  return element.text

def bitcoin_data(driver):
  driver.get("https://coinmarketcap.com/currencies/bitcoin/")
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div/section/div/div[2]/span")
  return element.text


def vwce_data(driver):
  driver.get("https://www.justetf.com/en/etf-profile.html?isin=IE00BK5BQT80")
  time.sleep(2)
  element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "realtime-quotes > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)"))
  )
  return element.text

def btce_data(driver):
  driver.get("https://www.justetf.com/en/etf-profile.html?isin=DE000A27Z304")
  time.sleep(2)
  element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "realtime-quotes > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)"))
  )
  return element.text

def ssln_data(driver):
  driver.get("https://www.justetf.com/en/etf-profile.html?isin=IE00B4NCWG09")
  time.sleep(2)
  element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "realtime-quotes > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)"))
  )
  return element.text

#We set the driver
driver = get_driver()

#Scraping the values we want
index_value = fear_greed_index(driver)
btc_price = bitcoin_data(driver)
vwce_price = vwce_data(driver)
btce_price = btce_data(driver)
ssln_price = ssln_data(driver)

#We clean the BTC value where we remove $ character
clean_btc_price = btc_price.replace("$","")

#Stpped the Chrome driver
driver.quit()

#We saved data to CSV file
save_to_csv(index_value,clean_btc_price,vwce_price,btce_price,ssln_price) 
print("Data saved in CSV!")

#Sending warrning if values cross settings
if int(index_value) < 25 or int(index_value) > 75:  
    send_email(index_value, clean_btc_price, vwce_price,btce_price,ssln_price)
    print("Warrning send!")

