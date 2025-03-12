#Create a range inclusive of 10 and print
for num in range(1,11):
    print(num)

print("\n")
#Create a range inclusive of 10, include a step, and print
for num in range(1,11,3):
    print(num)

print("\n")
#Add all numbers together in the range of 1-100

#temp variable for total
total = 0
for num in range(1,101):
    total += num
    #add each number to the total and set the total back to itself
    print(total)