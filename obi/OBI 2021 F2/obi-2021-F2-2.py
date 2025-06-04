l = []
n1 = int(input(''))
n2 = int(input(''))
l.append(n1)
l.append(n2)
c = min(l) * 3 - (n1 + n2)
if 1 <= n1 <= n2 <= 10**9:
    print(c)