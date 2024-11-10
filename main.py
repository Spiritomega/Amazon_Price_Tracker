import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

link = "https://www.amazon.in/LG-inches-Ultra-Smart-55UR7500PSC/dp/B0BFCCRPVM/ref=sr_1_1_sspa?crid=3UOQQ9DZXD6Y3&dib=eyJ2IjoiMSJ9.k8w7wp2UmfCIPN0JzI3JhiPS2QYZSrWGGrJZuyGfOcd5OAvboZXjJPumNnECLwX8vxcl80Tz3DpLFiDEm68YgS5sZiE3X94FegB5QgrEnp2AMNyQPCH7sIgo0UilOit13-RmkrqO7LbC2earspJDYtLhXqKhZQlyNdSkyPQ2Wf6z6krejeFuJKGosx8XZLIMJ2PzDd2nmut5Ob0Tlrcybw8-6NiW4VqtL7w3aFA_oUo.51cDzsibqYKFKfUdfGXaTsrQfDVPR90lwZDW5jrRArw&dib_tag=se&keywords=led%2Btv%2B55%2Binch&qid=1717568607&sprefix=led%2Btv%2B55%2Caps%2C185&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

header = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"

}

response = requests.get(url=link, headers=header)
response.raise_for_status()
content = response.content

soup = BeautifulSoup(content, "lxml")
title = soup.find("span", attrs={"id": "productTitle"})
print(title.getText().strip())
product_title = soup.find(class_="a-size-large product-title-word-break").getText().strip()
current_price = soup.find(class_="a-price-whole").getText()


current_price_amt = current_price.replace(",", "").replace(".", "")

buy_price = 44000

print(current_price_amt)

my_email = "itsme.adityachainani@gmail.com"
password = "xkga ncsf grax oncx "

if float(current_price_amt) <= buy_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Low price alert\n\nHeyyy,\n{product_title} is now available for {current_price_amt}. Best time to buy it is now!!!\n\nWarm Regards,\nAditya")
