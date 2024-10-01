def pattern1(n):
    for i in range(1, n + 1):
        print('*' * i)
    print()

def pattern2(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()
    print()

def pattern3(n):
    for i in range(1, n + 1):
        print(str(i) * i)
    print()

def pattern4(n):
    for i in range(n, 0, -1):
        print('*' * i)
    print()

def pattern5(n):
    for i in range(n, 0, -1):
        for j in range(n, n - i, -1):
            print(j, end='')
        print()
    print()

def pattern6(n):
    for i in range(n, 0, -1):
        print(str(i) * i)
    print()

# Main function to take input and call pattern functions
def main():
    n = int(input("Enter the number of lines: "))
    
    print("Pattern 1:")
    pattern1(n)
    
    print("Pattern 2:")
    pattern2(n)
    
    print("Pattern 3:")
    pattern3(n)
    
    print("Pattern 4:")
    pattern4(n)
    
    print("Pattern 5:")
    pattern5(n)
    
    print("Pattern 6:")
    pattern6(n)

if __name__ == "__main__":
    main()


print("Written and executed by DHAANI SANGWAN(0221BCA060)")