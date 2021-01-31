"""

Project Euler: Problem 1

If we list the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all multiples of 3 or 5 below 1000.

"""

# Return sum of multiples of 3 or 5 up to a given number n
def sumOfMultiples(n):
    sum = 0

    for i in range(0, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum

print("The sum of all multiples of 3 or 5 below 1000: " +
    str(sumOfMultiples(1000)))
