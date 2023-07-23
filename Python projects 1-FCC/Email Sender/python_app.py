from email.message import EmailMessage
from app2 import password

#secure socket layer for secure connection
import ssl

#for mail service
import smtplib

email_sender ='remyacnair710@gmail.com'
email_password=password

email_receiver='lopadi7658@nasskar.com'

subject="Sample Python Mail Subject"
body="""
Sample Python Mail body
"""

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

