def pattern1(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * i)
    print()

def pattern2(n):
    for i in range(1, n + 1, 2):
        print(' ' * ((n - i) // 2) + '*' * i)
    print()

def pattern3(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * i)
    print()

def pattern4(n):
    for i in range(1, n + 1, 2):
        print(' ' * ((n - i) // 2) + '*' * i)
    for i in range(n - 2, 0, -2):
        print(' ' * ((n - i) // 2) + '*' * i)
    print()

# Main function to take input and call pattern functions
def main():
    n = int(input("Enter the number of lines (odd number for patterns 2 & 4): "))
    
    print("Pattern 1:")
    pattern1(n)
    
    print("Pattern 2:")
    pattern2(n)
    
    print("Pattern 3:")
    pattern3(n)
    
    print("Pattern 4:")
    pattern4(n)

if __name__ == "__main__":
    main()


print("This program is written and executed by Harshit Sidher (0221BCA054)")