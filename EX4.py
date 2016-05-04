scores = [60, 73, 81, 95, 34]
n = 5
i = 0
w = 0
total = 0
while i < 5:
    total += scores[i]
    i += 1
eaqu = 0
while w < 5:
    eaqu += scores[w]*scores[w]
    w += 1
avg = total/n

print('total ' + str(total))
print('average ' + str(avg))
print('eaqu ' + str(eaqu))
print('40341124')
