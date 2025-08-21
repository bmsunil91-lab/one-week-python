print("enter the any word")
a = input()
print("reverse of the string is", a[::-1])
if a == a[::-1]:
  print("string is palindrome")
else:
  print("string is not palindrome")