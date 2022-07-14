import hashlib, base64

salts = [
    "Cat",
    "dOg",
    "goLf",
    "baSeBall",
    "tEam",
    "sHeeP",
    "gOAt",
    "moUsE",
    "PeOPLe",
    "hoUsE"
]

def create_hashKey(value, x, y):
    hashkey = value

    for j in range(x):
        passStr = hashkey + salts[y]
        hashKey = hashlib.shake_256(passStr.encode())

    return hashKey.hexdigest(10)

def encrypt(value):
    encrypted_value = base64.b64encode(value)
    return encrypted_value

def decrypt(value):
    decrypted_value = base64.b64decode(value)
    return decrypted_value
