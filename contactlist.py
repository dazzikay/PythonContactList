from contact import Contact

#list of contacts
contacts = []

#shows the contacts 
def printUpdated():
    print("-----CONTACTS-------")

    #sorts by name in alphabetical order
    contacts.sort(key = lambda x : x.name)

    for item in contacts:
        print(item)
    print("--------------------")

#added contacts
def addContact():
    name = input("Enter name: ")
    phone = input("Enter phone:")
    email = input("Enter email:")
    newCts = Contact(name, phone, email)
    contacts.append(newCts)
    
# removed, 
def removeContact():
    name = input("Enter name to remove: ")
    for cts in contacts:
        if name == cts.name:
            tempCts = cts
            contacts.remove(tempCts)

#search for contact
def searchContact():
    name = input("Enter name to search: ")
    for cts in contacts:
        if name == cts.name:
            tempCts = cts
            print("-----CONTACT FOUND-------")
            print(tempCts)
            print("--------------------------")

#save to file
#write() and writelines() methods will overwrite the contents of the file.
def saveToFile():
    with open('savefile.txt', 'w') as fp:
       for cts in contacts:
        ctsStrng = str(cts)
        fp.write(ctsStrng + '\n')

#start up 
with open('contactinfo.txt', encoding="utf-8") as fp:
    for line in fp:
        name, phone, email = line.split(' ', 2)
        cts = Contact(name, phone, email.removesuffix('\n'))
        contacts.append(cts)


while True:
    print("Command: show, add, remove, search, save, exit" )
    command = input("Enter command: ")
    pieces = command.split(' ')
   
    match pieces:
        case [('exit' | 'quit')]:
            break
        case [('add' | 'new')]:
            addContact()
        case ['show']:
            printUpdated()
        case [('remove' | 'delete')]:
            removeContact()
        case [('search' | 'look'),]:
            searchContact()
        case ['save']:
            saveToFile()
        case _:
            print("Command not understood: " + command)  

