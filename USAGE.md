## Usage
### Generate Encryption Key and Encrypt File
``` python
from pyfilecrypto import crypto
crypto.encFile("test.txt", "test.enc", "my_secret.key")

## Decrypt a File
``` python
from pyfilecrypto import crypto
crypto.decFile("test.enc", "test.txt", "my_secret.key")
