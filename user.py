from hash import create_hashKey, encrypt, decrypt

class setting:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class credential:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def addUser(username, password, accounts, passwords, settings, values):
    x1 = (len(username) % 17) + 3
    x2 = (len(password) % 17) + 3
    y1 = x2 % 10
    y2 = x1 % 10
    userID = create_hashKey(username, x1, y1)
    passID = create_hashKey(password, x2, y2)
    
    userFile = open("users.txt", "a")
    userFile.write("Username: " + userID + "\n")
    userFile.write("Password: " + passID + "\n")
    userFile.write("{\n")
    
    for i in range(len(accounts)):
        userFile.write("    Username: " + encrypt(accounts[i].encode()).decode() + "\n")
        userFile.write("    Password: " + encrypt(passwords[i].encode()).decode() + "\n")
        userFile.write("\n")

    for i in range(len(settings)):
        userFile.write("    Setting: " + settings[i] + "\n")
        userFile.write("    Value: " + values[i] + "\n")
        userFile.write("\n")

    userFile.write("}\n\n")
    userFile.close()
    return

def rmUser(username, password):
    x1 = (len(username) % 17) + 3
    x2 = (len(password) % 17) + 3
    y1 = x2 % 10
    y2 = x1 % 10
    userID = create_hashKey(username, x1, y1)
    passID = create_hashKey(password, x2, y2)

    userFile = open("users.txt", 'r')
    contents = userFile.readlines()
    userFile.close()

    start = 0
    end = 0
    for i in range(len(contents)):
        if (contents[i] == "Username: " + userID + '\n'):
            start = i
            i += 1

            if (contents[i] == "Password: " + passID + '\n'):
                i += 1
                while(contents[i] != "}\n"):
                    i += 1
                end = i

                del contents[start:end+2]
                userFile = open("users.txt", 'w')
                contents = "".join(contents)
                userFile.write(contents)
                userFile.close()
                return "Success"

            else:
                return "Error: 2"

    return "Error: 1"

def scanUserList(username, password):
    x1 = (len(username) % 17) + 3
    x2 = (len(password) % 17) + 3
    y1 = x2 % 10
    y2 = x1 % 10
    userID = create_hashKey(username, x1, y1)
    passID = create_hashKey(password, x2, y2)

    userFile = open("users.txt", 'r')
    contents = userFile.readlines()
    userFile.close()

    for i in range(len(contents)):
        if (contents[i][0:10] == "Username: "):
            userIDcmp = ""
            passIDcmp = ""

            for letter in contents[i][10:]:
                if (letter == '\n'):
                    break
                userIDcmp += letter
            i += 1

            for letter in contents[i][10:]:
                if (letter == '\n'):
                    break
                passIDcmp += letter
            i += 1

            if (userID == userIDcmp):
                if (passID == passIDcmp):
                    return ["Success", getUserInfo(contents, i)]
                else:
                    return ["Error: 2", 0]
             
    return ["Error: 1", 0]

def getUserInfo(contents, pointer):
    userCredentials = []
    userSettings = []

    i = pointer
    while (i < len(contents)):
        if (contents[i] == "}\n"):
            return [userCredentials, userSettings]

        if (contents[i][0:14] == "    Username: "):
            username = ""
            password = ""

            for letter in contents[i][14:]:
                if (letter == '\n'):
                    break
                username += letter
            i += 1

            for letter in contents[i][14:]:
                if (letter == '\n'):
                    break
                password += letter
            i += 1
            userCredentials.append(credential(username, password))

        if (contents[i][0:13] == "    Setting: "):
            name = ""
            value = ""

            for letter in contents[i][13:]:
                if (letter == '\n'):
                    break
                name += letter
            i += 1

            for letter in contents[i][11:]:
                if (letter == '\n'):
                    break
                value += letter
            i += 1
            userSettings.append(setting(name, value))
        i += 1

    return [userCredentials, userSettings]
