#wap to demonstrate try, except and else


try:
    n = int(input("Enter a number:"))
    res = 10 / n
except ZeroDivisionError:
    print("ERROR: Cannot divide by 0.")
except ValueError:
    print("ERROR: Invalid input. Please enter a valid number.")
else:
    print(f"Result:{res}")

print("\n")
print("Written and Executed by DHAANI SANGWAN(0221BCA060)")