d=[]
for i in range(128):
    s=bin(i)[2::]+bin(i%4)[2::]
    if 50<=int(s,2)<=99:
        d.append(i)
print(max(d),len(d))