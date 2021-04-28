from cryptography.fernet import Fernet

#Creates a symmetric key
def key_gen():
  key = Fernet.generate_key()
  with open('filekey.key', 'wb') as filekey:
     filekey.write(key)
key_gen()
