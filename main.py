user_name = input("What is your name? ")
user_guesses = 1
correct_number = 7

print(f"Welcome to the guessing game {user_name}. I'm going to choose a number and you are going to have to guess it. The number is between 1 and 10.")

print("Picking a number...")

user_number = int(input('OK done. What number do you think I picked? '))

while user_number != correct_number:
  user_number = int(input('Incorrect, try again. Pick another number: '))
  user_guesses = user_guesses + 1

print(f"That's right, great guess!")