from phisingProtection import getReputation, reportEmail
from receive import fetch_emails, sort
from list_folders import list_folders
from send import send_email
from user import scanUserList, addUser, rmUser
from user import credential, setting
from hash import decrypt, encrypt
from joke import joke
import json

# Steps to communicate with backend
# 1) Start by trying to log in
# 2) if fail create an account
# 3) if success for (1) then set the site settings from the returned settings
# 4) get all the emails using getEmails for each credential returned
# 5) sort emails using sortEmails command when needed
# 6) send emails using sendEmails command when needed
# 7) check for malicious email account using checkAccount
# 8) report malicious email accounts using reportAccount
# 9) remove a user from the site totally by deleteAccount

class email:
    def __init__(self, fromAccount, toAccount, subject, message, tags):
        self.fromAccount = fromAccount
        self.toAccount = toAccount
        self.subject = subject
        self.message = message
        self.tags = tags

def login(username, password):
    userInfo = scanUserList(username, password)
    if (userInfo[0] != ("Error: 1" or "Error: 2")):
        decodedCredentials = []
        for item in userInfo[1][0]:
            decodedUser = decrypt(item.username.encode()).decode()
            decodedPass = decrypt(item.password.encode()).decode()
            decodedCredentials.append(credential(decodedUser, decodedPass))
        return [decodedCredentials, userInfo[1][1]]
    else:
        return userInfo[0]

def createAccount(username, password, emailAccounts, emailPasswords, settingsList, settingsValues):
    try:
        addUser(username, password, emailAccounts,
            emailPasswords, settingsList, settingsValues)
        return "User successfully created."
    
    except:
        return "Error creating user."

def deleteAccount(username, password):
    return rmUser(username, password)

def updateAccount(operation, username, password, eUsers=None, ePass=None, settings=None, settingVals=None):
    # Variables
    #   operation = "add" or "sub"
    #   username = account username
    #   password = account password
    #   eUsers = List of usernames
    #   ePass = List of passwords len = len(new_eUser)
    #   settings = List of settings
    #   settingVals = List of setting values
    #
    # When operation = "add"
    #   The user account, determined by the input username
    #   and password, is updated with the list of new email
    #   accounts and settings added.
    # 
    # When operation = "sub"
    #   The user account is updated with the list of email
    #   accounts and settings removed.
    #  

    """Get the users current info"""
    userInfo = scanUserList(username, password)

    """Check if the user is found"""
    if (userInfo[0] == "Success"):

        """Generating the new user info when operation = add"""
        if (operation == "add"):
            new_eUsers = []
            new_ePass = []
            new_settings = []
            new_settingVals = []

            for item in eUsers:
                new_eUsers.append(item)
            for item in ePass:
                new_ePass.append(item)
            for item in settings:
                new_settings.append(item)
            for item in settingVals:
                new_settingVals.append(item)

            """Generating the new credentials"""
            for item in userInfo[1][0]:
                new_eUsers.append(decrypt(item.username.encode()).decode())
                new_ePass.append(decrypt(item.password.encode()).decode())

            """Generating the new settings"""
            for item in userInfo[1][1]:
                new_settings.append(item.name)
                new_settingVals.append(item.value)

            deleteAccount(username, password)
            createAccount(username, password, new_eUsers, new_ePass, new_settings, new_settingVals)

        elif (operation == "sub"):
            rm_eUsers = []
            rm_ePass = []
            rm_settings = []
            rm_settingVals = []

            """Generating the new credentials"""
            rm = False
            for item in userInfo[1][0]:
                for i in eUsers:
                    if (i == decrypt(item.username.encode()).decode()):
                        rm = True
                if (not(rm)):
                    rm_eUsers.append(decrypt(item.username.encode()).decode())
                    rm_ePass.append(decrypt(item.password.encode()).decode())
            
            """Generating the new settings"""
            rm = False
            for item in userInfo[1][1]:
                for i in settings:
                    if (i == item.name):
                        rm = True
                if (not(rm)):
                    rm_settings.append(item.name)
                    rm_settingVals.append(item.value)

            deleteAccount(username, password)
            createAccount(username, password, rm_eUsers, rm_ePass, rm_settings, rm_settingVals)

        else:
            return "Invalid operation"
    
    else:
        return "Error: 1"

def getSettings(username, password):
	userInfo = scanUserList(username, password)
	
	res = '['
	
	if (userInfo[0] == "Success"):
		for item in userInfo[1][0]:
			res += '[\"' + decrypt(item.username.encode()).decode() + '\", \"' + decrypt(item.password.encode()).decode() + '\"]'
	
	res += ']'
	
	return json.dumps(res)

# get the first number emails from each address
def getEmailsInbox(username, password, number):
	userInfo = scanUserList(username, password)
	
	# emails is just a list of emails... should be converted to json just fine
	emails = [] #'[{"name": ["bob", "joe"]}]'
	
	if (userInfo[0] == "Success"):
		for item in userInfo[1][0]:
			emails.append(getEmails(decrypt(item.username.encode()).decode(), decrypt(item.password.encode()).decode(), 'Inbox'))
	
	return json.dumps(str(emails))

def getEmails(account, password, folder, sortType=None):
    emails = []

    copy = False
    server = ""
    for letter in account:
        if (letter == "."):
            copy = False
        if (copy):
            server += letter
        if (letter == '@'):
            copy = True

    if (server == "gmail"):
        server = 'imap.gmail.com'
    elif (server == "yahoo"):
        server = 'imap.mail.yahoo.com'
    elif (server == "hotmail" or "outlook"):
        server = 'imap-mail.outlook.com'
    elif (server == "verizon"):
        server = 'incoming.verizon.net'
    elif (server == "comcast"):
        server = 'imap.comcast.net'
    elif (server == "att"):
        server = 'imap.mail.att.net'

    if (sortType == None):
        newEmails = fetch_emails(account, password, server, folder, 0, "", -1)
    else:
        newEmails = fetch_emails(account, password, server, folder, 1, sortType, -1)

        tags = []
        tags.append(folder)
        for item in newEmails:
            emails.append(email(item[0], item[1], item[2], item[3], tags))
    
    return emails

def getFolders(account, password):
    copy = False
    server = ""
    for letter in account:
        if (letter == "."):
            copy = False
        if (copy):
            server += letter
        if (letter == '@'):
            copy = True

    if (server == "gmail"):
        server = 'imap.gmail.com'
    elif (server == "yahoo"):
        server = 'imap.mail.yahoo.com'
    elif (server == "hotmail" or "outlook"):
        server = 'imap-mail.outlook.com'
    elif (server == "verizon"):
        server = 'incoming.verizon.net'
    elif (server == "comcast"):
        server = 'imap.comcast.net'
    elif (server == "att"):
        server = 'imap.mail.att.net'

    return list_folders(account, password, server)

def sendEmail(from_email, from_password, to_email, subject, message):
    copy = False
    server = ""
    for letter in from_email:
        if (letter == "."):
            copy = False
        if (copy):
            server += letter
        if (letter == '@'):
            copy = True

    port = 587
    if (server == "gmail"):
        server = 'imap.gmail.com'
    elif (server == "yahoo"):
        server = 'imap.mail.yahoo.com'
    elif (server == "hotmail" or "outlook"):
        server = 'imap-mail.outlook.com'
    elif (server == "verizon"):
        server = 'incoming.verizon.net'
        port = 465
    elif (server == "comcast"):
        server = 'imap.comcast.net'
    elif (server == "att"):
        server = 'imap.mail.att.net'

    send_email(from_email, from_password, server, port, to_email, subject, message)

def sortEmails(emails, sortType):
    emailArray = []
    for item in emails:
        newEmail = [
            item.fromAccount,
            item.toAccount,
            item.subject,
            item.message
        ]
        emailArray.append(newEmail)
    sortedArray = sort(emailArray, sortType)

    tmpEmailArray = []
    emailArray = []
    for item in sortedArray:
        tmpEmailArray.append(email(
            item[0],
            item[1],
            item[2],
            item[3],
            []
        ))
    for item in tmpEmailArray:
        emailArray.append(item)
    return emailArray

def checkAccount(account):
    return getReputation(account)

def reportAccount(account, reason, text=None):
    if (text == None):
        return reportEmail(account, reason)
    else:
        return reportEmail(account, reason, text)

def getJoke(category):
    return joke(category)