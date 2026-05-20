#!/usr/bin/python3

def fizzbuzz(n):
    iter = 1
    while iter <= n:
        if (iter % 3) == 0 and (iter % 5) == 0:
            print("Fizzbuzz")
        elif(iter % 3) == 0:
            print("Fizz")
        elif (iter % 5) == 0:
            print("Buzz")
        else:
            print(iter)
        iter = iter + 1
def run_fizzbuzz(limit):
    fizzbuzz(limit)
run_fizzbuzz(100)