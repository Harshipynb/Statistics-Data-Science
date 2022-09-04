def covar(l1,l2):
    new_li1=[]
    for j in l1:
        sum=0
        for i in l1:
            sum+=i
        mean_data=sum/len(l1)
        new_li1.append(j-mean_data)
    new_l2=[]
    for j in l2:
        sum2=0
        for i in l2:
            sum2+=0
        mean_data2=sum2/len(l2)
        new_l2.append(j-mean_data2)
    multiplication=[]
    for i in range(len(l1)):
        multiplication.append(new_li1[i]*new_l2[i])
    summasion=0
    for i in multiplication:
        summasion+=i
    return summasion/len(l1)
    
x=list(map(int,input("enter the list of element").split()))

y=list(map(int,input("enter the second of lelment ").split()))


print(covar(x,y))