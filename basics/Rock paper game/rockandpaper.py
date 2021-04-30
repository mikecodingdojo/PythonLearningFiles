import random 


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

mylist = [rock, paper, scissors]

user_choose = int(input("Choose 0 for rock, 1 for paper, or 2 for sciccors \n"))

computer_choose = random.randint(0, 2)
print(f" \n player {mylist[user_choose]} computer: {mylist[computer_choose]}")

if user_choose == 0 and computer_choose == 2:
    print("You Win!")
elif user_choose > computer_choose: 
    print("You Win!") 
elif user_choose == 1 and computer_choose == 2:
    print("You Lose!")
elif user_choose == 0 and computer_choose == 1: 
    print("You Lose!")
else:
    print("It's a Draw folks")





    