def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n

print(calc_sum(10))


def print_list(list, idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["M", "L", "A", "B"]
print_list(fruits)