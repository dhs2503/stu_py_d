print("TYPES OF PARAMETERS:")
print("\n")

#positional parameter
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 30)
print("\n")


#default parameter
def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old")

greet("Alice")
greet("Bob", 30)
print("\n")


#keyword parameter
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(name="Alice", age = 30)
greet(age = 30, name = "Alice")
print("\n")


#variable length parameter
def sum_numbers(*args):
        return sum(args)
print(sum_numbers(1,2,3))
print(sum_numbers(4,5,6,7,8))
print("\n")


#var length parameter-2
def print_info(**kwargs):
     for key, value in kwargs.items():
          print(F"{key} : {value}")
print_info(name = "Alice", age = 30, city = "New York")
print("\n")

print("This program is Written and Executed by DHAANI SANGWAN(0221BCA060)")