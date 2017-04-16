# This script contains a program for a simple guessing game!

# Define a function `print_hot_or_cold()` that takes in two arguments (the `target`
# and the `guess`), and prints out an appropriate message based on how close
# the guess is to the target:
#
# Distance    Message
# -------------------
# The same    "got it!"
# Within 1	  "scalding hot"
# Within 3	  "very warm"
# Within 5	  "warm"
# Within 8	  "cold"
# Within 13	  "very cold"
# > 13 away	  "icy freezing miserably cold"
#
# Be sure to consider both positive AND negative distances!
# BONUS: Also print out whether the guess is high or low

   
def print_hot_or_cold(target,guess):
    difference=(int(guess)-int(target))
    distance = abs(difference)
    if distance == 0:
        print("got it!") 
    elif distance == 1:
        print("scalding hot") 
    elif distance <= 3:
        print("very warm")
    elif distance <= 5:
        print("warm") 
    elif distance <= 8:
        print("cold") 
    elif distance <= 13:
        print("very cold") 
    else:
        print("icy freezing miserably cold") 
    if difference < 0:
        print("You're low.")
    elif difference > 0:
        print("You're high.")
    


# Define a function `guess_number()` that takes a single argument (a target number)
# and prompts the user for a guess using the `input()` method. Your function should
# then print how close the user's guess is (use your previous function!). Note that
# you will need to convert the input into a number.
#
# Once you have a single guess working, modify your function so that the user can
# make MULTIPLE guesses. You can either do this using a loop (see the next module)
# or by simply calling your `guess_number() method again IF the user didn't get
# the answer right. This is an example of **recursion**.


def guess_number(target):
    user_guess = int(input("What's your guess? "))
    print_hot_or_cold(target,user_guess)
    if target != user_guess:
        guess_number(target)


# If the file is run as a top-level script, your script should pick a random number
# between 1 and 50 as the target and then start the game. You should inform the
# use of the range of numbers before asking them for a guess.

if __name__ == "__main__":
    # execute only if run as a script
    from random import randint
    target = randint(1,50)  
    print("I'm thinking of a number between 1 and 50. Try and guess it.")
    guess_number(target)