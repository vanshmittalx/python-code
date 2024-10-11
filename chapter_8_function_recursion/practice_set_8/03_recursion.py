def sum_number(num):
    if num==1:
        return 1
    return sum_number(num-1) + num
print(sum_number(4))