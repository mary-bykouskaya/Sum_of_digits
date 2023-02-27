import math
numbers = []

def sum_of_digits(num : int):
    real_number = num
    sum_of_digits = 0
    print(f"The sum of the digits of the number {real_number} is: ", end='')
    if (num > 0) & (1 <= len(str(num)) <= 10):
        while num > 0:
            count = num % 10
            num //= 10
            sum_of_digits += count
        return sum_of_digits
    else:
        return "The number does not satisfy the condition of the problem!!!"

file = open("test_numbers.csv", 'r')
numbers = [line.strip() for line in file]
print(numbers)
for i in numbers:
    i = int(i)
    print(sum_of_digits(i))