# Team-35

### Sending Emails

The function to send an email in the `send.py` file is called `send_email`. It can be used with the parameters below:

```python
# send email with parameters
def send_email(from_email, from_password, outgoing_mail_server, outgoing_mail_server_port, to_email, subject, msg)
```

Outgoing Mail servers

Name	Server Domain Name	Port

Gmail	smtp.gmail.com	587

Outlook / Hotmail	smtp-mail.outlook.com	587

YAHOO Mail	smtp.mail.yahoo.com	587

Verizon	smtp.verizon.net	465

Comcast	smtp.comcast.net	587






### Fetching Emails

The function to receive an email in the `receive.py` file is called `fetch_emails`. It can be used with the parameters below:

```python

# sort_string can equal 'from', 'to', 'subject', 'msg'
# put -1 for num_emails_to_fetch if you want to fetch all emails!!
# this is the function that receives the emails. it stores them in a 2d array
def fetch_emails(email, password, incoming_mail_server, folder, sort_bool, sort_string, num_emails_to_fetch)



# returns email 2D array sorted in whichever fashion specified
"""
Note: to avoid having to re-auth with the email server each time you want to sort and pull
new data (no need since the data is already loaded), just call this sort function and pass in
your 2D email object to it and it'll return a sorted 2D email array itself!
"""
def sort(mat, sort_string)
```

Incoming Mail Servers

Gmail: imap.gmail.com

YAHOO:	imap.mail.yahoo.com

Hotmail/Outlook:	imap-mail.outlook.com

Verizon:	incoming.verizon.net

Comcast:	imap.comcast.net

AT&T:	imap.mail.att.net


###Note:
For a lot of these services, you must either use an app-specific password or turn on the "less secure apps" setting in your email.