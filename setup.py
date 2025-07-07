from setuptools import setup, find_packages

with open("DOCUMENTATION.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyfilecrypto",
    version="1.0.5",
    author="Muhammad Zeeshan Saeed",
    author_email="zshn1248@gmail.com",
    description="A module for file encryption, decryption, and steganography",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zshn1248/pyfilecrypto",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'cryptography',
        'pyzipper',
        'pillow',
    ],
    include_package_data=True,
)
