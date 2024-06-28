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
### Generate Encryption Key and Encrypt File
``` python
from pyfilecrypto import crypto
crypto.encFile("test.txt", "test.enc", "my_secret.key")
```

### Decrypt a File
``` python
from pyfilecrypto import crypto
crypto.decFile("test.enc", "test.txt", "my_secret.key")
```
### Generate Encryption Key and Encrypt File
``` python
from pyfilecrypto.crypto import *
crypt(filename = "test.txt", method = "encrypt")
```
### Decrypt
```python
from pyfilecrypto.crypto import *
crypt(filename = "test.txt", method = "decrypt")
```

### or
``` python
from pyfilecrypto.crypto import Crypto
Crypto.crypt(filename = "test.txt", method = "encrypt", password = "password")
Crypto.crypt(filename = "test.txt", method = "decrypt", password = "password")
```

