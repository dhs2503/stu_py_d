#return list through function
def get_sq(num):
    sq = [n ** 2 for n in num]
    return sq

nums = [1,2,3,4]
sql = get_sq(nums)
print(sql)

print("\n This program is Written and Executed by DHAANI SANGWAN(0221BCA060)")