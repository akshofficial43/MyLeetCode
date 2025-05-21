num = int(input("enter = "))
temp = num # copy of num
rev = 0

while num > 0:
    rem = num % 10 
    # 1. 121 % 10 = 1
    # 2. 12 % 10 = 2
    # 3. 1 % 10 = 1 
    rev = rev * 10 + rem
    # 1. 0 * 10 + 1 = 1
    # 2. 1 * 10 + 2 = 12
    # 3. 12 * 10 + 1 = 121
    num //= 10
    # 1. 121 // 10 = 12
    # 2. 12 // 10 = 1
    # 3. 1 // 10 = 0

print("Number is palindrome" if temp==rev else "Not a palindrome")



# # with class and function
class Solution:
    def isPalindrome(x):  
        temp = x
        rev = 0
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x //= 10
        # if temp == rev:
        #     return True
        # else:
        #     return False
        return True if temp == rev else False

x = int(input("enter = "))
sol = Solution()
print(sol.isPalindrome(x))


