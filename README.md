# PyFileCrypto

PyFileCrypto is a Python module for easy encryption and decryption of files using the `cryptography` library. It provides a simple interface to generate encryption keys, encrypt files, and decrypt files securely.

## Installation

You can install PyFileCrypto using pip:

```bash
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
