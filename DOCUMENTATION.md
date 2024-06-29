# pyfilecrypto Documentation
## Overview
The `pyfilecrypto` module provides functionality for file encryption, decryption, and zip compression with password protection in Python. It leverages `cryptography.fernet` for file encryption and `pyzipper` for handling zip files with AES encryption.

## Import
``` python
from pyfilecrypto.crypto import *
```
## Classes
### ACrypto
#### Methods:

* genKey(filename):
Generates a new encryption key and saves it to the specified file.
``` python
ACrypto.genKey(filename)
```

* loadKey(filename):
Loads an encryption key from the specified file.
``` python
ACrypto.loadKey(filename)
```

* encryptFile(original_filename, save_as, keyfile):
Encrypts a file using the specified encryption key file and saves the encrypted data to another file.
``` python
ACrypto.encryptFile(original_filename, save_as, keyfile)
```

*decryptFile(filename, save_as, keyfile):
Decrypts an encrypted file using the specified encryption key file and saves the decrypted data to another file.
``` python
ACrypto.decryptFile(filename, save_as, keyfile)
```


### BCrypto
#### Methods:
* Encrypt(filename):
Encrypts a file with multiple encryption keys ("alpha", "bravo", "charlie").
``` python
BCrypto.Encrypt(filename)
```

* Decrypt(filename):
Decrypts a file that was encrypted with multiple keys ("charlie", "bravo", "alpha").
``` python
BCrypto.Decrypt(filename)
```

* crypt(filename, method):
Encrypts or decrypts a file based on the specified method ("encrypt" or "decrypt").
``` python
BCrypto.crypt(filename, method)
```

### Crypto
#### Methods:
* crypt(filename, method, password):
Encrypts or decrypts a file with password-protected zip archive support.
``` python
Crypto.crypt(filename, method, password)
```

## Usage
### Method: 1
#### Generate Encryption Key and Encrypt File
``` python
from pyfilecrypto.crypto import ACrypto
ACrypto.encryptFile("test.txt", "test.enc", "my_secret.key")
```

#### Use key and Decrypt File
``` python
from pyfilecrypto.crypto import ACrypto
ACrypto.decryptFile("test.enc", "test.txt", "my_secret.key")
```

### Method: 2
#### Generate Encryption Key and Encrypt File
``` python
from pyfilecrypto.crypto import BCrypto
BCrypto.Encrypt(filename = "test.txt")
```

#### Use keys and Decrypt file
``` python
from pyfilecrypto.crypto import BCrypto
BCrypto.Decrypt(filename = "test.txt")
```

### Method: 3
#### Generate Encryption key and Encrypt File
``` python 
from pyfilecrypto.crypto import BCrypto
BCrypto.crypt(filename = "test.txt", method = "encrypt")
```

#### Decrypt file using keys
``` python
from pyfilecrypto.crypto import BCrypto
BCrypto.crypt(filename = "test.txt", method = "decrypt")
```

### Method: 4
#### Encrypt and Decrypt file with keys
``` python
from pyfilecrypto.crypto import Crypto
Crypto.crypt(filename = "test.txt", method = "encrypt", password = "password")
Crypto.crypt(filename = "test.txt", method = "decrypt", password = "password")
```


## Dependencies
* `cryptography`
* `pyzipper`