from cryptography.fernet import Fernet



# Generate key and write it to a file
def genKey(filename):
    """
    Save secret key Filename with extension
    """
    key = Fernet.generate_key()
    with open(filename, "wb") as key_file:
        key_file.write(key)
def loadKey(filename):
    """
    Load key file
    """
    return open(filename, "rb").read()
def encFile(original_filename, save_as, keyfile):
    gen = genKey(keyfile)
    key = loadKey(keyfile)
    fernet = Fernet(key)
    with open(original_filename, "rb") as file:
        data = file.read()
    encData = fernet.encrypt(data)
    
    with open(save_as, "wb") as file:
        file.write(encData)

def decFile(filename, save_as, keyfile):
    """
    Decrypt file
    filename: encrypted filename
    save_as: filename to save decrypted file
    keyfile: filename of key used for encryption
    """
    # Load key
    key = loadKey(keyfile)
    fernet = Fernet(key)
    # Load encrypted file
    with open(filename, "rb") as file:
        encData = file.read()
    decData = fernet.decrypt(encData)
    
    # Decrypt and save file
    with open(save_as, "wb") as file:
        file.write(decData)
    
def Encrypt(filename):
    """
    Encrypt files with original filenames and extensions
    """
    encFile(filename, filename, "alpha")
    encFile(filename, filename, "bravo")
    encFile(filename, filename, "charlie")
def Decrypt(filename):
    decFile(filename, filename, "charlie")
    decFile(filename, filename, "bravo")
    decFile(filename, filename, "alpha")
def crypt(filename, method):
    if method == "encrypt":
        Encrypt(filename)
    elif method == "decrypt":
        Decrypt(filename)
