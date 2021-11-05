def helloworld():
        print ("                       ")
        print ("----Start of Output ---------------------------")
        print ("                       ")
        print ("Hello World")
        print ("                       ")
        print ("----End of Output -----------------------------")
        print ("                       ")  
        print ("                       ")
        input ("Press Enter to continue")

def goodbyeworld():
        print ("                       ")
        print ("----Start of Output ---------------------------")
        print ("                       ")
        print ("Hello World")
        input ("------> Program paused - press enter to continue")
        print("Goodbye World")
        print ("                       ")
        print ("----End of Output -----------------------------")
        print ("                       ")  
        print ("                       ")
        input ("Press Enter to continue")
def goodbyeperson():
        print ("                       ")
        print ("----Start of Output ---------------------------")
        print ("                       ")
        print ("Hello")
        value = input("What is your name ? ") 
        print (f'Goodbye {value}')
        print ("                       ")
        print ("----End of Output -----------------------------")
        print ("                       ")  
        print ("                       ")
        input ("Press Enter to continue")
def goodteacher():
        print ("                       ")
        print ("----Start of Output ---------------------------")
        print ("                       ")
        value = input("Teacher's name (try Mr Horan) ")
        if value == "Mr Horan":
            print("You are lucky, he is a great teacher") 
        else:
            print(value, "is an ok teacher")
        print ("                       ")
        print ("----End of Output -----------------------------")
        print ("                       ")  
        print ("                       ")
        input ("Press Enter to continue")
def forloop():
        print ("                       ")
        print ("----Start of Output ---------------------------")
        print ("                       ")
        for x in range (1,500):
                print(x)
        print ("                       ")
        print ("----End of Output -----------------------------")
        print ("                       ")  
        print ("                       ")
        input ("Press Enter to continue")
def whileloop():
        print ("                       ")
        print ("----Start of Output ---------------------------")
        value = input("What is the name of this subject? " )
        while value != 'IST':
                print ("Not Correct - try again")
                value = input("What is the name of this subject? " )
        if value == "IST":
                print("               ")
                print("               ")
                print(" Congratulations!!")
                print("               ")
                print("               ")
                print("               ")
        print ("----End of Output -----------------------------")
        print ("                       ")  
        print ("                       ")
        input ("Press Enter to continue")

def invalid():
        print ("                       ")
        print ("----Start of Output ---------------------------")
        print ("                       ")
        print ("invalid option")
        print ("                       ")
        print ("----End of Output -----------------------------")
        print ("                       ")  
        print ("                       ")
        input ("Press Enter to continue") 
        clear()


def end():
        print ("                       ")
        print ("----Start of Output ---------------------------")
        print ("                       ")
        print ("                       ")
        print ("----End of Output -----------------------------")
        print ("                       ")  
        print ("                       ")
        input ("Press Enter to continue")

import os

def clear():
        os.system("cls")

        print (" ---------------------------------------------- ")
        print ("|                                              |")
        print ("|    07menu                                    |")
        print ("|    Name : Grace Thomas                       |")
        print ("|    Version : 01                              |")
        print ("|                                              |")
        print (" ---------------------------------------------- ")

        print ("1. Hello World")
        print ("2. Goodbye World")
        print ("3. Goodbye Person")
        print ("4. Good Teacher")
        print ("5. forLoop")
        print ("6. whileLoop")
        print ("7. string Loop")
        print ("8. Convert to ascii")
        print ("9. Encode a string")
        print ("x. To Exit")

        value = input("Enter an option ")

        if value == "1": 
                helloworld()
                clear()

        if value == "2": 
                goodbyeworld()
                clear()

        if value == "3":
                goodbyeperson()
                clear()


        if value == "4":
                goodteacher()
                clear()

        if value == "5": 
                forloop()
                clear()

        if value == "6": 
                whileloop()
                clear()
        if value == "7": 
                invalid()
                clear()
        
        if value == "8": 
                invalid()
                clear()
        
        if value == "9": 
                invalid()
                clear()

        if value == "x": 
                end()
                quit()

        
        

        
print (" ---------------------------------------------- ")
print ("|                                              |")
print ("|    07menu                                    |")
print ("|    Name : Grace Thomas                       |")
print ("|    Version : 01                              |")
print ("|                                              |")
print (" ---------------------------------------------- ")

print ("1. Hello World")
print ("2. Goodbye World")
print ("3. Goodbye Person")
print ("4. Good Teacher")
print ("5. forLoop")
print ("6. whileLoop")
print ("7. string Loop")
print ("8. Convert to ascii")
print ("9. Encode a string")
print ("x. To Exit")

value = input("Enter an option ")
if value == "1": 
        helloworld()
        clear()

if value == "2": 
        goodbyeworld()
        clear()
        
        

if value == "3":
        goodbyeperson()
        clear()


if value == "4":
        goodteacher()
        clear()

if value == "5": 
        forloop()
        clear()

if value == "6": 
        whileloop()
        clear()

if value == "7": 
        invalid()
        clear()

if value == "8": 
        invalid()
        clear()

if value == "9": 
        invalid()
        clear()

if value == "x": 
        end()
        quit()

if value != ("1") and ("2")and ("3")and ("4")and ("5")and ("6")and ("7")and ("8")and ("9")and ("x"):
        invalid()


