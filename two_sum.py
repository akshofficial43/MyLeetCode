# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

num = [int(x) for x in input("enter number = ").split()]
target = int(input("enter target = "))
# output -> [1,3]

# for i in num: # this give problem repeatation like(2+4=6, 3+3=6, 4+2=6)
# beacuse Here 'i' is a actual value of list when we print 'i' in loop its give value of list(0,1,2,3)
# we cant acces with index of list with this 'i' like num[i]
for i in range(len(num)): # so we use this range(len(num)) its take a undex of list in 'i', here len = 4 so range is 4=[0,1,2,3] so avoid repetion
    # if target - i in num: # 2, 3, 4
    for j in range(i + 1, len(num)): # here j is always j > i ([0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3], [2,4], [3,4]) thats why avoid repeat 
        if num[i] + num[j] == target: 
            print(f"{num[i]} + {num[j]} = {target}")
            print(f"[{i}, {j}]")




#with class and function
class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                if num[i] + num[j] == target:
                    return [i, j]

sol = Solution()
num = [2, 7, 11, 15]
target = 9
print(sol.twoSum(num, target))
