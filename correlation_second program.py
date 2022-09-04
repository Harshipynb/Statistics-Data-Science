

from cmath import sqrt
from functools import reduce


print('''Correlation is used to measure the strenght of the relations between two variable 

rxy = +1 Stongly direct relationship between two variable 

rxy= -1 Strongly indirect relationship between the two variables

rxy =0 or near to o it means it has minimal effect on change''')


def test(a,b):
    new_a=[]
    new_b=[]
    for j in range(len(a)):
        sum_a=0
        for i in a:
            sum_a+=i
        sum_b=0
        for k in b:
            sum_b+=k
        new_a.append(a[j]-(sum_a/len(a)))
        new_b.append(b[j]-(sum_b/len(b)))
    num=[]
    sqr_a=[]
    sqr_b=[]
    for i in range(len(new_a)):
        ele=new_a[i]*new_b[i]
        ele2=(new_a[i]**2)
        ele3=new_b[i]**2
        num.append(ele)
        sqr_a.append(ele2)
        sqr_b.append(ele3)
    deno_a=reduce((lambda x,y:x+y),sqr_a)
    deno_b=reduce((lambda x,y:x+y),sqr_b)
    nume_ab=reduce((lambda x,y:x+y),num)
    return (nume_ab/(deno_a*deno_b)**0.5)



        

x=list(map(int,input("enter the list of element").split()))

y=list(map(int,input("enter the second of lelment ").split()))

print(test(x,y))
