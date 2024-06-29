# PyFileCrypto USAGE
## Method: 1
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
