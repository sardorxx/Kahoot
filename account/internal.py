import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(email, message_user) -> None:
    sender_email = "kahoot.pdp.org@mail.ru"
    sender_password = "ecAcQpAWVm3u7s1NRW5F"
    recipient_email = f'{email}'
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Confirmation email for PDP Kahoot'
    body = f'{message_user}'
    message.attach(MIMEText(body, 'plain'))
    session = smtplib.SMTP('smtp.mail.ru', 587)
    session.starttls()
    session.login(sender_email, sender_password)
    text = message.as_string()
    session.sendmail(sender_email, recipient_email, text)
    session.quit()
