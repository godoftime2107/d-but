hashtable = [None,None,None,None,None,None,None,None,None,None,None]

print("HASHTABLE")
print("[INDEX][INT DATA VALUE]")
for i in range(0,len(hashtable)):
    print("[{}]".format(i) + "[{}]".format(hashtable[i]))

flag = False
for i in range(0,len(hashtable)):
    if hashtable[i] != None:
        flag = True
    else:
        flag = False

if flag == True:
    print("Hashtable is full. Please remove a data value from the hashtable and try again.")
    quit()

val = int(input("Enter an integer to be stored: "))

#mid-square method
squared = str(val**2)

if len(squared) % 2 == 0:
    middle = squared[(len(squared)/2)-1] + squared[len(squared)/2]
else:
    middle = squared[round((len(squared)/2))-1] + squared[round(len(squared)/2)]

iaddress = int(middle) % 11
address = iaddress

while hashtable[address] != None:
    print("Space [{}] in the hashtable already has a value in it.".format(address))
    print("Searching for the next available space...")
    if address == len(hashtable) - 1:
        address = 0
    else:
        address += 1
    
hashtable[address] = val
print("The value {} was successfully stored in space [{}] in the hashtable.".format(val,address))
            
    
