#start
n = int(input())
phones = dict()
for _ in range(n):
    phone = input().split()
    phones[phone[0]] = int(phone[1])
while True:
    try:
        name = input()
        print(f'{name}={phones[name]}')
    except KeyError:
        print('Not found')
    except EOFError:
        break
#end