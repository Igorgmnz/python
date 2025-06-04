x = int(input('megabytes: '))
n = int(input('meses: '))
m = x
for i in range(n):
    m_i = int(input('usou: '))
    if m_i <= x:
        x = m + (x - m_i)
    elif n < 1 or n > 100:
        break
    elif x < 1 or x > 100:
        break
    else:
        break
print(x)