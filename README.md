# PyFileCrypto

## Overview

The PyFileCrypto Module is a Python library for encrypting and decrypting files, compressing and extracting zip files with password protection. It utilizes `cryptography.fernet` for encryption and `pyzipper` for handling zip files with AES encryption.

## Features

- **File Encryption and Decryption**: Encrypt and decrypt files with strong AES encryption.
- **Key Management**: Generate and securely store keys for encryption and decryption.
- **Zip Compression**: Compress files into zip archives.
- **Password-Protected Zip Files**: Create and extract zip files with password protection.

## Installation

To install the Crypto Module, use the following command:

```sh
pip install pyfilecrypto
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

