T = int(input())
 
def calc(s):
 
    num_a = num_b = 0
    res = 0
 
    for i in range(len(s)):
        if s[i] == 'A':
            num_a += 1
        else:
            num_b += 1
 
        if num_b == 0:
            num_a = 0
        else:
            if num_a == num_b:
                res += num_a
                num_a = 0
                num_b = 0
 
    return res + num_a
 
for _ in range(T):
 
    N = int(input())
    S = input()
 
    print(calc(S))
