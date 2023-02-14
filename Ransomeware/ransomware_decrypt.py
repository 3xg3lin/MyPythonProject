import os
import cryptography.fernet

files = []

for file in os.listdir():
	if file == "ransomware.py" or file == "generated.key" or file =="ransomware_decrypt.py":
		continue #do not encrypt the current file we are working with or the key
	if os.path.isfile(file):
		files.append(file) #do not add if this is a directory, only if a file


with open("generated.key","rb") as generatedkey:
	secret_key = generatedkey.read()

for file in files:
	with open(file,"rb") as the_file:
		contents = the_file.read()
	contents_decrypted = cryptography.fernet.Fernet(secret_key).decrypt(contents)
	with open(file,"wb") as the_file:
		the_file.write(contents_decrypted)
