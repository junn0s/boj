def FizzBuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
first = input()
second = input()
third = input()

num = 0
if first.isdigit():
    num = int(first) + 3
elif second.isdigit():
    num = int(second) + 2
elif third.isdigit():
    num = int(third) + 1
    
FizzBuzz(num)