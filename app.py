import  random

secret_num = random.randint(1, 10)
guess_counter = 0
guess_limit = 3
while guess_counter < guess_limit:
    guess = int(input("Guess : "))
    guess_counter += 1
    if guess == secret_num:
        print("Congratulations! You guessed it!")
        break
else :
    print("Sorry, You failed")