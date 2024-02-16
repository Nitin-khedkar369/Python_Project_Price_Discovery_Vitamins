import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.in/MELTVIT-Chewable-Vitamin-2000-Cholecalciferol/dp/B09ND54W7M/ref=sr_1_20?keywords=vitamin+" \
      "d3&qid=1688967215&sprefix=vitamin+d%2Caps%2C232&sr=8-20"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                  "Safari/537.36 Edg/114.0.1823.67",

    "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8"
}

response = requests.get(URL, headers=header)
website_link = response.text

soup = BeautifulSoup(website_link, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1]
price_as_float = float(price_without_currency)
print(f"Current Price of vitamin D3: {price_as_float}")

title = soup.find(id="productTitle").get_text().strip()
# print(title)

BUY_PRICE = 326
print(f"By at this: {BUY_PRICE}")

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

#Put your email,pass,smtp address for eg:-Gmail: smtp.gmail.com, Hotmail: smtp.live.com, Outlook: outlook.office365.com,
    # Yahoo: smtp.mail.yahoo.com
    YOUR_SMTP_ADDRESS = "smtp.gmail.com"
    YOUR_EMAIL = "nkmercurial10@gmail.com"
    YOUR_PASSWORD = "utqfuvkgyoivunnq"
    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )

