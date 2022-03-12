import random 

maxrange = input("Enter the Maximum number: ")

#input has to be digit
if maxrange.isdigit():
    # we have to convert "num" string into "num" int. [conversion]
    maxrange = int(maxrange)

    # check inut is > 0
    if maxrange <= 0:
        print("Enter the number greater than 0.")
        quit()
else:
    print("Oops! Enter a number.")
    quit()

num = random.randint(0, maxrange) 
#generate random number between 0 & 12 including 0 and excluding 12
#num = random.randrange(0, 12)
# randint also include 12

#for making guess limit
guesses = 0

# to make a input for user to take a guess
while True:
    guesses += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:  
        print("Oops! Enter a number.")
        continue # it will bring back to the top of this loop 

    if guess == num:
        print(' You got it')
        break
    else:
        # to tell user that their guess approx
        if guess > num:
            print("Oh man! you went a little ahead")
        else:
            print("oh man! you are below the number ")


print("You got it in", guesses, "guesses")        
 