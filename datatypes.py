# type  is used to list the type of dataset that is being outputed or used
#       examples are listed below

# Define a variable 
x = 10
# Print the type that is referenced to the number (int)
print ( type(x))

####
# Define a variable 
x = 1.7
# Print the type that is referenced to the number (float)
print ( type(x))

###
# Multiply a int and float....(int x float = float)
print ( 10*x )

###
# When dealing with str you need to add "" between the str
message = "Hello World!"
print(type(message))

###
# When doing booleans is much be a capital first letter (True/False)
myBool = True
print(type(myBool))

###
# casting a int to a float
x = 15
print(type(x))

print(float(x))

print(type(float(x)))

###
# using the input function, the answer will be come back as a string. Example below
answer = input("Type a number? ")
print(answer * 7) #This will put the answer listed 7 times
#Two ways to fix this. This will fix this by saying the answer needs to be an int
print(int(answer)*7) 
answerInt = int(answer)
print(answerInt*7)

###
# Using literals to force a data type
x = 10.0 # decimal indicate float literal
x = True # boolean indicates boolean literal
x = "name" # "" indicates str literal (' & " are interchangeable)