#! python3

# The Collatz Sequence

try:
    x = int(input('Please enter a number: '))
    while x != 0: 
        if x % 2 == 0:
            x = x // 2
            print(x)
            if x == 1:
                print('Sequence complete')
                break
            else:
                continue
        elif x % 2 == 1:
            x = 3 * x + 1
            print(x)
except ValueError:
    print('You need to enter a valid integer')