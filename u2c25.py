#py code to print sum of cube of the prime numbers between a given range

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    print(n)
    return True


def sum_of_cube(start, end):
    total_sum = 0

    for n in range(start, end + 1):
        if is_prime(n):
            total_sum += n ** 3
    return total_sum


start = int(input("Enter the starting of the range:"))
end = int(input("Enter the ending of the range:"))

result = sum_of_cube(start, end)

print(f"The sum of the cube of prime numbers between {start} and {end} is: {result}")
