#Program to Chain Generators
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

def squared_numbers(numbers):
    for number in numbers:
        yield number ** 2

for square in squared_numbers(count_up_to(5)):  # Correctly call the generator function
    print(square)  # Outputs: 1, 4, 9, 16, 25


print("\n This program is Written and Executed by DHAANI SANGWAN(0221BCA060)")