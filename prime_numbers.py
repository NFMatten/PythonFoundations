prime_number_list = []

def prime_number_calc(number_input):
    if number_input > 1:
        for numbers in range(2, int(number_input ** 0.5) + 1):
            if number_input % numbers == 0:
                return False
        prime_number_list.append(number_input)
        return True

def inputting_numbers():
    number_input = 0
    for number_input in range(100):
        number_input += 1
        prime_number_calc(number_input)
        if number_input == 100:
            print(prime_number_list)
            
inputting_numbers()