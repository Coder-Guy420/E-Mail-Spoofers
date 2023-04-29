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

send_email('spoofedemail@gmail.com', ['recipient1@example.com', 'recipient2@example.com'], [],
           'This is a spoofed email', 'Hello, this email was sent from a fake address!', 
           'yourlogin@gmail.com', 'yourpassword')
