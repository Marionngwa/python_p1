scores = [150, 172, 68, 92, 65, 86, 142, 120,184]
sum = 0

# for num in scores:
#     sum+=num

# print(sum)

#print(max(scores))

max_num = 0
for num in scores:
    if num > max_num:
        max_num = num

print(max_num)

