"""This example shows all necessary steps for sending a basic plain text message."""

# Import the MailSender class from the sendmail module
from sendmail import MailSender

"""
Name	Server Domain Name	Port
Gmail	smtp.gmail.com	587
Outlook / Hotmail	smtp-mail.outlook.com	587
YAHOO Mail	smtp.mail.yahoo.com	587
Verizon	smtp.verizon.net	465
Comcast	smtp.comcast.net	587
AT&T	imap.mail.att.net   ???
"""


# Yahoo you must use app specific password
# Outlook/hotmail you must use app specific password

# Gmail you must turn on allow less secure apps

def send_email(from_email, from_password, outgoing_mail_server, outgoing_mail_server_port, to_email, subject, msg):
    plaintext = msg
    ourmailsender = MailSender(from_email, from_password, (outgoing_mail_server, outgoing_mail_server_port))
    ourmailsender.set_message(plaintext, subject, from_email)
    ourmailsender.set_recipients([to_email])

    ourmailsender.connect()
    ourmailsender.send_all()
