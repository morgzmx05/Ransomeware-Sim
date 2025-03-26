# where the encryption and decryption will take place


import os
import json
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# test_folder to encrypt tests
TEST_FOLDER = "test_files"

# generate a rand encryption key
KEY_FILE = "key.bin"
if not os.path.exists(KEY_FILE):
    key = get_random_bytes(32)  # AES-256 req 32-byte key
    with open(KEY_FILE, "wb") as kf:
        kf.write(key)
else:
    with open(KEY_FILE, "rb") as kf:
        key = kf.read()

# AES encryption func
def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_EAX)  # EAX for auth
    with open(file_path, "rb") as f:
        file_data = f.read()

    ciphertext, tag = cipher.encrypt_and_digest(file_data)
    encrypted_data = {
        "nonce": cipher.nonce.hex(),
        "tag": tag.hex(),
        "ciphertext": ciphertext.hex()
    }

    # Overwrite testfiles
    with open(file_path, "w") as f:
        json.dump(encrypted_data, f)

    print(f"🔒 Encrypted: {file_path}")

# Encrypt test_folder files
for filename in os.listdir(TEST_FOLDER):
    file_path = os.path.join(TEST_FOLDER, filename)
    encrypt_file(file_path, key)

print("All files successfuly encrypted!")
