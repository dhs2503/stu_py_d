#positional arguments
def greet(name, age): 
    print(f"Hello, {name}! You are {age} years old.")
print("\n")


#keyword arguments
def greet(name, age): 
    print(f"Hello, {name}! You are {age} years old.")
print("\n")


#default arguments
def greet(name, age=25): 
    print(f"Hello, {name}! You are {age} years old.")
print("\n")


#variable length arguments - *args
def sum_numbers(*args): 
    return sum(args) 
print(sum_numbers(1, 2, 3))# Output: 6 
print(sum_numbers(4, 5, 6, 7, 8)) # Output: 30
print("\n")


#variable length arguments - *kwargs
def print_info(**kwargs): 
    for key, value in kwargs.items(): 
        print(f"{key}: {value}") 
print_info(name="Alice", age=30, city="New York")
print("\n")

print("This program is Written and Executed by DHAANI SANGWAN(0221CA060)")
