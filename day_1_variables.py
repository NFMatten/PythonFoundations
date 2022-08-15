# Task 1
my_age = 32
print(f'\nI am {my_age} years old.\n')

# Task 2,3 and 4
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
full_name = first_name + ' ' + last_name
print(f'\nMy first name is {first_name} and my last name is {last_name} and full name is {full_name}.\n')

# Task 5
fahrenheit = input("Enter Degrees(F): ")
fahrenheit_converted = int(fahrenheit)
fahrenheit_to_celsius = (fahrenheit_converted-32)*(5/9)
celsius = fahrenheit_to_celsius
celsius_rounded = round(celsius, 2) # round(float, decimal_places)
print(f'{fahrenheit} degrees Fahrenheit is {celsius_rounded} degrees Celsius\n\n')