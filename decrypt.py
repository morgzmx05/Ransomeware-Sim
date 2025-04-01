# will be used to reverse the file encryption (test if its needed over standalone sim.py)

import os
import json
from Crypto.Cipher import AES

# Define folderwith encrypted files
TEST_FOLDER = "test_files"
KEY_FILE = "key.bin"

# Ensures keyfile exists
if not os.path.exists(KEY_FILE):
    print("ERROR: Key file missing! Cannot decrypt files.")
    exit()

# loads encryption key
with open(KEY_FILE, "rb") as kf:
    key = kf.read()

# AES decryption func
def decrypt_file(file_path, key):
    with open(file_path, "r") as f:
        encrypted_data = json.load(f)

    # extract stored encryption dets
    nonce = bytes.fromhex(encrypted_data["nonce"])
    tag = bytes.fromhex(encrypted_data["tag"])
    ciphertext = bytes.fromhex(encrypted_data["ciphertext"])

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    
    try:
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
        with open(file_path, "wb") as f:
            f.write(decrypted_data)
        print(f"Decrypted: {file_path}")
    except ValueError:
        print(f"ERROR: Decryption failed for {file_path} (Wrong key?)")

# Decrypt all files in test_files
for filename in os.listdir(TEST_FOLDER):
    file_path = os.path.join(TEST_FOLDER, filename)
    # ensures the readme isnt decrypted asw
    if file_path.endswith(".json"):
        decrypt_file(file_path, key)

print("All files successfully decrypted!")

