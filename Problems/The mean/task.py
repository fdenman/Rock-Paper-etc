data = 0
n_nums = 0
sum_nums = 0

while True:
    data = input()
    if data == ".":
        break
    n_nums += 1
    sum_nums += int(data)

print(sum_nums/n_nums)
