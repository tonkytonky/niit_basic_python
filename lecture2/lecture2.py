# Задание 1
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)


numbers_list = range(1, 101)
# Задание 2
result_for = 0
for number in numbers_list:
    result_for += number
print('Sum using `for`:', result_for)


# Задание 3
result_while = 0
counter = 0
while counter < len(numbers_list):
    result_while += numbers_list[counter]
    counter += 1
print('Sum using `while`:', result_while)
