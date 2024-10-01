#write a py code to demonstrate try and except

try:
    n = int(input("Enter a number:"))
    res = 10 / n
except ZeroDivisionError:
    print("ERROR: Cannot divide by 0.")
except ValueError:
    print("ERROR: Invalid input. Please enter a valid number.")


print("\n")
print("Written and Executed by DHAANI SANGWAN(0221BCA060)")