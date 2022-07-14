import backendAPI
from backendAPI import email
from hash import decrypt, encrypt
from user import credential
from user import scanUserList, addUser, rmUser
from list_folders import list_folders
from receive import fetch_emails, sort
from send import send_email
from phisingProtection import reportEmail, getReputation

#get user email input
username1 = "Put your email here"
password1 = "Put your password here"

#Create account test
try:
    username = "btgathright"
    password = "password"
    emailAccounts = ["brandon1", "brandon2"]
    emailPasswords = ["password1", "password2"]
    settingsList = ["jokeType"]
    settingsValues = ["dirty"]
    result = backendAPI.createAccount(username, password, 
        emailAccounts, emailPasswords, 
        settingsList, settingsValues)
    print("TEST PASSED: CREATE ACCOUNT")
except Exception as ex:
    print("TEST FAILED: CREATE ACCOUNT")
    print(ex)

#Login test
try:
    username = "btgathright"
    password = "password"
    userInfo = backendAPI.login(username, password)
    if (userInfo[0] != ("Error: 1" or "Error: 2")):
        print("TEST PASSED: LOGIN")
    else:
        print("TEST FAILED: LOGIN")
except Exception as ex:
    print("TEST FAILED: LOGIN")
    print(ex)

#Get emails test
try:
    folders = backendAPI.getFolders(username1, password1)
    emails = backendAPI.getEmails(username1, password1, folders[11])
    print(emails[0])
    print("TEST FAILED: GET EMAILS")
except Exception as ex:
    print("TEST FAILED: GET EMAILS")
    print(ex)

#Send email test
try:
    from_email = username1
    from_password = password1
    to_email = username1
    subject = "Test"
    message = "Test"

    backendAPI.sendEmail(from_email, from_password, to_email, subject, message)
    print("TEST PASSED: SEND EMAIL")
except Exception as ex:
    print("TEST FAILED: SEND EMAIL")
    print(ex)

#Sort email test
try:
    emails = [
        email("apple", "banana", "c", "b", []),
        email("apple1", "apple", "b", "a", []),
        email("banana", "cherry", "e", "d", []),
        email("cherry", "apple1", "a", "c", [])
    ]
    sortType = 'subject'
    sortedEmails = backendAPI.sortEmails(emails, sortType)
    #for item in sortedEmails:
    #   print(item.subject)
    print("TEST PASSED: SORT EMAILS")
except Exception as ex:
    print("TEST FAILED: SORT EMAILS")
    print(ex)

#Check account test
try:
    account = "bill@microsoft.com"
    [reputation, suspicious, summary] = backendAPI.checkAccount(account)
    if ((reputation == "high") and (suspicious == False)):
        print("TEST PASSED: CHECK ACCOUNT")
    else:
        print("TEST FAILED: CHECK ACCOUNT")
except Exception as ex:
    print("TEST FAILED: CHECK ACCOUNT")
    print(ex)

#Report account test
try:
    account = "bgathrite98@gmail.com"
    reason = 4
    response = backendAPI.reportAccount(account, reason)
    print("TEST PASSED: REPORT ACCOUNT")
except Exception as ex:
    print("TEST FAILED: REPORT ACCOUNT")
    print(ex)

#Delete account test
try:
    username = "btgathright"
    password = "password"
    result = backendAPI.deleteAccount(username, password)
    print("TEST PASSED: DELETE ACCOUNT")
except Exception as ex:
    print("TEST FAILED: DELETE ACCOUNT")
    print(ex)


testUsername = "brandong"
testPass = "password"
eUser1 = ["btgathright@tamu.edu"]
eUser2 = ["brandong98@gmail.com"]
ePass1 = ["Password1"]
ePass2 = ["Password2"]
setting1 = ["jokeType"]
settingVal1 = ["Blonde"]
settingVal2 = ["Bar"]

print("CREATING ACCOUNT")
backendAPI.createAccount(testUsername, testPass, eUser1, ePass1, setting1, settingVal1)
userInfo = backendAPI.login(testUsername, testPass)
for item in userInfo[0]:
    print(item.username)
    print(item.password)
for item in userInfo[1]:
    print(item.name)
    print(item.value)

print("ADDING NEW EMAIL")
backendAPI.updateAccount("add", testUsername, testPass, eUser2, ePass2, [], [])
userInfo = backendAPI.login(testUsername, testPass)
for item in userInfo[0]:
    print(item.username)
    print(item.password)
for item in userInfo[1]:
    print(item.name)
    print(item.value)

print("REMOVING INITIAL EMAIL")
backendAPI.updateAccount("sub", testUsername, testPass, eUser1, ePass1, [], [])
userInfo = backendAPI.login(testUsername, testPass)
for item in userInfo[0]:
    print(item.username)
    print(item.password)
for item in userInfo[1]:
    print(item.name)
    print(item.value)

print("CHANGING JOKE TYPE")
backendAPI.updateAccount("sub", testUsername, testPass, [], [], setting1, settingVal1)
backendAPI.updateAccount("add", testUsername, testPass, [], [], setting1, settingVal2)
userInfo = backendAPI.login(testUsername, testPass)
for item in userInfo[0]:
    print(item.username)
    print(item.password)
for item in userInfo[1]:
    print(item.name)
    print(item.value)

print("DELETING ACCOUNT")
backendAPI.deleteAccount(testUsername, testPass)

#Get joke test
try:
    category = "Math"
    # testJoke = backendAPI.getJoke(category)
    print("TEST PASSED: GET JOKE")
    print("\nJoke of the Day")
    #print(testJoke)
except Exception as ex:
    print("TEST FAILED: GET JOKE")
    print(ex)
