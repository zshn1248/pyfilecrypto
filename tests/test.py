import unittest
import os
from pyfilecrypto import crypto

class TestCrypto(unittest.TestCase):
    
    def setUp(self):
        """Set up test variables and files"""
        self.keyfile = "test_key.key"
        self.original_file = "test_file.txt"
        self.encrypted_file = "test_file.enc"
        self.decrypted_file = "decrypted_file.txt"
        
        with open(self.original_file, "w") as file:
            file.write("This is a test file for encryption and decryption.")
        
        crypto.genKey(self.keyfile)
    
    def tearDown(self):
        """Clean up test files"""
        os.remove(self.keyfile)
        os.remove(self.original_file)
        if os.path.exists(self.encrypted_file):
            os.remove(self.encrypted_file)
        if os.path.exists(self.decrypted_file):
            os.remove(self.decrypted_file)
    
    def test_encryption(self):
        """Test encryption"""
        crypto.encFile(self.original_file, self.encrypted_file, self.keyfile)
        self.assertTrue(os.path.exists(self.encrypted_file))
    
    def test_decryption(self):
        """Test decryption"""
        crypto.encFile(self.original_file, self.encrypted_file, self.keyfile)
        crypto.decFile(self.encrypted_file, self.decrypted_file, self.keyfile)
        
        with open(self.decrypted_file, "r") as file:
            decrypted_content = file.read()
        
        with open(self.original_file, "r") as file:
            original_content = file.read()
        
        self.assertEqual(original_content, decrypted_content)

if __name__ == "__main__":
    unittest.main()
