
f1 = list(str.lower(input('')))
f2 = list(str.lower(input('')))
for i in f1:
    c = f2.count(i)
    if c < 1:
        print('N')
        s = False
        break
    else:
        s = True
        continue
if s == True:
    print('S')