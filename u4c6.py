#early exit w return
def find(nums):
    for n in  nums:
        if n % 2 == 0:
            return n
    return None

num = [1,3,5,8,9]
even = find(num)
print(f"The first even number is {even}")

print("\n This program is Written and Executed by DHAANI SANGWAN(0221BCA060)")