from cmath import sqrt


print('''Correlation is used to measure the strenght of the relations between two variable 

rxy = +1 Stongly direct relationship between two variable 

rxy= -1 Strongly indirect relationship between the two variables

rxy =0 or near to o it means it has minimal effect on change''')


#////////////correaltion program////////////////

def correlation(a,b):
    new_a=[]
    for i in a:
        sum1=0
        for j in a:
            sum1+=j
        mean_data1=sum1/len(a)
        new_a.append(i-mean_data1)
    print(new_a)
    new_a_2=[]
    for i in new_a:
        new_a_2.append(i**2)
    new_b=[]
    for i in b:
        sum2=0
        for j in b:
            sum2+=j
        mean_data2=sum2/len(b)
        new_b.append(i-mean_data2)
    print(new_b)
    new_b_2=[]
    for i in new_b:
        new_b_2.append(i**2)
    numerator=[]
    for i in range(len(a)):
        numerator.append(new_a[i]*new_b[i])
    deno=[]
    for i in range (len(a)):
        deno.append(new_a_2[i]*new_b_2[i])
    sum_num=0
    sum_dem=0
    for i in range(len(new_a)):
        sum_num+=numerator[i]
        sum_dem+=deno[i]
    print(sum_dem)
    return (sum_num/((sum_dem)**0.5))
    
x=list(map(int,input("enter the list of element").split()))

y=list(map(int,input("enter the second of lelment ").split()))


print(correlation(x,y))