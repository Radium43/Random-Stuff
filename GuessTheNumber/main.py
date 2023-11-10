import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    
    print("Number has been Picked chose a Number Between 1-100")

    attempts = 0

    while True:
        try:
            guess = int(input("please guess ur Number: "))
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Wow u did it.  number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")

        except ValueError:
            print("valid number.")

if __name__ == "__main__":
    guess_the_number()
