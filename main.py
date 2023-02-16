import math
numbers = []

def sum_of_digits(num : int):
    real_number = num
    sum_of_digits = 0
    if (num > 0) & (1 <= len(str(num)) <= 10):
        while num > 0:
            count = num % 10
            num //= 10
            sum_of_digits += count
        print(f"The sum of the digits of the number {real_number} is: ", round(sum_of_digits))
    else:
        print(f"The sum of the digits of the number {real_number} is: The number does not satisfy the condition of the problem!!!")

file = open("test_numbers.csv", 'r')
numbers = [line.strip() for line in file]
print(numbers)
for i in numbers:
    i = int(i)
    sum_of_digits(i)