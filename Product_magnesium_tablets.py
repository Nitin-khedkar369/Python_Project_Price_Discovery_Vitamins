import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

URL = "https://www.amazon.in/Carbamide-Forte-Magnesium-Glycinate-Supplement/dp/B08F7MDDSH/ref=sr_1_7?crid=" \
      "1WI2G6I0S4F3T&keywords=magnesium+glycinate+supplement&qid=1688967797&sprefix=magnesium%2Caps%2C448&sr=8-7"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "114.0.0.0 Safari/537.36 Edg/114.0.1823.67",
    "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8",
}


response = requests.get(URL, headers=header)
response.raise_for_status()

website_link = response.text

soup = BeautifulSoup(website_link, "lxml")

price = soup.find(class_="a-offscreen").get_text()

price_without_currency = price.split("₹")[1]

price_as_float = float(price_without_currency)

print(f"Current Price is :{price_as_float}".strip(".0"))

title = soup.find(id="productTitle").get_text().strip()
# print(title)

# put this price 253
BUY_PRICE = 254
print(f"By at this:{BUY_PRICE}")

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    # Put your email,pass,smtp address for eg:-Gmail: smtp.gmail.com, Hotmail: smtp.live.com, Outlook: outlook.office365.com,
    # Yahoo: smtp.mail.yahoo.com

    SMTP_ADDRESS = "smtp.gmail.com"
    EMAIL = "nkmercurial10@gmail.com"
    PASSWORD = "xjghncthrehqyjyd"
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )