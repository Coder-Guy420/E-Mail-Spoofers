import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import COMMASPACE
from email import encoders

def send_email(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = COMMASPACE.join(to_addr_list)
    msg['Cc'] = COMMASPACE.join(cc_addr_list)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    smtpserver = smtplib.SMTP(smtpserver)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(login, password)
    smtpserver.sendmail(from_addr, to_addr_list, msg.as_string())
    smtpserver.quit()

from_addr = input("Enter the email address that you want to spoof: ")
to_addr_list = input("Enter the recipient email addresse(s) separated by commas: ").split(',')
cc_addr_list = input("Enter the CC email addresse(s) separated by commas: ").split(',')
subject = input("Enter the email subject: ")
message = input("Enter the email message: ")
login = input("Enter the email address you want to use: ")
password = input("Enter the password to the email address: ")

send_email(from_addr, to_addr_list, cc_addr_list, subject, message, login, password)
