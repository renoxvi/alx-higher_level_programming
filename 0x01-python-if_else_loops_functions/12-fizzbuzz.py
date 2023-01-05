#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz \n', end='')
        elif i % 3 == 0:
            print('Fizz \n', end='')
        elif i % 5 == 0:
            print('Buzz \n', end='')
        else:
            print('{} \n'.format(i), end='')
