

letters = "a", "e", "i", "o", "u", "w", "y", "å", "ä", "ö"
out = ""
namn = input("")


 
for x in namn:
    if x in letters:
        out = out+x
    else:
        out = out+x+"o"+x

print(out)
