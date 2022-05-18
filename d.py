ap = []

while 1:
    a = int(input())
    if a == -1:
        break
    else:
        ap.append(a)

cnt = 0
for i in ap:
    if i>=100:
        cnt+=1
print(cnt)