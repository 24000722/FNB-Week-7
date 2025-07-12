# Loop Control Statements

fruits = ["apple" , "banana" , "cherry" , "date"]

for fruit in fruits:
    if fruit == "cherry":
        break      # exits the loop if cherry is found
    print(fruit)   # prints apple and banana
    
print()

for fruit in fruits:
    if fruit == "cherry":
        continue      # skips cherry and move to next iteration
    print(fruit)   # prints apple and banana and date
    
print()

for fruit in fruits:
    if fruit == "cherry":
        pass     # Placeholder , no action is needed for cherry
    print(fruit)   # prints apple and banana and cherry and date  (prints everything as usual)
    
    
# While loop

count = 0

while  count <= 5 :
    print(count)
    count += 1    # increments the count by 1
    if count == 3:
        break   # exits the loop when the count 3 is reached  (prints 0 1 2)



