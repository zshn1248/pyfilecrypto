from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyfilecrypto",
    version="1.0.1",
    author="Muhammad Zeeshan Saeed",
    author_email="zshn1248@gmail.com",
    description="A module for file encryption and decryption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zshn1248/pyfilecrypto",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'cryptography',
        'pyzipper',
    ],
    include_package_data=True,
)
