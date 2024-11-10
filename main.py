# Import required libraries
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

# 1. Set the Amazon product link you want to track
link = "https://www.amazon.in/Apple-iPhone-Pro-Max-256/dp/B0DGHYPFYB/ref=sr_1_2?crid=3KVVW0X3S43XZ&dib=eyJ2IjoiMSJ9.avR4APTs5mH0MB0YNHm94GF-OlZSpO8X0ApR72OjT4WUDJd6x92MGt5oUhVvUOeyDmkhI6nOG0NtSan28UGrfZU52Ct3SCUMXQcVqHdIPZapL_fIn1Lrwt3h7mctEuVGBN_QyZ42yUONQUKG9jk2J-BoJ9-sBIaNHrploVDwyEKEvhMKGubnPqCFhceOL4mnxcu3qb1gBsDYn2sTdFEZeu740BZ6t6R23tjgLvnUr0I.gxK6UY0uWVa2HOH-xe_KWTw8H4oSdZjv4Cvh65DKNTE&dib_tag=se&keywords=iphone+16+pro+max+256gb&qid=1731222626&sprefix=iphone%2Caps%2C190&sr=8-2"
# Make sure to replace the link with the product you want to track

# 2. Define headers for the request to Amazon (use a valid User-Agent string)
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# 3. Fetch the product page content from Amazon
response = requests.get(url=link, headers=header)
response.raise_for_status()  # Check if the request was successful
content = response.content  # Get the page content

# 4. Parse the page content with BeautifulSoup
soup = BeautifulSoup(content, "lxml")

# 5. Find the product title
title = soup.find("span", attrs={"id": "productTitle"})
print(title.getText().strip())  # Print the title to check if it was fetched correctly
product_title = title.getText().strip()

# 6. Find the current price of the product
current_price = soup.find(class_="a-price-whole").getText()
# Remove commas and periods to convert price to a usable number format
current_price_amt = current_price.replace(",", "").replace(".", "")

# 7. Define your target price (price at which you want to receive an alert)
buy_price = 44000  # Set your desired purchase price

# Print the current price for verification
print(f"Current price: {current_price_amt}")

# 8. Set up email credentials
my_email = "itsme.adityachainani@gmail.com"  # Your email address
password = "xkga ncsf grax oncx"  # Your email app password (use environment variable in production)

# 9. Check if the current price is less than or equal to your target price
if float(current_price_amt) <= buy_price:
    # 10. Send an email alert if the price is low
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Start TLS encryption
        connection.login(user=my_email, password=password)  # Log in to your email account
        # Compose the email
        message = f"Subject: Low price alert\n\nHey,\n{product_title} is now available for {current_price_amt}. Best time to buy it is now!!!\n\nWarm Regards,\nAditya"
        # Send the email to yourself
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=message)

