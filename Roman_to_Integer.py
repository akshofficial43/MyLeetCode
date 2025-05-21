# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II(1+1) in Roman numeral, just two ones added together. 12 is written as XII, which is simply X(10) + II(1+1=2). The number 27 is written as XXVII, which is XX(10+10=20) + V(5) + II(1+1=2).



# here start code
symbol = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}
roman = input("Roman number = ")
result = 0


# Loop through each character in the roman numeral
for i in range(len(roman)):
    # If the current symbol is less than the next symbol and the next symbol exists
    if i + 1 < len(roman) and symbol[roman[i]] < symbol[roman[i + 1]]:
    # i -> index of the current character
    # roman[i] -> character at index i
    # symbol[roman[i]] -> value of the character at index i
        result -= symbol[roman[i]] # Subtract the current symbol from the result
    else:
        result += symbol[roman[i]] # Add the current symbol to the result 
    
print(result)

# for i in symbol:
#     print(i, symbol[i]) # Print the symbol and its value
#     # here i is the key and symbol[i] is the value

# for i in range(len(roman)):
#     print(i, roman[i], symbol[roman[i]]) 
#     # i -> index of the current character
#     # roman[i] -> character at index i
#     # symbol[roman[i]] -> value of the character at index i




# with class and function
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}
        result = 0

        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
            
        return result

    
sol = Solution()
s = "III"
sol.romanToInt(s)