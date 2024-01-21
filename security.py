"""
>> Security portion of the program where encrypting/decrypting happens.
"""

# Requires an install of 'pip install rsa'
#imports
import rsa

public_key, private_key = rsa.newkeys(1024)


def get_keys():
    with open("public.pem", "wb") as file:
        file.write(public_key.save_pkcs1("PEM"))

    with open("private.pem", "wb") as file:
        file.write(private_key.save_pkcs1("PEM"))


def encrypt_with_pub(data):
    return rsa.encrypt(data.encode(), public_key)


def decrypt_with_priv(data, key):
    return rsa.decrypt(data, key)
