print (" ---------------------------------------------- ")
print ("|                                              |")
print ("|    01HelloWorld                              |")
print ("|    Name : Grace Thomas                       |")
print ("|    Version : 01                              |")
print ("|                                              |")
print (" ---------------------------------------------- ")

value = input("What is your string? ")
message = ""
for element in value:
    x = chr(ord(element)+1)
    print(element,"=",x)
    message += x
    print(message)