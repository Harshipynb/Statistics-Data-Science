from functools import reduce


a=[-4620,-520,180,980,3980]

x=list(map((lambda x:x**2),a))
print(x)

y=[-190,-150,50,100,190]
b=list(map((lambda x: x**2),y))
print(b)
l=[]
for i in range(len(x)):

    l.append(x[i]*b[i])

print("final",l)

su=reduce((lambda x,y:x+y),l)

finalll=su**0.5


print(finalll)