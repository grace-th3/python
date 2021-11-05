print (" ---------------------------------------------- ")
print ("|                                              |")
print ("|    01HelloWorld                              |")
print ("|    Name : Grace Thomas                       |")
print ("|    Version : 01                              |")
print ("|                                              |")
print (" ---------------------------------------------- ")

string = input("What is your string? ")
for i in range(len(string)):
    print("%c = %d" %(string[i], ord(string[i])))