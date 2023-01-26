import requests
import os
import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup
# from pprint import pprint

url= "https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=pd_rhf_d_gw_s_pd_sbs_rvi_sccl_1_1/147-5914447-0493019?pd_rd_w=IbxKi&content-id=amzn1.sym.a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_p=a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_r=2SBWXA58SKSHRRAZ6DY5&pd_rd_wg=UWkaZ&pd_rd_r=55be899e-2b35-469a-aaca-7c9035bd96e0&pd_rd_i=B06Y1MP2PY&th=1"
headers = {'Accept-Language' : os.getenv("HTTP_HEADER_USER_AGENT"),
            'User-Agent': os.getenv("HTTP_HEADER_ACCEPT_LANG"),
            } 

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
price = float(soup.find(class_="a-offscreen").get_text().split("$")[1])
item = soup.find(id="productTitle").get_text().strip()

target_price = 200

MY_EMAIL = os.environ.get('TEST_GMAIL')
MY_PASSWORD = os.environ.get('TEST_GMAIL_PASSWORD')

if price <= target_price:
    mail_content = f"""{item} is now {price}. 
    Shop now at {url}"""

    print(mail_content)
    
    msg = EmailMessage()
    msg['Subject'] = 'Amazon Price Alert!'
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL
    msg.set_content(mail_content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        try:
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.send_message(msg)
            print(f"Successfully sent mail! Check!")
        except smtplib.SMTPConnectError:
            print(f"Hmmn. Something went wrong.")
