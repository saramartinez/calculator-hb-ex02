def add(list_of_numbers):
    sum_of_all_numbers = 0
    for each_num in list_of_numbers:
        sum_of_all_numbers += int(each_num)
    print sum_of_all_numbers
    return sum_of_all_numbers

def subtract(list_of_numbers):
    subtraction = 0
    for each_num in list_of_numbers:
        subtraction -= int(each_num)
    print subtraction
    return subtraction

def multiply(list_of_numbers):
    multiplication = 1
    for each_num in list_of_numbers:
        multiplication *= int(each_num)
    print multiplication
    return multiplication

def divide(list_of_numbers):
    if "0" in list_of_numbers:
        print "You cannot divide by zero."
        return
    else:
        quotient = float(list_of_numbers[0])
        for each_num in list_of_numbers[1:]:
            quotient /= float(each_num)
        print quotient
        return quotient

def square(list_of_numbers):
    if len(list_of_numbers) > 1:
        print "You can only square one number. Use 'pow' for exponential computations."
        return
    else:
        for num in list_of_numbers:
            square = int(num) * int(num)
        print square
        return square

def cube(list_of_numbers):
    if len(list_of_numbers) > 1:
        print "You can only cube one number. Use 'pow' for exponential computations."
        return
    else:
        for num in list_of_numbers:
            cube = int(num) * int(num) * int(num)
        print cube
        return cube

def power(list_of_numbers):
    if len(list_of_numbers) < 2:
        print "You need at least two numbers for exponential computations. Use 'square' or 'cube' for those functions."
        return
    if len(list_of_numbers) == 2:
        exponent = int(list_of_numbers[0]) ** int(list_of_numbers[1])
        print exponent
        return exponent
    else:
        exponent = int(list_of_numbers[0])
        for each_num in list_of_numbers[:-1]:
            exponent **= int(each_num)
        print exponent
        return exponent

# def mod(num1, num2):
#     return num1 % num2

while True:

    tokens = raw_input("> ").split(" ")

    if tokens[0] == 'q' or tokens[0] == 'Q':
        break
    elif tokens[0] == "+":
        add(tokens[1:])
    elif tokens[0] == "-":
        subtract(tokens[1:])
    elif tokens[0] == "*":
        multiply(tokens[1:])
    elif tokens[0] == "/":
        divide(tokens[1:])
    elif tokens[0] == "square":
        square(tokens[1:])
    elif tokens[0] == "cube":
        cube(tokens[1:])
    elif tokens[0] == "pow" or "power":
        power(tokens[1:])
#     elif tokens[0] == "mod":
#         mod(tokens[1:])
    else:
        print "Does not compute"