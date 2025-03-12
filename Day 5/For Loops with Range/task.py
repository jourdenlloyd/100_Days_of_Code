# Create a range inclusive of 10 and print
for num in range(1, 11):
    print(num)

print("\n")
# Create a range inclusive of 10, include a step, and print
for num in range(1, 11, 3):
    print(num)

print("\n")
# Add all numbers together in the range of 1-100

# temp variable for total
total = 0
for num in range(1, 101):
    total += num
    # add each number to the total and set the total back to itself
    print(total)

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
    #Have to check for this condition first so that there aren't duplicate entries
    # when something matches multiple conditions / code breaks / repeated changes to list