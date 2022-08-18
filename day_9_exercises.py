# Task 1: Reverse a string
normal_string = "Hello"
reversed_string = ''
for items in range(len(normal_string) -1, -1, -1):
    reversed_string += normal_string[items]
print(reversed_string)

# Task 2: Capitalize a Letter
original_string = "hello world!"
print(original_string.title())

# Task 3: Palindrome
phrase = input("Please enter a word: ")
phrase = phrase.lower()
reversed_phrase = phrase[::-1]
if phrase == reversed_phrase:
    print("This word is a Palindrome!")
else:
    print("Not a Palindrome.")

# Task 4: Compress a string of characters
string_to_compress = 'aaaaabbbeeeecccckkkssjjjjewe'
compressed_string = ''
string_length = len(string_to_compress)
index = 0
while index != string_length: #starts/restarts/ends loop
    count = 1 #resets count
    while (index < string_length - 1) and (string_to_compress[index] == string_to_compress[index + 1]): #counts char's, if new char move to if statement
        count += 1 #counts same character in string
        index += 1 #tracks where index in string is
    if count == 1: #if new character in string
        compressed_string += str(string_to_compress[index]) #if only one char, adds to compressed string
    else:
        compressed_string += str(string_to_compress[index]) + str(count)#takes previous character and pairs with character count. Adds to compressed string
    index += 1 #moves to next index in original string after compression
print(compressed_string) #compressed string complete, prints