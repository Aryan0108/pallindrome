input = input("Enter a word")
input1 = input.casefold()
revs = reversed(input1)
if list(input1) == list(revs):
    print("This is a pallindrome")

elif list(input1) == input.type(int):
     print("Error, please type a word")

else:
     print("This is not a pallindrome")

