print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#how much is each size of pizza?
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")
#how much to add for pepperoni based on size?
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
#how much to add for extra cheese?
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")