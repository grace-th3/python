def stringloop():
        print ("                       ")
        print ("----Start of Output ---------------------------")
        print ("                       ")
        value = input("What is your string? ")
        for x in value:
            print (x)
        print ("                       ")
        print ("----End of Output -----------------------------")
        print ("                       ")  
        print ("                       ")
        input ("Press Enter to continue") 
def convertascii():
        print(" ")
        print("----Start of Output ---------------------------")
        print(" ")
        string = input("What is your string? ")
        for i in range(len(string)):
            print("%c = %d" %(string[i], ord(string[i])))
        print(" ")
        print("----End of Output -----------------------------")
        print(" ")
        print(" ")
        print(" ")
        input ("Press Enter to continue") 
def encodestring():
        print ("                       ")
        print ("----Start of Output ---------------------------")
        value = input("What is your string? ")
        message = ""
        for element in value:
              x = chr(ord(element)+1)
              print(element,"=",x)
              message += x
              print(message)
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
