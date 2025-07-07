from cryptography.fernet import Fernet

class ImageStego:
    @staticmethod
    def genKey(filename):
        key = Fernet.generate_key()
        with open(filename, "wb") as f:
            f.write(key)

    @staticmethod
    def loadKey(filename):
        return open(filename, "rb").read()

    @staticmethod
    def encryptImage(secret_image_path, cover_image_path, output_image_path, keyfile):
        # Generate and load encryption key
        ImageStego.genKey(keyfile)
        key = ImageStego.loadKey(keyfile)
        fernet = Fernet(key)

        # Read secret image and encrypt it
        with open(secret_image_path, "rb") as secret_file:
            secret_data = secret_file.read()
        encrypted_data = fernet.encrypt(secret_data)

        # Read cover image (as bytes)
        with open(cover_image_path, "rb") as cover_file:
            cover_data = cover_file.read()

        # Append encrypted image data to the cover
        with open(output_image_path, "wb") as output_file:
            output_file.write(cover_data)
            output_file.write(b":::STEGO:::" + encrypted_data)

        print(f"[✔] Encrypted {secret_image_path} into {output_image_path} using {cover_image_path}")

    @staticmethod
    def decryptImage(stego_image_path, output_image_path, keyfile):
        key = ImageStego.loadKey(keyfile)
        fernet = Fernet(key)

        with open(stego_image_path, "rb") as f:
            data = f.read()

        # Find the marker and split data
        marker = b":::STEGO:::"
        if marker not in data:
            raise ValueError("No encrypted data found in the image.")

        idx = data.index(marker)
        encrypted_data = data[idx + len(marker):]

        # Decrypt original image
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(output_image_path, "wb") as out_file:
            out_file.write(decrypted_data)

        print(f"[✔] Decrypted hidden image to {output_image_path}")


# Encrypt secret image using cover
# ImageStego.encryptImage("secret.png", "cover.png", "stego.png", "stegokey.key")

# Decrypt to get original image
ImageStego.decryptImage("stego.png", "original.png", "stegokey.key")
