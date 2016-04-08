# Author: Cubed | Alex Munoz
# Email: alex@napend.com
# Site: alex-munoz.net
# Also.... This is python.... Just for my dad........

# Tells them the begining
print("Quiz: Written by Cubed | Alex Munoz")
print(" ")
print("Please use ALL lower case!!!!!!! If you use uppercase, your answer will be wrong!")

# Asks and repeats name
name = raw_input('Enter your name: ')
print("Hello " + name + "!")
print(" ")

# Asks what company I own
company = raw_input('What company do I own? ')
if company == "napend":
    print("Correct")
else:
    print("Wrong, the answer was 'napend'.")
print(" ")

# Asks for my fav lang
favLang = raw_input('What is my favorite language? ')
if favLang == "c#":
    print("Correct")
else:
    print("Wrong, the answer was 'c#'.")
print(" ")

# Asks for my least lang
lstLang = raw_input('What is my least favorite language? ')
if lstLang == "asp.net":
    print("Correct")
else:
    print("Wrong, the answer is 'asp.net'.")
print(" ")

# Thanks them for playing
print("Thank you for playing " + name + "!")
print("\n")
