l = []
for i in range(6):
    l.append(str.upper(input('')))
c = l.count('V')
if c >= 5:
    print('1')
elif c >= 3:
    print('2')
elif c >= 1:
    print('3')
else:
    print('-1')