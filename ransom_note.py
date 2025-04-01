import os
import time

# Define ransom note content
RANSOM_NOTE = """
 YOUR FILES HAVE BEEN ENCRYPTED 

ALL your important files have been locked using **military-grade encryption**. 

To get your files back, you must send **20,000 SOL** to the following wallet:

wallet Address: 123beepboopbeepboop

You have **24 HOURS** to comply, or your files will be permanently deleted.

**waittttta  minnnnnn hold onnn**
This just a simulation! To restore your files, run `decrypt.py` with the correct key.

:)
"""

# Defines test_files path
TEST_FOLDER = "test_files"
NOTE_FILE = os.path.join(TEST_FOLDER, "README_YOU_ARE_HACKED.txt")

# Writes note
with open(NOTE_FILE, "w") as f:
    f.write(RANSOM_NOTE)

print(f"💀Ransom note dropped: {NOTE_FILE}")

COUNTDOWN = 10 #not 24 hours since sim

print("\n⏳ Time remaining until permanent loss:")
for i in range(COUNTDOWN, 0, -1):
    print(f"⏳ {i} seconds remaining...", end="\r", flush=True)
    time.sleep(1)

print("\n💀*Files deleted!* ... LOL Run `decrypt.py` to restore:)")
