import random

answer = random.randint(0,20)
fin = False

while fin != True:

    guess = int(input("Guess the number between 0 and 20: "))

    if guess == answer:
        print("Congratulations! You have guessed correctly")
        fin = True
    elif guess < answer:
        print("Wrong! Answer is HIGHER")

    elif guess > answer:
        print("Wrong! Answer is LOWER")
