
# pyfilecrypto Documentation

## Overview
The `pyfilecrypto` module provides functionality for file encryption, decryption, and zip compression with password protection in Python. It leverages `cryptography.fernet` for file encryption, `pyzipper` for handling zip files with AES encryption, and `Pillow` for image-based steganography using PNGs.

---

## 🔐 ACrypto

### Methods

- **`genKey(filename)`**  
  Generate and save a symmetric encryption key.
  ```python
  ACrypto.genKey("mykey.key")
  ```

- **`loadKey(filename)`**  
  Load a symmetric key from a file.
  ```python
  key = ACrypto.loadKey("mykey.key")
  ```

- **`encryptFile(original_filename, save_as, keyfile)`**  
  Encrypt a file and save the result.
  ```python
  ACrypto.encryptFile("test.txt", "test.enc", "mykey.key")
  ```

- **`decryptFile(filename, save_as, keyfile)`**  
  Decrypt a file and save the output.
  ```python
  ACrypto.decryptFile("test.enc", "test.txt", "mykey.key")
  ```

---

## 🔐 BCrypto

Encrypt/decrypt files using 3 predefined keys (`alpha`, `bravo`, `charlie`).

### Methods

- **`Encrypt(filename)`**  
  Encrypt using all 3 keys.
  ```python
  BCrypto.Encrypt("file.txt")
  ```

- **`Decrypt(filename)`**  
  Decrypt using the same key order.
  ```python
  BCrypto.Decrypt("file.txt")
  ```

- **`crypt(filename, method)`**  
  Generic encrypt/decrypt interface.
  ```python
  BCrypto.crypt("file.txt", method="encrypt")
  BCrypto.crypt("file.txt", method="decrypt")
  ```

---

## 🔐 Crypto

Encrypts file and also compresses the encryption keys into a password-protected ZIP archive.

### Methods

- **`crypt(filename, method, password)`**  
  Encrypt or decrypt file with key compression via ZIP.
  ```python
  Crypto.crypt("file.txt", method="encrypt", password="securepass")
  Crypto.crypt("file.txt", method="decrypt", password="securepass")
  ```

---

## 🖼️ ImageStego

Encrypt a secret PNG image into another visible PNG image.

### Methods

- **`encryptImage(secret_image, cover_image, output_image, keyfile)`**  
  Hide a secret PNG inside a cover PNG and save as output image.
  ```python
  ImageStego.encryptImage("secret.png", "cover.png", "stego.png", "stegokey.key")
  ```

- **`decryptImage(stego_image, output_image, keyfile)`**  
  Extract the hidden PNG from the stego image.
  ```python
  ImageStego.decryptImage("stego.png", "revealed.png", "stegokey.key")
  ```

---

## ✅ Usage Examples

### 🔸 Method 1: Basic Encryption/Decryption (ACrypto)
```python
from pyfilecrypto.crypto import ACrypto

# Encrypt
ACrypto.encryptFile("test.txt", "test.enc", "my_secret.key")

# Decrypt
ACrypto.decryptFile("test.enc", "test.txt", "my_secret.key")
```

### 🔸 Method 2: Multi-Key Encryption (BCrypto)
```python
from pyfilecrypto.crypto import BCrypto

# Encrypt
BCrypto.Encrypt("test.txt")

# Decrypt
BCrypto.Decrypt("test.txt")
```

### 🔸 Method 3: Generic Multi-Key Operation
```python
from pyfilecrypto.crypto import BCrypto

# Encrypt
BCrypto.crypt("test.txt", method="encrypt")

# Decrypt
BCrypto.crypt("test.txt", method="decrypt")
```

### 🔸 Method 4: ZIP Key Packaging with Password (Crypto)
```python
from pyfilecrypto.crypto import Crypto

# Encrypt
Crypto.crypt("test.txt", method="encrypt", password="password")

# Decrypt
Crypto.crypt("test.txt", method="decrypt", password="password")
```

### 🔸 Method 5: Steganography (Image Inside Image)
```python
from pyfilecrypto.stego import ImageStego

# Hide secret image inside cover image
ImageStego.encryptImage("secret.png", "cover.png", "stego.png", "stegokey.key")

# Reveal hidden image
ImageStego.decryptImage("stego.png", "revealed.png", "stegokey.key")
```

---

## 🧩 Dependencies

Install all dependencies via pip:

```bash
pip install cryptography pyzipper pillow
```

- **`cryptography`** – for encryption and decryption  
- **`pyzipper`** – for AES ZIP support  
- **`pillow`** – for PNG image handling in steganography