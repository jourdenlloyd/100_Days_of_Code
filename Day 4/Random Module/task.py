import random

# rand_num = random.randint(1, 10)
# print(rand_num)
# from 1 to 9 because 10 isn't included

# rand_num = random.random() * 10
# print(rand_num)
# from to get float numbers


random_coin_face = random.randint(0,1)
if random_coin_face == 0:
    print("Heads")
else: print("Tails")
