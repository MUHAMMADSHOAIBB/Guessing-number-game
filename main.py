import random
import pyautogui
# Declaring some variables
lower = 1
upper = 100
attempt = 0
chances_left = 10
target = random.randint(lower, upper)

# Show the first window
pyautogui.alert("Please Guess the number between \
1 and 100.\nYou've only 10 chances.")
# The while loop will iterate until the user
# attempts 10 guesses
while attempt < 10:
    attempt += 1

    guess = pyautogui.prompt(f"Chances left: {chances_left}\nPlease\
    guess the number.")

    # Checks if the guess matches with the target number
    # Convert the guess variable to an integer
    if int(guess) == target:
        pyautogui.alert(f"Congrats! You did it in {attempt} attempts.")
        break
    elif int(guess) < target:
        pyautogui.alert(f"You've chosen less.")
    elif int(guess) > target:
        pyautogui.alert(f"You've chosen high.")

    chances_left -= 1
    if attempt >= 10:
        pyautogui.alert(f"Sorry! you lost.\nThe number is: {target}.")