# Ransomeware-Sim
For educational purposes

Test_files folder contains various different file types for testing
ransom_note.py contains the ransom note
sim.py will handle the ransomware simulation
decrypt.py may be used for decrypting the encrypted files
use generate_test_files.py to create test_files folder and variety of dif test files

To run this safely, please follow the steps below:
1) Recommended to run in virtual environment (VM)
2) make sure you have installed pycrptodome 
3) in line 47 of sim.py, if you're 'using a specific version of python, you might want to replace python with i.e. python3 or specify the full path to your python interpreter
4) Note, do not delete the key bin file, it is where the key is stored for decryption