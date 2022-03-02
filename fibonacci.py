# Fibonacci Sequence
# -------------------
#
# Formula:
# fib(n) = fib (n-1) + fib (n-2)

# Attempt 1 -----------------------------------------
fib_list = [0, 1]

input_number = int(input("Please enter a number: "))

big_o = 0


for i in range(input_number - 1):
    calculated_number = (fib_list[i]) + (fib_list[i + 1])
    fib_list.append(calculated_number)

    big_o += 1
    print(calculated_number)

print(fib_list)
print("Big O:", big_o)

# Attempt 2 -------------------------------------- Using Recursion
n_input = int(input("Please enter a number: "))

big_o = 0


def fibonacci_sequence(n):
    global big_o
    big_o += 1
    if n <= 1:
        return n
    else:
        #  Formula: fib(n) = fib(n-1) + fib(n-2)
        return(fibonacci_sequence(n-1) + fibonacci_sequence(n-2))


for i in range(n_input + 1):
    print(fibonacci_sequence(i))

print("Big O:", big_o)
