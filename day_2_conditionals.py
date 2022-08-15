from random import randint

# Task 1: Driving age
def task_one():
    print("\nTask One: ")
    driving_age = 16
    users_age = int(input("Please enter your age: "))

    if users_age >= driving_age:
        print("You are legally able to drive.")
    elif users_age < driving_age:
        print("You are not old enough to drive yet.")

# Task 2: Random Number
def task_two():
    print("\nTask Two: ")
    random_number = randint(0, 10)
    if random_number >= 0 and random_number <= 2:
     print("The number is 0, 1 or 2;", random_number)
    elif random_number >= 3 and random_number <= 5:
      print("The number is 3, 4 or 5;", random_number)
    elif random_number >= 6 and random_number <= 8:
      print("The number is 6, 7 or 8;", random_number)
    elif random_number >= 9 and random_number <= 10:
       print("The number is 9 or 10;", random_number)

# Task 3: NFL Teams
def task_three():
    print("\nTask Three: ")
    user_input_nfl_team = input("Please enter NFL Team: ")
    lowercase_nfl_team = user_input_nfl_team.lower()
    
    if lowercase_nfl_team == "bears":
        print("Quarterback much?\n")
    elif lowercase_nfl_team == "vikings":
        print("Loud noises!\n")
    elif lowercase_nfl_team == "lions":
        print("LOL! They bad!\n")
    elif lowercase_nfl_team == "packers":
        print("Best team in the World! Actually, the universe!\n")
    else:
        print("Pick a different team.")
        task_three()

def do_all_the_tasks():
    task_one()
    task_two()
    task_three()

do_all_the_tasks()