# 🧠 Fear & Greed Index Tracker

This project was created as part of a home education initiative with the goal of learning how financial sentiment (fear & greed) affects market behavior. The project tracks the **Fear & Greed Index** alongside key financial assets such as **Bitcoin**, **VWCE**, **BTCE**, and **SSLN** prices, and logs them for further analysis. When extreme values are detected, it sends a **warning email** to the user.

## 💡 Key Features

- ✅ Automatically scrapes:
  - CNN Fear & Greed Index
  - Bitcoin price (from CoinMarketCap)
  - VWCE, BTCE, and SSLN ETF prices (from JustETF)
- ✅ Saves data to a CSV file
- ✅ Sends email alerts when index is below 25 (fear) or above 75 (greed)

## 🛠️ Technologies Used

- **Python**
- **Selenium** for browser automation and scraping
- **smtplib** for sending email notifications
- **CSV** for data storage
- **Chrome WebDriver** (Headed browser)

## 🧩 Project Structure

- `get_driver()` – Sets up and returns a Selenium Chrome WebDriver with custom options.
- `fear_greed_index()` – Scrapes the CNN index.
- `bitcoin_data()` – Gets the current BTC price.
- `vwce_data()`, `btce_data()`, `ssln_data()` – Scrape ETF prices from JustETF.
- `save_to_csv()` – Saves all data points into `fear_greed_index.csv`.
- `send_email()` – Sends an email warning when index is < 25 or > 75.

## ⚙️ How to Use

### 1. Clone the Repository

```
git clone https://github.com/your-username/fear-greed-tracker.git
cd fear-greed-tracker
```
### 2. Install Dependencies
Make sure you have Python and Chrome installed.

Install required Python libraries:
```
pip install selenium
```
Note: You need to have Chrome WebDriver installed and added to your system's PATH.

### 3. Setup Email Credentials
In the scrap_index_vlaue.py file, locate the **send_email()** function and replace the following placeholders:

```
sender_email = "your-email@gmail.com"  # Your Gmail address
receiver_email = "receiver@gmail.com"  # Who will receive alerts
password = "your-app-password"         # Use a Gmail app password (not your login password)
```
Note: You must enable 2FA on your Google account and generate an App Password for this to work.

### 4. Run the Script
```
python scrap_index_vlaue.py
```

- This will launch Chrome, scrape the data, save it to a .csv file, and send an alert if needed.
- Output data is saved to fear_greed_index.csv.

