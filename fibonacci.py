n = int(input('qual numero? '))
termos = int(input('quantos termos? '))
c = 1
l = [0]
v = 0
while True:
    l.append(n)
    n += l[v]
    c += 1
    v += 1
    print(l)
    if c > termos:
        break