# # Task 1: Reverse a string
# original_string = "hello world"
# reversed_string = original_string[::-1]
# print(reversed_string)

# # Task 2: Capitalize a Letter
# print(original_string.title())

# # Task 3: Palindrome
# phrase = input("Please enter a word: ")
# phrase = phrase.lower()
# reversed_phrase = phrase[::-1]
# if phrase == reversed_phrase:
#     print("This word is a Palindrome!")
# else:
#     print("Not a Palindrome.")

# # Task 4: Compress a string of characters
# string_to_compress = 'aaaaabbbeeeecccckkkssjjjjewe'
# compressed_string = ''
# string_length = len(string_to_compress)
# index = 0
# while index != string_length: #starts/restarts/ends loop
#     count = 1 #resets count
#     while (index < string_length - 1) and (string_to_compress[index] == string_to_compress[index + 1]): #counts char's, if new char move to if statement
#         count += 1 #counts same character in string
#         index += 1 #tracks where index in string is
#     if count == 1: #if new character in string
#         compressed_string += str(string_to_compress[index]) #if only one char, adds to compressed string
#     else:
#         compressed_string += str(string_to_compress[index]) + str(count)#takes previous character and pairs with character count. Adds to compressed string
#     index += 1 #moves to next index in original string after compression
# print(compressed_string) #compressed string complete, prints


################################################################################################################################


# def calc_happy_num(happy_number):
#     placeholder = []
#     index = 0
   
#     split_happy_number = [int(a) for a in str(happy_number)]
#     string_length = len(split_happy_number)
#     print(f'{split_happy_number} \nString length: {string_length}\n')

#     while index in range(string_length):
#         num_to_sqre = split_happy_number[index]
#         #print("index: ", index)
#         print("num to sq: ", num_to_sqre)

#         num_sqrd = num_to_sqre ** 2
#         print("num sqrd: ", num_sqrd)

#         placeholder.append(num_sqrd)
#         print("placeholder: ", placeholder)

#         iteration = index + 1
#         print(f"iteration: {iteration} \n")
#         index += 1
#     # placing new numbers into list
#     split_happy_number = placeholder
#     print(split_happy_number)
#     adding(split_happy_number)

# def adding(split_happy_number):
#     sum_of_list = sum(split_happy_number) 
#     print(sum_of_list)
#     # set happy number to new number and start loop over
#     happy_number = sum_of_list
#     if happy_number == 1:
#         try_again = input("Would you like to try a new number? Y/N: ")
#         try_again = try_again.lower()
#         if try_again == 'y':
#             main()
#         else:
#             print("Quitting program...")
#             quit()
#     calc_happy_num(happy_number)

# def main(): 
#     list_of_happy_numbers = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 
#     129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293]
#     split_happy_number = []
#     is_not_in_list = True
#     index = 0
#     happy_number = int(input("\nPlease enter happy number from 1 to 293: "))

#     while(is_not_in_list):
#         if happy_number in list_of_happy_numbers:
#             calc_happy_num(happy_number)
#         else: 
#             print(f'{happy_number} is not a happy number, please enter a happy number.\n')
#             main()

# main()

## Task Three Fibonacci
# def user_input_fib_seq():
#     fib_list = [0]
#     numbers = 0
#     user_input = int(input("Enter a number to start Finonacci Sequince: "))
#     fib_list.append(user_input)

#     while numbers in range(20):
#         new_value = fib_list[-2] + fib_list[-1]
#         fib_list.append(new_value)
#         numbers += 1
#     if numbers == 20:
#         print(fib_list)  

# user_input_fib_seq()