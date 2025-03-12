student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55,
                  91, 64, 89,202]
# print(range(1, 10))
#
# sum1 = 0
# for score in student_scores:
#     sum1 += score
#
# print(sum1)

max1 = 0
#Start with temp variable at 0
for score in student_scores:
    #print(score)
    if score > max1:
        print(f"temp = {max1}")
        max1 = score
#if score from list is greater than 0, it becomes the temp; then when a higher number
# is reached that becomes the temp each time we check the list, until no higher numbers
print(f"final = {max1}")