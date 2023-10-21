from email.utils import formataddr
from email.message import EmailMessage
import smtplib, ssl

msg = EmailMessage()
msg['From'] = formataddr(('Example Sender Name', 'john@example.com'))
msg['To'] = formataddr(('Example Recipient Name', 'jack@example.org'))
msg.set_content('Lorem Ipsum')

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "my@gmail.com"  # Enter your address
receiver_email = "your@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)