import requests
from bs4 import BeautifulSoup
from blahblah import get_secrets

FILE = "C:/Users/yaseen/secrets/mail.txt"
URL = "https://www.amazon.in/Faddish-Anti-glare-Spectacle-Bluelight-HOOP/dp/B08J3VL7M6?pd_rd_w=BMgtc&pf_rd_p=218e88e6" \
      "-02df-4531-b5e1-61aaeb78a7f5&pf_rd_r=HBE02VY2FWXCNST3BNYQ&pd_rd_r=ab816c76-806b-47a0-b1b1-583ac806bd8f" \
      "&pd_rd_wg=RchCu&pd_rd_i=B08J3VL7M6&psc=1&ref_=pd_bap_d_rp_8_t "
BUY_PRICE = 900
HEADERS = {
    "User-Agent": "Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
SMTP_ADDRESS = "smtp.gmail.com"
EMAIL_ID = get_secrets().get("mail")["email_id"]
EMAIL_PASSWORD = get_secrets().get("mail")["email_password"]


def send_mail(email, password):
    import smtplib
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Amazon Price Alert!\n\n{product_title}\n{URL}\n"
                f"Current Price : ₹{product_price}".encode('utf-8')    # utf encode is required for rupees symbol
        )


response = requests.get(url=URL, headers=HEADERS)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
# [1::] is to remove "rupees" symbol
product_price = round(float(soup.find(id="priceblock_ourprice").text[1::]))
product_title = soup.find(id="productTitle").text.strip()
if product_price <= BUY_PRICE:
    send_mail(EMAIL_ID, EMAIL_PASSWORD)