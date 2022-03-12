print("Welcome to the game!")
 
#promt user for the input
# first declare a variable

playing = input("Do you want to play ? ")
#use tab for indentation
# .lower() make the input in lower
if playing.lower() != "yes":
    quit()

score = 0
print("Game is on")

answer= input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect! ")

answer = input("How many bits in a Byte? ")
if answer.lower() == "8":
    print("correct!")
    score += 1
else:
    print("Incorrect! ")

answer = input("What does GPU stand for ? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect! ")


answer = input("What does RAM stand for ? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect! ")

#to add int and string, we have to convert int(score) into string
print("Your score is: " + str(score))
print("Your percentage is: " + str((score/4)*100) + "%")
