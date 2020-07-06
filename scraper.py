import requests
import smtplib
import time

from bs4 import BeautifulSoup

URL= "https://www.amazon.in/Rockerz-610-Bluetooth-Headphone-Earcushions/dp/B086C79DFJ/ref=sr_1_2_sspa?dchild=1&fst=as%3Aoff&qid=1594039529&refinements=p_n_feature_six_browse-bin%3A15564048031&rnid=15564019031&s=electronics&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOTk5V0pXTVVOSTdDJmVuY3J5cHRlZElkPUEwMTc5NjAzMUJKVkY2NDdWN1RBWSZlbmNyeXB0ZWRBZElkPUEwOTcxMTYwMVE5QzFVTlIzUDRJRCZ3aWRnZXROYW1lPXNwX2F0Zl9icm93c2UmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

page=requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

soup.encode('utf-8')

title=soup.find(id="title-feature-div")

# print(soup.prettify())

# function to check if the price has dropped below 1300
def check_price():
  title = soup.find(id= "productTitle").get_text()
  price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
  #print(price)

  #converting the string amount to float
  converted_price = float(price[0:4])
  print(converted_price)
  if(converted_price <= 9999):
    send_mail()

  #using strip to remove extra spaces in the title
  print(title.strip())



# function that sends an email if the prices fell down
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('email@gmail.com', 'password')

  subject = 'Price Fell Down'
  body = "https://www.amazon.in/Rockerz-610-Bluetooth-Headphone-Earcushions/dp/B086C79DFJ/ref=sr_1_2_sspa?dchild=1&fst=as%3Aoff&qid=1594039529&refinements=p_n_feature_six_browse-bin%3A15564048031&rnid=15564019031&s=electronics&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOTk5V0pXTVVOSTdDJmVuY3J5cHRlZElkPUEwMTc5NjAzMUJKVkY2NDdWN1RBWSZlbmNyeXB0ZWRBZElkPUEwOTcxMTYwMVE5QzFVTlIzUDRJRCZ3aWRnZXROYW1lPXNwX2F0Zl9icm93c2UmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

  msg = f"Subject: {subject}\n\n{body}"
  
  server.sendmail(
    'sender@gmail.com',
    'receiver@gmail.com',
    msg
  )
  #print a message to check if the email has been sent
  print('Hey Email has been sent')
  # quit the server
  server.quit()

#loop that allows the program to regularly check for prices
while(True):
  check_price()
  time.sleep(60 * 60)







# ***********************************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************************
# Amazon product price tracker using Python 

# importing libraries 
# import requests
# from bs4 import BeautifulSoup
# import smtplib
# import time

# # set the headers and user string
# headers = {
# "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
# }

# # send a request to fetch HTML of the page
# response = requests.get('https://www.amazon.in/Bose-SoundLink-Wireless-Around-Ear-Headphones/dp/B0117RGG8E/ref=sr_1_11?qid=1562395272&refinements=p_89%3ABose&s=electronics&sr=1-11', headers=headers)

# # create the soup object
# soup = BeautifulSoup(response.content, 'html.parser')

# # change the encoding to utf-8
# soup.encode('utf-8')

# #print(soup.prettify())

# function to check if the price has dropped below 20,000
# def check_price():
#   title = soup.find(id= "productTitle").get_text()
#   price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
#   #print(price)

#   #converting the string amount to float
#   converted_price = float(price[0:5])
#   print(converted_price)
#   if(converted_price < 20000):
#     send_mail()

#   #using strip to remove extra spaces in the title
#   print(title.strip())





# # function that sends an email if the prices fell down
# def send_mail():
#   server = smtplib.SMTP('smtp.gmail.com', 587)
#   server.ehlo()
#   server.starttls()
#   server.ehlo()

#   server.login('email@gmail.com', 'password')

#   subject = 'Price Fell Down'
#   body = "Check the amazon link https://www.amazon.in/Bose-SoundLink-Wireless-Around-Ear-Headphones/dp/B0117RGG8E/ref=sr_1_11?qid=1562395272&refinements=p_89%3ABose&s=electronics&sr=1-11 "

#   msg = f"Subject: {subject}\n\n{body}"
  
#   server.sendmail(
#     'sender@gmail.com',
#     'receiver@gmail.com',
#     msg
#   )
#   #print a message to check if the email has been sent
#   print('Hey Email has been sent')
#   # quit the server
#   server.quit()

# #loop that allows the program to regularly check for prices
# while(True):
#   check_price()
#   time.sleep(60 * 60)