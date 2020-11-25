a = [0,1]
b = []
for i in range(1000):
    if a[-1] <= 500:
        b = a[i+1] + a[i]
        a.append(b)
    else:
        pass
del(a[-1])

print('Fibonacci ---> {}'.format(a))

