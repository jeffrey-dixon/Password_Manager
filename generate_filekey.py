from cryptography.fernet import Fernet

def key_gen():
  # key generation
  key = Fernet.generate_key()

  # string the key in a file
  with open('filekey.key', 'wb') as filekey:
     filekey.write(key)
key_gen()
