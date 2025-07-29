import random
rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)    
      (____)
---.__(___)
ROCK'''

paper = ''' 
     _______
---'    ____)____
           ______)
          _______)     
         _______)
---.__________)
PAPER'''

scissors = ''' 
    _______
---'   ____)____
          ______)
       __________)    
      (____)
---.__(___)
SCISSORS'''

print("\n                                           Welcome to Rock-Paper-Scissor Game!!!\nPress 0 for Rock\nPress 1 for Paper\nPress 2 for Scissor\n")

images = [rock,paper,scissors]

while True: 
    try:
        user_choice = int(input("\nWhat do you choose? : "))
        if user_choice <=2:
            print (images[user_choice]) 
        else: 
            print("Invalid Choice!! Please Choose Between 0 to 2")
            continue        
        computer_choice = (random.randint(0,2))
        print (images[computer_choice])
        if user_choice >= 3:
            print ("Invalid Choice!! Please Choose Between 0 to 2")
            continue
        elif user_choice == computer_choice:
            print("\nIT\'s A TIE")
        elif user_choice == 2 and computer_choice == 0:
            print("\nYOU LOSE!!")
        elif user_choice == 1 and computer_choice ==2:
            print("\nYOU LOSE!!")
        elif user_choice > computer_choice:
            print("\nYOU WON!!")
        elif user_choice == 0 and computer_choice == 1:
            print("YOU LOSE!!")    
        elif user_choice == 0 and computer_choice == 2:
            print("\nYOU WON!!")    
    except ValueError:
        print("Please enter a valid number (0, 1, or 2).")   