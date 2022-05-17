import smtplib
import time 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
def sendmail():  
  n = int(input("Enter the number of emails you want to send: ")) 
  mail_content = ''
  sender_address = ""
  sender_pass = ''
  receiver_address = input("Enter the receiver's email address: ")
  print('sending mail to ' + receiver_address) 
  for i in range(n):
    mail_content = 'have fun' 
    sender_address = ""
    sender_pass = ''
    print('sending mail to ' + receiver_address)
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = ''   
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp server of the sender', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string() 
    session.sendmail(sender_address, receiver_address, text) 
    session.quit() 