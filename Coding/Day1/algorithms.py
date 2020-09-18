# 1. Return the number of perfect squares (like 4, 16, 25, 36, etc.) between two integers a and b, inclusive
# 2. Write a Python program to calculate the value of 'a' to the power 'b'. Test Data : (power(3,4) -> 81
# 3. Write a program that calculate the number of vowels used in a sentence. Example: input = "The elephant is walking in the enclosure!"
    # Output: e = 5 a = 2 i = 2 
# 4. Fibonacci numbers
# 5. Using python write figure out how you could find and return the sum of all the multiples of 7 or 11 below 1000. def theSum 

def perfect_squares(min, max):
    start = int(min)
    stop = int(max)
    numbers = []
    squares = []

    for i in range(start, (stop + 1)):
        numbers.append(i)
    
    for num in numbers:
        for i in range(1, len(numbers)):
            if num / i == i:
                squares.append(num)

    print(squares)

def power_of(first, second):
    
    power = first ** second

    return print(power)

def count_vowels(string):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    y = 0

    for letter in string:
        if letter == "a":
            a += 1
        elif letter == "e":
            e += 1
        elif letter == "i":
            i += 1
        elif letter == "o":
            o += 1
        elif letter == "u":
            u += 1
        elif letter == "y":
            y += 1
    
    return print(f"There are {a} a's, {e} e's, {i} i's, {o} o's, {u} u's, and sometimes {y} y's in your string.")

def fibonacci(start, stop):
    nums = []

    for i in range(start, (stop + 1)):
        if len(nums) < 2:
            nums.append(i)
        else:
            new_num = nums[-1] + nums[-2]
            nums.append(new_num)

    return print(nums)

def theSum():
    multiples = []

    for i in range(1, 1001):
        if i % 7 == 0 or i % 11 == 0:
            multiples.append(i)

    return print(multiples)

