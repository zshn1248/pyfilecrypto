import pyzipper
from cryptography.fernet import Fernet
import os

class ACrypto:
    @staticmethod
    def genKey(filename):
        """
        Save secret key Filename with extension
        """
        key = Fernet.generate_key()
        with open(filename, "wb") as key_file:
            key_file.write(key)

    @staticmethod
    def loadKey(filename):
        """
        Load key file
        """
        return open(filename, "rb").read()

    @staticmethod
    def encryptFile(original_filename, save_as, keyfile):
        ACrypto.genKey(keyfile)
        key = ACrypto.loadKey(keyfile)
        fernet = Fernet(key)
        with open(original_filename, "rb") as file:
            data = file.read()
        encData = fernet.encrypt(data)

        with open(save_as, "wb") as file:
            file.write(encData)
        print(f"Encrypted {original_filename} to {save_as} using {keyfile}")

    @staticmethod
    def decryptFile(filename, save_as, keyfile):
        """
        Decrypt file
        filename: encrypted filename
        save_as: filename to save decrypted file
        keyfile: filename of key used for encryption
        """
        key = ACrypto.loadKey(keyfile)
        fernet = Fernet(key)
        with open(filename, "rb") as file:
            encData = file.read()
        decData = fernet.decrypt(encData)

        with open(save_as, "wb") as file:
            file.write(decData)
        print(f"Decrypted {filename} to {save_as} using {keyfile}")

class BCrypto:
    @staticmethod
    def Encrypt(filename):
        """
        Encrypt files with original filenames and extensions
        """
        ACrypto.encryptFile(filename, filename, "alpha")
        ACrypto.encryptFile(filename, filename, "bravo")
        ACrypto.encryptFile(filename, filename, "charlie")

    @staticmethod
    def Decrypt(filename):
        ACrypto.decryptFile(filename, filename, "charlie")
        ACrypto.decryptFile(filename, filename, "bravo")
        ACrypto.decryptFile(filename, filename, "alpha")

    @staticmethod
    def crypt(filename, method):
        if method == "encrypt":
            BCrypto.Encrypt(filename)
        elif method == "decrypt":
            BCrypto.Decrypt(filename)

class Crypto:
    @staticmethod
    def crypt(filename, method, password):
        if method == "encrypt":
            BCrypto.Encrypt(filename)
            with pyzipper.AESZipFile("keys.zip", 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
                zipf.setpassword(password.encode('utf-8'))
                for file in ["alpha", "bravo", "charlie"]:
                    zipf.write(file, arcname=file)
            ACrypto.encryptFile("keys.zip", "keys.enc", "key")
            print("Encrypted keys.zip to keys.enc using key")
            os.remove("alpha")
            os.remove("bravo")
            os.remove("charlie")
            os.remove("keys.zip")
        elif method == "decrypt":
            ACrypto.decryptFile("keys.enc", "keys.zip", "key")
            print("Decrypted keys.enc to keys.zip using key")
            with pyzipper.AESZipFile("keys.zip") as zipf:
                zipf.setpassword(password.encode('utf-8'))
                zipf.extractall()
            BCrypto.Decrypt(filename)
            os.remove("alpha")
            os.remove("bravo")
            os.remove("charlie")
            os.remove("keys.zip")
            os.remove("keys.enc")

# Example usage
# Encrypt
# Crypto.crypt("m.txt", "encrypt", "Zeeshan")

# Decrypt
# Crypto.crypt("m.txt", "decrypt", "Zeeshan")
