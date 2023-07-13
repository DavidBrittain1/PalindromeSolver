
def ValidatePalindrome(Palindrome): 
   
  # Step 1: Combine the string into one word
  thislist = Palindrome.split()
  newlist = ""
  for word in thislist:
    newlist = newlist + word

    # Step 2: Convert the string to all lowercase
  lowerPalindrome = newlist.lower()

    # Step 3: Reverse the string
  reverseLower = lowerPalindrome [::-1]
  if reverseLower == lowerPalindrome:
          
    print("Yes, it is a Palindrome")
    
  else:
    
    print("No, it is not a Palindrome")

  userInput = str(input("Please enter in a word or sentence to check if it is a Palindrome. "))
  ValidatePalindrome(userInput)

              




