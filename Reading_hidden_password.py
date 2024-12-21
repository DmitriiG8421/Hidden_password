file1 = open("HiddenPassword&Username.txt","r")
list_of_lines = file1.readlines()




objectfind = "Username="
index = list_of_lines[6].find(objectfind)
if index != -1:
    correct_username = list_of_lines[6][index+len(objectfind):index+len(objectfind)+5]
    print(correct_username) 

objectfind = "password="
index = list_of_lines[7].find(objectfind)
if index != -1:
    correct_password = list_of_lines[7][index+len(objectfind):index+len(objectfind)+4]
    print(correct_password,"\n\n") 


while True:
    username = input("PLease type your username: ")
    if username == correct_username:
        print("Username found.\n")
        password = input("Please type your password: ")
        if password == correct_password:
            print("Password found.\n Youa re logged in. Welcome!")
        else:
            print("Password not found. try again!\n")
            continue
    else:
            print("Username not found. try again!\n")
            continue