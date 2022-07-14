from imapclient import IMAPClient
import re


def list_folders(email, password, incoming_mail_server):
    _server = IMAPClient(incoming_mail_server, use_uid=True)
    _server.login(email, password)
    folders_unf = _server.list_folders()

    formatted_folder_array = []

    for f in folders_unf:
        f = str(f)
        # print(f)
        f = re.sub(r".*b'/', ", "", f)
        f = f[:-2]
        f = f[1:]
        formatted_folder_array.append(f)
    return formatted_folder_array

# values = list_folders("email", "password", "imap.gmail.com")
# print(values)
