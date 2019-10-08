def reverse(s): 
    return s[::-1] 

def isPalindrome(s):
    rev = reverse(s) 
    if (s == rev): 
        return True
    return False

s = str(input("Enter your text: \n"))
result = isPalindrome(s.lower()) 

if result == 1: 
    print("Yes") 
else: 
    print("No")
