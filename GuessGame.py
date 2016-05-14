from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
     guess = int(raw_input ("What is your guess: "))
     print "Your current guess is: " + str(guess)
     if guess == random_number:
        print "you win"
        print "The random number was: " + str(random_number)
        break
     guesses_left -= 1
     print "Number of guesses left " + str(guesses_left) + "!"
else:
    print "your guesses are over. You Lose"
    print "The random number was: " + str(random_number)