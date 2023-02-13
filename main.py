# Python Dice Roll Simulator

# Improting the random module to generate aa randomm number
import random

# Dice rolling function
def roll2Dice():
    dice_sum = 0
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    dice_sum = dice_one + dice_two
    print(str(dice_one) + "," + str(dice_two) + " (sum: " +     str(dice_sum) + ")")
    return dice_sum

# Main Program Loop
loop = True
while loop:
  # Print Main Menu
  print("\nDice Roll Simulator Menu")
  print("1. Roll Dice Once")
  print("2. Roll Dice 5 Times")
  print("3. Roll Dice ‘n’ Times")
  print("4. Roll Dice until Snake Eyes")
  print("5. Exit")

  # Get Menu Selection from User
  selection = input("Enter Selection (1-5): ")

  # Take Action Based on Menu Selection 
  # Option 1
  if selection == "1":
    # Roll Dice Once
    print("\nRoll Dice Once")
    roll2Dice()
  # Option 2
  elif selection == "2":
    # Roll Dice Five Times
    print("\nRoll Dice Five Times")
    n = 1
    for n in range(5):
      roll2Dice()
  # Option 3
  elif selection == "3":
    # Roll Dice `n` Times
    n = int(input("\nHow many rolls would you like?"))
    while n >= 1:
      roll2Dice()
      n -= 1
      
  # Option 4
  elif selection == "4":
    print("\nRoll Dice Until Snake Eyes")
    the_dice_sum = roll2Dice()
    count = 0
    while the_dice_sum != 2:
      count += 1
      the_dice_sum = roll2Dice()
    print("Snake Eyes! It took " + str(count) + " rolls to get snake eyes.")
    
  # Option 5
  elif selection == "5":
    print("EXIT")
    loop = False
