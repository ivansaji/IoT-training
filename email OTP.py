# To use this module.... provide access to less secure apps in account manager

import time
import random
import smtplib          #mail protocol client
from email.mime.multipart import MIMEMultipart      #Import modules for using mail servers

gmail_user = "abcd@gmail.com"   #Enter the user email ID
gmail_pwd = "your passwd"       #Enter the User Password
TO = ['1234@gmail.com']     # must be a list (Recepient mail)
msg = MIMEMultipart()
time.sleep(1)
otp = 'Your OTP is  ' + str(random.randint(10000,99999))
msg['Subject'] = otp
try:
    server = smtplib.SMTP("smtp.gmail.com",587)
    print("SMTP Success")
    server.ehlo()
    print("EHLO Success")
    server.starttls()
    print("TLS Success")
    server.login(gmail_user,gmail_pwd)
    print("Login Success")
    server.sendmail(gmail_user,TO,msg.as_string())
    print("sending.....")
    server.close()
    print("successfully send mail....")
except:
    print("Some Error")

user_otp = input("Enter your OTP send to "+ TO)
if user_otp == otp:
    print("OTP Accepted")
else:
    print("Invalid OTP")