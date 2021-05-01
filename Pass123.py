import random, os, time, signal
from cryptography.fernet import Fernet #128-bit AES encryption using symmetric key
from colorama import Fore #provides color to text

#Determines the location of the symmetric key to use for the encryption/decryption
os.system("where /r c:\\users filekey.key > whereiskey.txt")
f = open("whereiskey.txt", "r")
keylocation = f.read().strip("\n")
f.close()
os.system("del whereiskey.txt")

#Function that decrypts the password.txt file using the symmetric key
def decrypt():
    os.system("attrib -h password.txt")
    with open(keylocation, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('password.txt', 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('password.txt', 'wb') as dec_file:
        dec_file.write(decrypted)
    os.system("attrib +h password.txt")

#Function that decrypts the defaultpass.txt file using the symmetric key 
def decrypt_masterpass():
    os.system("attrib -h defaultpass.txt")
    with open(keylocation, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('defaultpass.txt', 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('defaultpass.txt', 'wb') as dec_file:
        dec_file.write(decrypted)
    os.system("attrib +h defaultpass.txt")
 
#Function to encrypt the password.txt file using the symmetric key
def encrypt():
    os.system("attrib -h password.txt")
    with open(keylocation, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('password.txt', 'rb') as file:
        plaintext = file.read()
    encrypted = fernet.encrypt(plaintext)
    with open('password.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    os.system("attrib +h password.txt")

#Function that decrypts the defaultpass.txt file using the symmetric key 
def encrypt_masterpass():
    os.system("attrib -h defaultpass.txt")
    with open(keylocation, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('defaultpass.txt', 'rb') as file:
        plaintext = file.read()
    encrypted = fernet.encrypt(plaintext)
    with open('defaultpass.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    os.system("attrib +h defaultpass.txt")
 
#Function that creates a secure password using user input mixed with integration of numbers, symbols, and randomization
def passwordgenerator():
    password_generated_list = []
 
    #chooses a random number between 0-99
    number_list = []
    for num in range(0,100):
        number_list.append(num)
    random_number = random.choice(number_list)
    password_generated_list.append(str(random_number))
 
    #randomly select three category questions for user input
    category_list = ["household item", "color", "computer brand", "country",'video game', 'sports team', 'city', 'food and drink', 'verb', 'adjective', 'profession', 'famous person', 'thing you find in the bathroom/kitchen', 'thing you take on holiday', 'fruit or vegetable', 'thing that flys', 'thing that is yellow', 'item you can buy in IKEA', 'thing you find inside your refrigerator', 'thing that is cold', 'thing you find in an office', 'thing that is round', 'thing that you find scary', 'thing related to Christmas', 'thing with wheels', 'thing in the garden', 'thing you can turn off', 'girls name', 'boys name', 'restaurant', 'ocean', 'reptile', 'piece of furniture', 'US state', 'National park', 'thing that you plug in', 'thing you do in the morning', 'thing you hang up', 'emotion', 'shiny object', 'thing that runs', 'thing that is fast', 'weather forecast', 'musical instrument', 'thing that is quiet', 'zoo animal', 'farm animal', 'hand tool', 'power tool', 'eating utensil', 'thing made of plastic', 'thing made of wood', 'thing made of paper', 'type of pet', 'thing you find in the bathroom', 'breakable object', 'thing with wheels', 'thing that rings', 'thing that is light', 'thing that is heavy', 'thing that opens', 'thing that locks', 'article of clothing', 'writing utensil', 'thing that is wet', 'hard object', 'dessert', 'furry animal', 'sharp thing', 'breakfast food', 'thing that is loud', 'thing with buttons', 'method of transportation', 'thing with numbers', 'thing that grows', 'container', 'item in a classroom', 'long object', 'small object', 'calendar month', 'holiday', 'marine animal', 'type of berry', 'retail store', 'fast food chain', 'type or meat', 'type of cheese', 'dairy product', 'thing that is blue','thing that is green', 'thing that is red','thing that is white','thing that is black', 'electronic device', 'type of fish', 'type of bird']
    random_word_1 = random.choice(category_list)
    random_word_2 = random.choice(category_list)
    random_word_3 = random.choice(category_list)
    
    #Ensuring all three questions are different
    while random_word_2 == random_word_1:
        random_word_2 = random.choice(category_list)
    while random_word_3 == random_word_1 or random_word_3 == random_word_2:
        random_word_3 = random.choice(category_list)

    #View the password file in order to compare its contents to user input
    os.system("attrib -h password.txt")
    f = open('password.txt', 'r')
    fstring = f.read()
    f.close()
    os.system("attrib +h password.txt")

    #Assigns a variable for the answer to question 1, ensure that it is longer than 3 characters, and that the word has not been previously used
    ans_1 = input(Fore.LIGHTYELLOW_EX + '\nEnter a word related to a(n) ' + random_word_1 + ': ')
    if len(ans_1) <= 3:
        ans_1 = input(Fore.LIGHTRED_EX + '**ERROR**: must be longer than 3 characters: ' + Fore.LIGHTYELLOW_EX)
    while ans_1.upper() in fstring.upper():
        ans_1 = input(Fore.LIGHTRED_EX + '**ERROR**: This word has been previously used: ' + Fore.LIGHTYELLOW_EX)
    
    #Assigns a variable for the answer to question 2, ...
    ans_2 = input(Fore.LIGHTYELLOW_EX + 'Enter a word related to a(n) ' + random_word_2 + ': ')
    if len(ans_2) <= 3:
        ans_2 = input(Fore.LIGHTRED_EX + '**ERROR**: must be longer than 3 characters: ' + Fore.LIGHTYELLOW_EX)
    while ans_2.upper() in fstring.upper() or ans_2 == ans_1:
        ans_2 = input(Fore.LIGHTRED_EX + '**ERROR**: This word has been previously used: ' + Fore.LIGHTYELLOW_EX)
    
    #Assigns a variable for the answer to question 3, ...
    ans_3 = input(Fore.LIGHTYELLOW_EX + 'Enter a word related to a(n) ' + random_word_3 + ': ')
    if len(ans_3) <= 3:
        ans_3 = input(Fore.LIGHTRED_EX + '**ERROR**: must be longer than 3 characters: ' + Fore.LIGHTYELLOW_EX)
    while ans_3.upper() in fstring.upper() or ans_3 == ans_2 or ans_3 == ans_1:
        ans_3 = input(Fore.LIGHTRED_EX + '**ERROR**: This word has been previously used: ' + Fore.LIGHTYELLOW_EX)
    
    #Create a list of lowercase letters
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string1 = ''
    string2 = ''
    string3 = ''
    wordlist = [ans_1, ans_2, ans_3]
 
    for items in wordlist:
        
        #Capitalize a random letter from answer 1
        if items == ans_1:
            random_letter = random.choice(alphabet)
            for char in ans_1:
                while random_letter not in ans_1:
                    random_letter = random.choice(alphabet)
                if char == random_letter:
                    char = char.upper()
                else:
                    char = char
                string1 += char
            password_generated_list.append(string1)
 
        #Capitalize a random letter from answer 2
        if items == ans_2:
            random_letter_2 = random.choice(alphabet)
            for char in ans_2:
                while random_letter_2 not in ans_2:
                    random_letter_2 = random.choice(alphabet)
                if char == random_letter_2:
                    char = char.upper()
                else:
                    char = char
                string2 += char
            password_generated_list.append(string2)

        #Capitalize a random letter from answer 3
        if items == ans_3:
            random_letter_3 = random.choice(alphabet)
            for char in ans_3:
                while random_letter_3 not in ans_3:
                    random_letter_3 = random.choice(alphabet)
                if char == random_letter_3:
                    char = char.upper()
                else:
                    char = char
                string3 += char
            password_generated_list.append(string3) 
 
    #Create a list of special characters/symbols that are generally accepted for most websites
    special_char_list = ['!','@','#','$','%','&','*','?','_','-']
    #Generate random symbols from the list
    random_special = random.choice(special_char_list)
    random_special_2 = random.choice(special_char_list)
    #Ensures the symbols are unique 
    while random_special_2 == random_special:
        random_special_2 = random.choice(special_char_list)
    password_generated_list.append(random_special)
    password_generated_list.append(random_special_2)
 
    #Assigning variables username and website that will be associated with the password that will be generated
    username = input("\nWhat is your username: ")
    website = input("\nWhat website is this password for: ")
    
    #Add add the variables form password_generated_list and randomize the order into a final password
    final_password = ''
    random.shuffle(password_generated_list)
    for items in password_generated_list:
        final_password += items
    #Format the user's new password, website, and username to be stored in the password file
    fileadd = Fore.RESET + "Website: " + Fore.BLUE + website + Fore.RESET + " | Username: " + Fore.RED + username + Fore.RESET + " | Password: " + Fore.CYAN + final_password + Fore.RESET + "\n"
    os.system("attrib -h password.txt")
    f = open("password.txt", "a")
    #Add the newly formatted information to the password.txt
    f.write(fileadd)
    f.close()
    os.system("attrib +h password.txt")
    #Prints the generated password
    print("\nYour generated password is: " + final_password + "\n")

#Test a user provided password for strength based on 6 quantifiable metrics 
def pass_strength():
    
    length_score = 0
    case_complexity_score = 0
    number_score = 0
    special_char_score = 0
    repeating_score = 0
    incrementing_score = 0
    
    #Assigns a vairiable for the user's provided password
    passwd = input(Fore.LIGHTYELLOW_EX + "\nWhat is your password?: ")
    #Define the length of the user's password
    length_of_password = len(passwd)
    #Calculate length score based on password length (1 of 6 metrics)
    if length_of_password <= 6:
        length_score = 0
    elif length_of_password > 6 and length_of_password <=10:
        length_score = 18
    else:
        length_score = 30
    
    #Calculates a score based of if the password has both upper and lowercase letters (2 of 6 metrics)
    upper = False
    lower = False
    for char in passwd:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        else:
            break
    #Calculates a score of 5 or 12 if password has only uppper/lower or mixed, respectively
    if upper == lower:
        case_complexity_score = 12
    
    else:
        case_complexity_score = 5
 
    #Calculates a score based off of how many numbers are included (3 of 6 metrics)
    digit_counter = 0
    for char in passwd:
        if char.isdigit():
            digit_counter += 1
    if digit_counter == 0:
        number_score = 0
    elif digit_counter == 1:
        number_score = 5
    else:
        number_score = 7
 
    #Calculate a score based on if passwords includes special characters (4 of 6 metrics)
    special_counter = 0
    for char in passwd:
        if char in "[@_!#$%&*?-":
            special_counter += 1
    if special_counter == 0:
        special_char_score = 0
    elif special_counter == 1:
        special_char_score = 7
    else:
        special_char_score = 10
 
    #Calculate repeating/identical character score (5 of 6 metrics)
    charcount = 0
    singlecount = 1
    preceeding_char = None
     
    for char in passwd:
        if char == preceeding_char:
            singlecount += 1
            charcount = max(charcount, singlecount)
        else:
            singlecount = 0
        preceeding_char = char
    if charcount == 0:
        repeating_score = 21
    if charcount == 1:
        repeating_score = 19
    if charcount == 2:
        repeating_score = 0
 
    #Calculate incrementing character score based on if password includes strings in below list
    characters = ['abc','bcd','cde','123','234','345','456','567','678','789']
    for i in characters:
        if i in passwd:
            incrementing_score += 20
        else:
            incrementing_score +=0
    if incrementing_score > 0:
        incrementing_score = 0
    else:
        incrementing_score = 20
    
    #Calculate the total password score out of 100 by adding the 6 metrics together
    total_score = length_score + case_complexity_score + number_score + special_char_score + repeating_score + incrementing_score      
    #added special considerations to calibrate password score based off of different conditions
    if length_score == 0:
        total_score -= 20
    if length_of_password < 4:
        total_score = 0
    print("\nYour password score is: " + (str(total_score) + '/100\n'))
 
#Function that changes a user's stored password
def change_pass():
    x = Fore.RED + "**No password is stored for this website**" + Fore.RESET
    old_pass = input(Fore.LIGHTYELLOW_EX + "\nWhat website do you want to change your password for: ")
    os.system("attrib -h password.txt")
    oldfile = open("password.txt", "r")
    #finds the line in the pasword file which relates to the users input
    lines = oldfile.readlines()
    for individual_line in lines:
        if old_pass.upper() in individual_line.upper():
            x = individual_line
    oldfile.close()
    os.system("attrib +h password.txt")
    print("\n" + x)
    #Replaces the line with the new password
    if x != Fore.RED + "**No password is stored for this website**" + Fore.RESET: 
        new_password = input(Fore.LIGHTYELLOW_EX + "What is your new password: ")
        username = input("\nWhat is your username: ")
        fileadd = Fore.RESET + "Website: " + Fore.BLUE + old_pass + Fore.RESET + " | Username: " + Fore.RED + username + Fore.RESET + " | Password: " + Fore.CYAN + new_password + Fore.RESET + "\n"
        print(Fore.GREEN + "\nSuccessfully updated" + Fore.RESET)
        print("\n" + fileadd)

        #Rewrite the password.txt with the updated password
        os.system("attrib -h password.txt")
        newfile = open("password.txt", "w")
        for line in lines:
            if line != x:
                newfile.write(line)
        newfile.close()

        f = open("password.txt", "a")
        f.write(fileadd)
        f.close()
        os.system("attrib +h password.txt")

#Function that searchs for a stored password
def search_pass():
    x = Fore.RED + "**No password is stored for this website**" + Fore.RESET
    old_pass = input(Fore.LIGHTYELLOW_EX + "\nWhat website do you want to search the password for: ")
    os.system("attrib -h password.txt")
    oldfile = open("password.txt", "r")
    lines = oldfile.readlines()
    #Search through the password.txt using website provided by the users
    for individual_line in lines:
        if old_pass.upper() in individual_line.upper():
            x = individual_line
    oldfile.close()
    os.system("attrib +h password.txt")
    print(Fore.RESET + "\n" + x)

#The main app function which displays different options the user may choose, requiring user input
def main_app():
    #Try statement to wrap the proper use of the application
    try:
        #The whole application only runs if the filekey location can be found
        if len(keylocation) > 0:
            os.system("attrib -h defaultpass.txt && attrib -h password.txt")
            f = open("defaultpass.txt", "r")
            y = f.read()
            f.close()
            f = open("password.txt", "r")
            x1 = f.read()
            f.close()
            os.system("attrib +h defaultpass.txt && attrib +h password.txt")
            #The application will check if defaultpass.txt and password.txt have not been change from its original state, indicating a new user
            #string "____default____password____" is the contents of the unchanged defaultpass.txt
            #gAAAAABg is a string indicating the file would be encrypted
            if y == "____default____password____" and "gAAAAABg" not in x1:
                print(Fore.CYAN + "------- Welcome to Pass123, the All Inclusive Password Tool -------" + Fore.RESET)
                master_reset = 1
                #Allows the new user to creats a master password
                while master_reset == 1:
                    newpass = input(Fore.LIGHTYELLOW_EX + "\nWhat would you like to use as a master password: ")
                    confirm_newpass = input("\nConfirm your master password: ")
                    os.system("cls")
                    if newpass == confirm_newpass:
                        os.system("attrib -h defaultpass.txt")
                        newmaster = open("defaultpass.txt", "w")
                        newmaster.write(confirm_newpass)
                        newmaster.close()
                        os.system("attrib +h defaultpass.txt")
                        print(Fore.GREEN + "\nMaster Password Succefully Saved" + Fore.RESET)
                        master_reset = 0
                        time.sleep(3)
                        os.system("cls")

           #This master password authentication will be required upon each app startup
            masterpass = input(Fore.LIGHTCYAN_EX + "Enter your master password: ")
            os.system("cls")
            os.system("attrib -h defaultpass.txt")
            f = open("defaultpass.txt", "r")
            x = f.read()
            f.close()

            if masterpass in x and "gAAAAABg" not in x1:
                with open(keylocation, 'rb') as filekey:
                    key = filekey.read()
                fernet = Fernet(key)
                with open('defaultpass.txt', 'rb') as file:
                    plaintext = file.read()
                encrypted = fernet.encrypt(plaintext)
                with open('defaultpass.txt', 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
            decrypt_masterpass()
            os.system("attrib -h defaultpass.txt")
            f = open("defaultpass.txt", "r")

            #cross-references input with stored master password
            if masterpass == f.read():
                encrypt_masterpass()
                f.close()
                os.system("attrib +h defaultpass.txt")

                while True:
                   
                    os.system("type password.txt > encryptionTest.txt")
                    f = open("encryptionTest.txt", "r")
                    password_string = f.read()
                    f.close()
                    #If password.txt is not encrypted upon application startup, this will encrypt if to allow app to function properl;y
                    if "gAAAAABg" not in password_string:
                        encrypt()
                    os.system("del encryptionTest.txt")
                    #Desplays main application menu
                    print(Fore.CYAN + "\n-----Password Menu-----\n")
                    print(Fore.YELLOW + "1.Test a Password")
                    print("2.Add a Password to Stored Passwords")
                    print("3.Generate New Password / Update Existing Password")
                    print("4.Search for a Stored Password") 
                    print("5.Change a Password")   
                    print("6.Exit\n" + Fore.RESET)
                    choice=input("Enter Option Number: ")
                    
                    #If selected, password strength function will run
                    if choice=="1":
                        pass_strength()
                        time.sleep(7)
                        os.system("cls")

                    #the enctypt() and decrypt() functions are repeatedly used to limit the time the password file in in clear text

                    #If selected, user can store their provided password, website, and username information
                    elif choice=="2":
                        own_passwd = input(Fore.LIGHTYELLOW_EX + "\nWhat password do you want to store: ")
                        username2 = input("\nWhat is your username: ") 
                        website2 = input("\nWhat website is this password for: ")
                        fileadd = Fore.RESET + "Website: " + Fore.BLUE + website2 + Fore.RESET + " | Username: " + Fore.RED + username2 + Fore.RESET + " | Password: " + Fore.CYAN + own_passwd + Fore.RESET + "\n"
                        os.system("attrib -h password.txt")
                        decrypt()
                        f = open("password.txt", "a")
                        f.write(fileadd)
                        f.close()
                        encrypt()
                        time.sleep(1)
                        os.system("cls && attrib +h password.txt")
        
                    #If selected, password generator function will run
                    elif choice=="3":
                        os.system("attrib -h password.txt")
                        decrypt()
                        passwordgenerator()
                        encrypt()
                        time.sleep(10)
                        os.system("cls && attrib +h password.txt")
                    
                    #If selected, search password function will run
                    elif choice=="4":
                        os.system("attrib -h password.txt")
                        decrypt()
                        search_pass()
                        time.sleep(10)
                        encrypt()
                        os.system("cls && attrib +h password.txt")
        
                    #If selected, change password function will run
                    elif choice=="5":
                        os.system("attrib -h password.txt")
                        decrypt()
                        change_pass()
                        encrypt()
                        time.sleep(7)
                        os.system("cls && attrib +h password.txt")
                    
                    #If selected, application will close
                    elif choice=="6":
                        os.system("cls")
                        os.system("attrib +h password.txt && attrib +h defaultpass.txt")
                        break

                    #If the user chooses any other option other than 1-6, display an error message and provide the terminal window again
                    else:
                        print(Fore.LIGHTRED_EX + "\n**Invalid Option Number**")
                        time.sleep(3)
                        os.system("cls")
           
            #If the user provides an incorrect master password, the application will close. 
            else:
                encrypt_masterpass()  
                os.system("attrib +h password.txt && attrib +h defaultpass.txt")
    #Failsafe to ensure the encryption and rehiding of the password and defaultpassword (master password) files upon improper exit of application
    except EOFError:
        encrypt()
        os.system("attrib +h password.txt && attrib +h defaultpass.txt")
    #Failsafe to ensure the encryption and rehiding of the password and defaultpassword (master password) files upon keyboard interruption
    except KeyboardInterrupt:
        encrypt()  
        os.system("attrib +h password.txt && attrib +h defaultpass.txt")
#Calls the application function
main_app()
