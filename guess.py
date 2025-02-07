import random
def GuessNumber():
    print("Guess a Number 1 - 10")
    number = random.randint(1,10)
    guess= int(input("Enter your guess: "))

    if guess == number:
        print("Winner")
        print("The number was",number)
    elif guess < number :
        print("Too low")
        print("The number was",number)
    elif guess > number:
        print("Too high")
        print("The number was",number)        
    else:
       print("loser")
       print("The number was",number)
    

    
        
