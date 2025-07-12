#Advanced concepts - Strings

message = 'Hello'

print(message[0])  #This prints the first letter "H" of the word Hello
print(message[1]) #This prints the letter in the 1st position which is "e"

print(message[-1])  #This prints the last character which is "o"

# Length of string
print(len(message)) #This prints the lenth of the word "Hello" which is 5

#Using strip
message = ' Hello, World! '
print(message.strip())  #This removes leading and trailing whitespace
#It prints Hello World! without the space at start and end
print(message.lower())  #This will convetts all characters to lower case = hello, world!
print(message.split(',')) #This split the string into a list based on the coma = ['Hello' , 'World!']

#Upper Method
#replace Method