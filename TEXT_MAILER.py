import csv
import smtplib
import re
import os
from smtplib import SMTPException
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

img_data = open('ATTACHMENT FILE', 'rb').read()
msg = MIMEMultipart()
msg['Subject'] = 'MAIL_SUBJECT'   # SUBJECT
msg['From'] = 'SENDER_EMAIL'
html = """\
<html>
  <head></head>
  <body>
    <p>
    BODY_CONTENT
    </p>
  </body>
</html>
"""
txt = MIMEText(html, 'html')
msg.attach(txt)
image = MIMEImage(img_data, name=os.path.basename('ATTACHMENT_IMAGE'))

msg.attach(image)

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('SENDER_EMAIL', 'SENDER_PASSWORD')
email_data = csv.reader(open('DATA_FILE', 'r'))
email_pattern = re.compile("^.+@.+\..+$")
for row in email_data:
    if(email_pattern.search(row[1])):
        del msg['To']
        msg['To'] = row[1]
        try:
            server.sendmail('SENDER_EMAIL', [row[1]], msg.as_string())
        except SMTPException:
            print("An error occured.")
server.quit()
