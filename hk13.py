def removeAlternate(n):
    if (n == 1):
        return 1
 
    if (n % 2 == 0):
        return 2 * removeAlternate(n / 2) - 1
    else:
        return 2 * removeAlternate(((n - 1) / 2)) + 1
 
 
from sys import stdin, stdout
 
for t in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    d = removeAlternate(n)
    i = (2 + 2 * k) % (n)
    if i == 0:
        i = n
    if i==1:
        e = (d -1) % n
    else:
        e = (d + i-2) % n
    if e == 0:
        e = n
    print(e)
