#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []
    for n in range(length):
        if n == 0:
            fibonacci_sequence.append(n)

        if n == 1:
            fibonacci_sequence.append(n)

        if n > 1:
            sum = fibonacci_sequence[-1] + fibonacci_sequence[-2]  
            fibonacci_sequence.append(sum)

    print(fibonacci_sequence)          