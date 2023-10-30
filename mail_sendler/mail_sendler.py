import os
import re
import ssl
import smtplib
from email.message import EmailMessage

class MailProperties:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    def __init__(self):
        self.mail_properties(self.regex)

    def mail_properties(self, regex):

        # mail validation
        while True:
            mail = input('Write mail to send: ')

            if not re.fullmatch(regex, mail):
                print('Enter the valid emai')
                continue

            self.to = mail
            subject = input('Write a subject: ')
            body = input('Write a body: ')

            self.subject = subject
            self.body = body
            break

class MailSend:
    email_sender = 'samvelavagyan91@gmail.com'

    # add key after two-factor auth for send email
    key = os.environ.get('MAIL_KEY')

    def __init__(self):
        mail_properties = MailProperties()
        self.mail_send(mail_properties, self.email_sender)

    def mail_send(self, mail_properties, email_sender):
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = mail_properties.to
        em['Subject'] = mail_properties.subject
        body = mail_properties.body
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, self.key)
            smtp.sendmail(email_sender, mail_properties.to, em.as_string())
