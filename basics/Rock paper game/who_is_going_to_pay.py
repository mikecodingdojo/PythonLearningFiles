import random 
from time import gmtime, strftime

what_time_is_it = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

names = input("Enter the names of people to randomly select for payment: ")
people = names.split(",")
length_list = len(people)
eatting_time = ""

times_of_day = input("Enter B for breakfast L for lunch D for dinner")

if times_of_day == 'B' or times_of_day == 'b':
    eatting_time = "Breakfast"
elif times_of_day == 'L' or times_of_day == 'l':
    eatting_time = "Lunch"
elif times_of_day == 'D' or times_of_day == 'd': 
    eatting_time = "Dinner"
else:
    eatting_time = "Whatever"


print("\n")
pay_up=random.randint(0, length_list-1)
print(f"The time is {what_time_is_it} \n")
print(f"Looks like {people[pay_up]} is going to pay {times_of_day}")