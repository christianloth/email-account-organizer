# Importing libraries
import imaplib
import numpy

# must have the allow less secure apps turned on in gmail
# password must me app specific for yahoo

# Yahoo you must use app specific password
# Outlook/hotmail you must use app specific password

# Gmail you must turn on allow less secure apps

"""
Provider	Domain Name for IMAP Server
Gmail  : imap.gmail.com
YAHOO	imap.mail.yahoo.com
Hotmail/Outlook	imap-mail.outlook.com
Verizon	incoming.verizon.net
Comcast	imap.comcast.net
AT&T	imap.mail.att.net
"""


# Function to get email content part i.e its body part
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)


# Function to search for a key value pair
def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data


def transpose(matA, matB):
    matB = [[row[i] for row in matA] for i in range(len(matA[0]))]
    return matB

# this is the function that receives the emails. it stores them in a 2d array
def fetch_emails(email, password, incoming_mail_server, folder, sort_bool, sort_string, num_emails_to_fetch):
    # declare arrays like from, to, etc.
    from_addr_array = []
    to_addr_array = []
    subject_header_array = []
    msg_array = []

    # this is done to make SSL connnection
    mail = imaplib.IMAP4_SSL(incoming_mail_server)

    # logging the user in
    mail.login(email, password)

    # calling function to check for email under this label
    mail.select(folder)
    type_param, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()

    num_emails_in_folder = data[0].split()

    i = 0
    for num in data[0].split():
        if i >= num_emails_to_fetch and num_emails_to_fetch != -1:
            break
        typ, data = mail.fetch(num, '(RFC822)')
        raw_email = data[0][1]
        # converts byte literal to string removing b''
        raw_email_string = raw_email.decode('utf-8')

        import email
        email_message_encoded = email.message_from_string(raw_email_string)

        from_addr = email_message_encoded["From"]
        to_addr = email_message_encoded["To"]
        subject_header = email_message_encoded["Subject"]
        msg = get_body(email_message_encoded)

        from_addr_array.append(from_addr)
        to_addr_array.append(to_addr)
        subject_header_array.append(subject_header)
        msg_array.append(msg)
        i = i + 1

    l1 = [from_addr_array, to_addr_array, subject_header_array, msg_array]
    l2 = []

    # transpose matrix to make it the way i want it
    final_mat = transpose(l1, l2)

    if sort_bool == 0:
        return final_mat
    elif sort_bool > 0:
        return sort(final_mat, sort_string)



# returns email 2D array sorted in whichever fashion specified
def sort(mat, sort_string):
    # sort strings: subject, from, to

    return_arr = mat

    if sort_string == 'from':
        for i in range(0, len(return_arr) - 1):
            if return_arr[i + 1][0] < return_arr[i][0]:
                temp = return_arr[i + 1]
                return_arr[i + 1] = return_arr[i]
                return_arr[i] = temp

    elif sort_string == 'to':
        for i in range(0, len(return_arr) - 1):
            if return_arr[i + 1][1] < return_arr[i][1]:
                temp = return_arr[i + 1]
                return_arr[i + 1] = return_arr[i]
                return_arr[i] = temp

    elif sort_string == 'subject':
        for i in range(0, len(return_arr) - 1):
            if return_arr[i + 1][2] < return_arr[i][2]:
                temp = return_arr[i + 1]
                return_arr[i + 1] = return_arr[i]
                return_arr[i] = temp

    elif sort_string == 'msg':
        for i in range(0, len(return_arr) - 1):
            if return_arr[i + 1][3] < return_arr[i][3]:
                temp = return_arr[i + 1]
                return_arr[i + 1] = return_arr[i]
                return_arr[i] = temp

    return return_arr

#values = fetch_emails('email', 'password', 'imap.gmail.com', 'Inbox', 1, "msg", -1)
#print(len(values))
#print(values[1][2])
#print(values[2][2])
#print(values[3][2])
