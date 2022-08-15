# Task 1: Accessing a Value
print("Task One: ")
languages = ['JavaScript', 'Python', 'Java', 'Django', 'React']
print(languages[1], "\n")

# Task 2: Adding and Changing Values
print("Task Two: ")
instructors = ['Nevin', 'Mike', 'Jake', 'Dan', 'Megan']
instructors.append('Dan')
instructors.append('James')
instructors.append('John-Boy')
instructors[5] = "Danimal"
print(instructors, "\n")

# Task 3: Popping a value
print("Task Three: ")
popped_instructor = instructors.pop()
print(f'Popped instructor: {popped_instructor}\n{instructors}\n')

# Task 4: Removing a value
print("Task Four: ")
instructors.remove('Mike')
print(instructors, "\n")

# Task 5: Looping over a List
print("Task Five: ")
first_list = ['fan', 'bull-', 'high-', 'barrel-o-', 'slap']
second_list = ['dango', 'rider', 'horse', 'monkeys', 'stick']

counter = 0
for index in range(5):
    print(first_list[counter] + second_list[counter])
    counter += 1
print("\n")

# Task 6: List Function
def list_of_instructors(instructors, first_name):
    is_not_duplicate = False
    print("_" * 53,)
    print(f'{instructors}')
    print("\u203e" * 53, "\n\n")
    while is_not_duplicate == False:
            if first_name in instructors:
                print('Sorry that name has been taken, please provide a nickname.')
                is_not_duplicate = False
                do_the_stuff()
            elif first_name not in instructors:
                instructors.append(first_name)
                print(f'{first_name} added to the list! {instructors}\n')
                is_not_duplicate = True
                do_the_stuff()

def do_the_stuff():
    first_name = input("Please enter a Name or type quit: ")
    if first_name == "quit":
        print("Moving to Task 7...\n")
        task_7()
    else:
        list_of_instructors(instructors, first_name)

# Task 7: Joining Lists
def task_7():
    traveling_to_west = ['hawaii', 'okinawa', 'thailand']
    traveling_to_east = ['germany', 'poland']
    print(f'To the West: \n\t{traveling_to_west}')
    print(f'To the East: \n\t{traveling_to_east}')
    print(f'Combined list using "+" method: \n\t{traveling_to_west + traveling_to_east}')

    for combined_list in traveling_to_west:
        traveling_to_east.append(combined_list)
    print(f'Append function: \n\t{traveling_to_east}')

    traveling_to_west = ['hawaii', 'okinawa', 'thailand']
    traveling_to_east = ['germany', 'poland']
    for new_combined_list in traveling_to_west:
        traveling_to_east.extend(new_combined_list)
    print(f'Extend function: \n\t{traveling_to_east}')

    task_8()

# Task 8: Copy Lists
def task_8():
    favorite_vehicles = ['infiniti', 'dodge', 'nissan']
    print(f"Task 8:\nFavorite Vehicle List: {favorite_vehicles}")

    copy_1 = []
    counter = 0
    for index in favorite_vehicles:
        new_car = favorite_vehicles[counter]
        copy_1.append(new_car)
        counter += 1
    print(f'Printing first copy: {copy_1}')

    copy_2 = []
    copy_2 = favorite_vehicles.copy()
    print(f'Printing [copy()] Copy: {copy_2}')

    copy_3 = []
    copy_3 = list(favorite_vehicles)
    print(f'Printing [list()] Copy: {copy_3}')

    task_9()

# Task 9 Sort Lists
def task_9():
    foods = ['pizza', 'chicken', 'steak', 'burger', 'pasta']
    foods.sort()
    print(foods)
    foods.sort(reverse = True)
    print(foods)

do_the_stuff()