myfile = open("scores.txt", "r") #Open the "scores.txt" file in read mode
lines = myfile.readlines() #Read all lines from the file
myfile.close() 

# Convert each line to a tuple of (score, name) and store them in a list
scores = [(int(line.split()[0]), line.split()[1].strip()) for line in lines]

#print the stuff in the list
for score, name in scores: 
    print(score, " - ", name)
    
#insert game logic here!    

#get user info
user_score = int(input("Enter your score: ")) #this part should be automated in your game
user_name = input("Enter your name: ")

scores.append((user_score, user_name))#Append the user's score and name to the scores list
scores.sort(reverse=True) #Sort the scores list in descending order

while len(scores) > 10:
    scores.pop()
    
myfile = open("scores.txt", "w") #Open the "scores.txt" file in write mode
for score, name in scores:
    myfile.write(f"{score} {name}\n")
myfile.close()  # Close the file after writing
