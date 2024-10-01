# Demonstrating bitwise operators in Python

a = 10  # 1010 in binary
b = 4   # 0100 in binary

# AND Operator
print(f"{a} & {b}: {a & b} (binary: {bin(a & b)})")

# OR Operator
print(f"{a} | {b}: {a | b} (binary: {bin(a | b)})")

# XOR Operator
print(f"{a} ^ {b}: {a ^ b} (binary: {bin(a ^ b)})")

# NOT Operator
print(f"~{a}: {-a} (binary: {bin(-a)})")

# Left Shift Operator
print(f"{a} << 1: {a << 1} (binary: {bin(a << 1)})")

# Right Shift Operator
print(f"{a} >> 1: {a >> 1} (binary: {bin(a >> 1)})")

print("This code was written and demonstrated by DHAANI SANGWAN(0221BCA060)")