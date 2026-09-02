print("Enter two strings:")
string1 = input()
string2 = input()
if len(string1) == len(string2):
    print("Strings are equal length.")
elif len(string1) > len(string2):
    print("First string is longer by %i characters." % (len(string1)-len(string2)))
else: 
    print("Second string is longer by %i characters." % (len(string2)-len(string1)))
