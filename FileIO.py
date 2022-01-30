#File I/O Example
  
# Opening a file
saveFile = open('save.txt', 'w') #if "save.txt" doesn't exist, it's created here!
inventory = ["\nkey\n", "bread\n", "dirty sock\n"]
PlayerName = "Clambraham Moregil\n"
money = 5
  
#write stuff to the file
saveFile.write(PlayerName) #for writing one thing
saveFile.write(str(money)) #I think the write function only wants strings
saveFile.writelines(inventory) #for lots of stuff
saveFile.close()
  
#testing if it worked:
saveFile = open('save.txt', 'r')
print("here's what we just saved:")
print(saveFile.read())
saveFile.close()

#read each line
saveFile = open('save.txt', 'r')
NewPlayerName = saveFile.readline()
NewMoney = saveFile.readline()
NewInventory = saveFile.read() #read the rest of the file (i think this saves to a tuple?)
saveFile.close()

#test again:
print("Printing out new variables just loaded:")
print(NewPlayerName)
print(NewMoney)
print(NewInventory)


