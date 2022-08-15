# Task 1: First and Last Character from String
def first_and_last_char(nfl_team):
    str_1 = nfl_team[0]
    str_2 = nfl_team[-1]
    str_3 = str_1 + '' + str_2
    return str_3

returned_string = first_and_last_char('Packers')
print(returned_string)

# Task 2: Print 0-100; If number divisible by 3 print peanut butter; If divisible by 5 print Jelly; If both print Peanut Butter Jelly
def peanutbutter_jelly():
    for counting_numbers in range(101):
        print(counting_numbers)
        if ((counting_numbers % 3) == 0) and ((counting_numbers % 5) == 0):
            print("\033[A" "peanut butter jelly") # the "\033[A" bring the text to the correct location (one line up)
        elif (counting_numbers % 3) == 0:
            print("\033[A" "peanut butter")
        elif (counting_numbers % 5) == 0:
            print("\033[A" "jelly")
    print("\n")

peanutbutter_jelly()

# Task 3: Word-Letter Indexing
def word_letter_indexing(string_name):
    final_result = ''
    index = 0
    for char in string_name:
        str_1 = char
        str_2 = str(index)
        str_3 = str_1 + str_2
        final_result = final_result[::] + str_3[::]
        index += 1

    return final_result

returned_result = word_letter_indexing("World Peace")
print(returned_result)

# Task 4: Ingredient Search
def searching_for_ingredients(ingredients):
    index = 0
    try_again = True
    while try_again == True:
        user_input = input("Enter an ingredient to search: ")
        for item in ingredients:
            if user_input in ingredients:
                return user_input # Prefer to return element in list
            else:
                answer = input(f'{user_input} not in list. Search again? y/n: ')
                if answer == 'y':
                    break
                else:
                    try_again = False
                    break
                
ingredients = ['ground beef', 'cheese', 'ketchup', 'buns']
returned_ingredient = searching_for_ingredients(ingredients)
print(f'{returned_ingredient} is in the list of ingredients')

# Task 5: Reverse a List
def reverse_a_list():
    list_to_reverse = ['Yellow', 'Purple', 'Orange']
    reversed_list = []
    for items in range(len(list_to_reverse)):
        last_item = list_to_reverse.pop()
        reversed_list.append(last_item)
    print(reversed_list)

reverse_a_list()

# Task 6: Drop Four
def list_of_names(names):
    names_greater_than_4_char = []
    
    for item in names:
        item_length = len(item)
        if item_length > 4:
            names_greater_than_4_char.append(item)

    print(names_greater_than_4_char)

names = ['Rebecca', 'Sam', 'Bob', 'Dante', 'Monica', 'Brad']
list_of_names(names)


# Example function:
def display_name(name):
    print(name)
    #  this is the logic of the function

# The above function takes in a variable, known as the parameter.
# In this example, that variable is name.
# The function then prints to the console the value that is passed in


display_name('Mike')
display_name('Ian')
display_name('Nevin')

# Above we are now calling the function. This means using the function that we wrote.
# Here we are passing in an actual value. In this case, the value is 'Mike'

# Example 2


def add_one_to_number(number):
    number_one = 1
    add_one = number + number_one
    return add_one

# The above function takes in a variable, known as the parameter.
# In this example, that variable is number.
# The function then adds one to the parameter and returns the sum


result = add_one_to_number(30)

# Above we are now calling the function. This means using the function that we wrote.
# Here we are passing in an actual value. In this case, the value is 30
# We create and set a variable equal to the function call becuase the function returns a value

# Problem 1
# Write a function that takes in two numbers
# The logic of the function should add those two numbers together and return a sum
# Capture the returned value in a variable and print it to the console
def add_two_numbers(number_1, number_2):
    sum = number_1 + number_2
    return sum

returned_value = add_two_numbers(25, 82)
print(returned_value)

# Problem 2
# Write a function that takes in two strings
# The logic of the function should concatenate those two strings together and return the concatenated result
# Capture the returned value in a variable and print it to the console
def two_strings(str_1, str_2):
    str_3 = str_1 + " " + str_2
    return str_3

returned_str = two_strings("hello", "world")
print(returned_str)

# Problem 3
# Write a function that takes in a string
# The logic of the function should print each character of the string one at a time to the console
# HINT: for loop is one way to do this
def print_chars(string_name):
        for char in string_name:
            print(char)

print_chars("Hello World!")


# Problem 4
# Write a function that takes in a string
# The logic of the function should print the string to the console but only if that string has three or more characters in it
# If it is less than three characters, then print to the console 'we need a larger string to print!'
def string_larger_than_3_chars(input_string):
    if len(input_string) >= 3:
        print(input_string)
    else:
        print('we need a larger string to print!')

string_larger_than_3_chars('Hello World!')
string_larger_than_3_chars("123")
string_larger_than_3_chars("12")