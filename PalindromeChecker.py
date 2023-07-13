
def ValidatePalindrome(Palindrome): 
   
  # Step 1: Combine the string into one word
  thislist = Palindrome.split()
  newlist = ""
  for word in thislist:
    newlist = newlist + word

    # Step 2: Convert the string to all lowercase
  lowerPalindrome = newlist.lower()
  print(lowerPalindrome)

    # Step 3: Reverse the string
  reverseLower = lowerPalindrome [::-1]
  print(reverseLower)
  if reverseLower == lowerPalindrome:
          
    return True
    
  else:
    
    return False

  


if ValidatePalindrome("Rise to vote sir"):
  print("yes")
else:
  print("no")                   



#TestString = "Does this strip?"
#SplitString = TestString.split()
#StrippedString = ""
#x = 0
#while x < len(SplitString):
#	x += 1
#	for y in SplitString:
#		StrippedString = StrippedString.join(y)
#print(StrippedString)
