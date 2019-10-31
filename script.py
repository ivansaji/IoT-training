import time
import smtplib
from email.mime.multipart import MIMEMultipart

gmail_user = "abcd@gmail.com"   #Enter the user email ID
gmail_pwd = "your passwd"       #Enter the User Password
TO = ['1234@gmail.com']     # must be a list (Recepient mail)
msg = MIMEMultipart()
time.sleep(1)
msg['Subject'] = 'testing msg send from python'
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