userName = input("What is your name? ")
userAge = input("And how old are you? ")

print("Hello " + userName)

if int(userAge) >= 18:
    print("You're old enough to vote in the U.S. ")
else:
    print("You need to wait a few more years before you can vote in the U.S. ")
    print("Stay in school!")
