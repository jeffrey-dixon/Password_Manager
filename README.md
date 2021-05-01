# Password_Manager
Pass123 is a terminal-based password manager application designed windows users. The .exe application would be placed on a flash drive along with two text files( password.txt and defaultpass.txt) and a pre-made secret key. 

To view a demonstration of the application, view our presentation with the link below.
Presentation: https://www.youtube.com/watch?v=0xvSFtdXAoA

Security Implementations:
Data encryption- Using python's fernet cryptography module, the sensitive data files (password.txt and defaultpass.txt) are encrypted and can only be decrypted using a secret key generated with this import
Multifactor Authentication- Use of a master password upon login and the requirement of a secret key. The user will be instructed to move this secret off the flashdrive onto their computer.
Application Inturruption Automatic Encryption- Using the python's signal module, if the user shuts down the application in ways not designed to exit, the application will automatically encrypt the sensitive data files. Examples include keyboard inturruption via control + C or pressing the red exit button on the terminal window. 

******To set up a functional application, please review instructions below******
1. Convert Pass123.py into a .exe file. We recommend using pyinstaller. An this .exe file onto a flashdrive.
2. Use the generate_filekey.py function to creat a secret key, do not change the name of the file key. Add this key to the flashdrive.
3. Create a blank passwords.txt file and defaultpass.txt file that includes the string <____default____password____>. Add these two files on the flashdrive.

For first use, refer to the User Manual.
