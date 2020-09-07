def isPalindrome(s): 
    if type(s)!=str:
        print ("please pass string")
        return False
    # Using predefined function to
    s= s.lower()
    rev = ''.join(reversed(s)) 
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False

# main function 
s = "1234554321"
ans = isPalindrome(s) 

if (ans): 
    print("Yes") 
else: 
    print("No") 

print ("Test Case 1")
s = "1221"
print ("Is ",s," palindrome: ",isPalindrome(s) )
print ("\nTest Case 2")
s = 1221
print ("Is ",s," palindrome: ",isPalindrome(s) )
print ("\nTest Case 3")
s = "abba"
print ("Is ",s," palindrome: ",isPalindrome(s) )
print ("\nTest Case 4")
s = "abbA"
print ("Is ",s," palindrome: ",isPalindrome(s) )
print ("\nTest Case 5")
s = "abcdcdab"
print ("Is ",s," palindrome: ",isPalindrome(s) )