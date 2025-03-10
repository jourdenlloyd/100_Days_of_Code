num = int(input("Which number would you like a mod for? "))
mod = int(input("Which mod would you like to check? "))
result = (num % mod)
if result == 0:
    print("even")
else:
    print("odd")