from collections import OrderedDict
n = int(input())

recipt = OrderedDict()
for _ in range(n):
    item = input().split()
    price = int(item[-1])
    item = ' '.join(item[:-1])
    if item in recipt.keys():
        recipt[item] += price
    else:
        recipt[item] = price
        
for item, price in recipt.items():
    print(f'{item} {price}')