"""

>> This is a simple program created to encrypt and decrypt files.
>> File paths should be in the form DISK:\... (You can't encrypt folders, only actual files).
>> Private and public keys are in the same directory, but you don't need to access them to run the program.

"""

# imports
import rsa
from security import encrypt_with_pub, decrypt_with_priv, get_keys


# Main program
def options():
    print("1. Encrypt a file\n2. Decrypt a file")
    user_response = int(input())

    if user_response == 1:
        get_keys()
        print("Enter the path for the file that you want to encrypt: ", end="")
        file_path_encrypt = str(input())

        try:
            with open(file_path_encrypt, "r") as file:
                file_data = file.read()
            with open(file_path_encrypt, "wb") as file:
                file.write(encrypt_with_pub(file_data))

            print("File successfully encrypted, private key and public key are below.\n")
            with open("public.pem", "rb") as file:
                print("--PUBLIC KEY (SAFE TO SHARE)--")
                print(file.read().decode())
            with open("private.pem", "rb") as file:
                print("--PRIVATE KEY (DO NOT SHARE & KEEP SECURE, ANYONE WITH THIS KEY CAN DECRYPT YOUR DATA.)--")
                print(file.read().decode())

        except FileNotFoundError:
            print("No such path exists. Check to make sure you entered it correctly.")

    elif user_response == 2:
        print("Enter the path for the file that you want to decrypt: ", end="")
        file_path_decrypt = str(input())
        try:
            with open(file_path_decrypt, "rb") as file_decrypt:
                encrypted_data = file_decrypt.read()
                with open("private.pem", "rb") as file_privatekey:
                    private_key = rsa.PrivateKey.load_pkcs1(file_privatekey.read())
                    decrypted_data = decrypt_with_priv(encrypted_data, private_key)
            with open(file_path_decrypt, "w") as file_decrypt_write:
                file_decrypt_write.write(decrypted_data.decode())
                print("Successfully decrypted file. Decrypted data is in the same file.")

        except FileNotFoundError:
            print("No such path exists. Check to make sure you entered it correctly.")


# Autorun on start
options()
