# Print some text to console
print("Supply a word to manipulate")

# option will get assigned whatever the user types
wrd = input("What word would you like to use : ")

baseL = input("What letter would you like to replace in " + wrd + ": ")

editL = input("What letter would you replace it with : ")

print(wrd.replace(baseL, editL))
    