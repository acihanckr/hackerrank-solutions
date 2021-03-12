import re
def fun(s):
    #start
    return bool(re.match(r'^[\w\-_]+@[a-zA-Z0-9]+\.[a-z]{,3}$',s))
    #end

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)