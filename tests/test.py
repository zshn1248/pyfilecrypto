import unittest
import os
from pyfilecrypto.crypto import ACrypto, BCrypto, Crypto

class TestPyFileCrypto(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.filename = "test_file.txt"
        self.encrypted_filename = "test_file.enc"
        self.decrypted_filename = "test_file_dec.txt"
        self.keyfile = "test_key"
        self.password = "testpassword"
        with open(self.filename, "w") as f:
            f.write("This is a test file for encryption and decryption.")

    def tearDown(self):
        """Clean up after each test"""
        files_to_remove = [
            self.filename,
            self.encrypted_filename,
            self.decrypted_filename,
            self.keyfile,
            "alpha",
            "bravo",
            "charlie",
            "keys.zip",
            "keys.enc"
        ]
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)

    def test_genKey_and_loadKey(self):
        """Test key generation and loading"""
        ACrypto.genKey(self.keyfile)
        key = ACrypto.loadKey(self.keyfile)
        self.assertTrue(os.path.exists(self.keyfile))
        self.assertIsInstance(key, bytes)

    def test_encryptFile_and_decryptFile(self):
        """Test file encryption and decryption"""
        ACrypto.encryptFile(self.filename, self.encrypted_filename, self.keyfile)
        ACrypto.decryptFile(self.encrypted_filename, self.decrypted_filename, self.keyfile)
        with open(self.decrypted_filename, "r") as f:
            data = f.read()
        self.assertEqual(data, "This is a test file for encryption and decryption.")

    def test_BCrypto_Encrypt_and_Decrypt(self):
        """Test BCrypto encryption and decryption"""
        BCrypto.crypt(self.filename, "encrypt")
        BCrypto.crypt(self.filename, "decrypt")
        with open(self.filename, "r") as f:
            data = f.read()
        self.assertEqual(data, "This is a test file for encryption and decryption.")

    def test_Crypto_crypt_encrypt_and_decrypt(self):
        """Test Crypto class encryption and decryption with password"""
        Crypto.crypt(self.filename, "encrypt", self.password)
        Crypto.crypt(self.filename, "decrypt", self.password)
        with open(self.filename, "r") as f:
            data = f.read()
        self.assertEqual(data, "This is a test file for encryption and decryption.")

if __name__ == "__main__":
    unittest.main()
