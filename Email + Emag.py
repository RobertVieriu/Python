import string
import requests
from bs4 import BeautifulSoup
import smtplib
from apscheduler.schedulers.blocking import BlockingScheduler
from hashlib import new
import smtplib
sender='data_scraping@coneasorin.ro'
subject='Pretul a scazut la:'
to_addr_list = ['robertva.robertva@yahoo.com']
cc_addr_list = ['']
def sendemail(sender,message, subject,to_addr_list, cc_addr_list=[]):
    try:
        smtpserver='mail.x-it.ro:26'
        header  = 'From: %s\n' % sender
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message
 
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender,"stiinte217_2022")
        problems = server.sendmail(sender, to_addr_list, message)
        server.quit()
        return True
    except:
        return False

def data_scraping() :
    req=requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-max-128gb-5g-deep-purple-mq9t3rx-a/pd/DXDY4LMBM/?cmpid=99160&gclid=CjwKCAjw7p6aBhBiEiwA83fGutQEzd8jTFRrgGNgq-64rJSekVI_-HBUv2ljRnybUWvX7Ny_Rzh68hoClScQAvD_BwE")
    soup=BeautifulSoup(req.text,"html.parser")
    price=soup.find('p', attrs={'class': 'product-new-price'}).text
    new_price=price[0:5]
    new_price=new_price.replace(".","")
    new_price=int(new_price)
    pret_referinta = 7069
    if(new_price<pret_referinta):
        sendemail( sender, "dada" +str(new_price), subject, to_addr_list, cc_addr_list=[])
        print("pretul a scazut")
    else:
        print("pretul nu a scazut")


sendemail(sender, "Nice", subject, to_addr_list, cc_addr_list)
data_scraping()