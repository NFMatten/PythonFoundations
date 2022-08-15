## For Loops ##

# Task One: Five Hellos
print("\nTask One: ")
for print_hello in range(5):
    print("hello!")
print("\n")

# Task Two: Counting
print("\nTask Two: ")
for print_numbers in range(11):
    print(print_numbers)
print("\n")

# Task Three: Counting Backwards
print("\nTask Three: ")
for print_backwards in range(10,-1,-1):
    print(print_backwards)
print("\n")

# Task Four: Prompted Output
print("\nTask Four: ")
print_how_many_times = int(input("Please enter how many times to print: "))
for print_devCodeCamp in range(print_how_many_times):
    print('devCodeCamp')
print("\n")

# Task Five: Packers Split-up.
print("\nTask Five: ")
nfl_team = 'Packers'
for each_character in nfl_team:
    print(each_character)
print("\n")

# Task Six: Fizz Buzz.
print("\nTask Six: ")
# Part 1
for counting_numbers in range(101):
    print(counting_numbers)
    if ((counting_numbers % 3) == 0) and ((counting_numbers % 5) == 0):
        print("\033[A" "fizzbuzz") # the "\033[A" bring the text to the correct location (one line up)
    elif (counting_numbers % 3) == 0:
        print("\033[A" "fizz")
    elif (counting_numbers % 5) == 0:
        print("\033[A" "buzz")
print("\n")

## While Loops ##

# Task 7: Five Hellos. Write a while loop that will run 5 times and print "hello!" to the console 5 times.
print("For Loops \nTask 7:\n")
counter = 0
while counter < 5:
    print("hello!")
    counter += 1
print("\n")

# Task 8: Validation. Write a while loop that will prompt a user for their password and will continue to
#         prompt the user until the typed in password is correct. If correct, print to the console "User Validated".
original_password = input("Please enter a password: ")
is_correct_password = False

while is_correct_password == False:
    password_check = input("Please reenter password: ")
    if password_check != original_password:
        print("Incorrect password, please try again!\n")
    elif password_check == original_password:
        is_correct_password = True
        print("User Validated.")