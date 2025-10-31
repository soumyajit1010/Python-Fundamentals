'''
def calc_sum(a, b):
    sum=a+b
    print(sum)
    return sum

a = 5;
b = 10;
print(calc_sum(a, b));





def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)


cal_fact(6)

'''

def converter(usd_val):
    inr_val = usd_val*83
    print(usd_val, "USD =", inr_val, "INR")

converter(73)