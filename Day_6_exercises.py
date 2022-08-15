# Task 1: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#         You may assume that each input would have exaclty one solution and you may not use the same element twice.
def task_1(target_number, list_of_numbers):
    result = 0
    for index in range(len(list_of_numbers)): #in order to move to the next element, line 6 must complete all elements in loop
        for index2 in range(len(list_of_numbers)):
            if list_of_numbers[index] + list_of_numbers[index2] == target_number:
                result = [index, index2]
                return result
            
list_of_numbers = [50, 17, 5, 77]
target_number = 55

results = task_1(target_number, list_of_numbers)
print(results)

# Task 2: Instructed to skip / not do

# Task 3: Given a list of integers, return a bool that represents whether or not all integers in the list can form a sequence of incrementing int's

def seq_numbers(numbers_list):
    numbers_list.sort()
    number = 0
    for number in range(len(numbers_list)):
        while number <= len(numbers_list):
                if (numbers_list[number] + 1) == numbers_list[number + 1]:
                    number += 1
                    if (numbers_list[number + 1]) == numbers_list[-1]:
                        break
                else: 
                    return False
        return True
    

def do_the_stuff():
    list1 = [5,7,3,8,6] #returns false, needs num 4
    list2 = [17,15,20,19,21,16,18]

    result1 = seq_numbers(list1)
    result2 = seq_numbers(list2)
    print(f'{list1} returns {result1}')
    print(f'{list2} returns {result2}')

do_the_stuff()