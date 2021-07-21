import time

# list to hold the sequence
fib_numbers = [0, 1]


def fibonacci():
    while True:
        a = sum(fib_numbers)
        fib_numbers.append(a) # Adds the next number to the end of the list
        del fib_numbers[0] # deletes the integer at index 0
        print(fib_numbers[1])
        time.sleep(0.25)

fibonacci()
