l = list(str.lower(input('')))
print(l)
l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
for i in l1:
    c = l.count(i)
    if c < 1:
        print('N')
        s = False
        break
    else:
        s = True
        continue
if s == True:
    print('S')