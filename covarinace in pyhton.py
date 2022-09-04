


from audioop import mul


def covran(list1,list2):
    #mean of first list
    sum=0
    mean_l1=0
    for i in list1:
        sum+=i
    mean_l1=sum/(len(list1))
    new_li=[]
    for j in list1:
        new_li.append(j-mean_l1)
    print(new_li)
    sum_2=0
    mean_l2=0
    for i in list2:
        sum_2+=i
    mean_l2=sum_2/(len(list2))
    new_li2=[]
    for j in list2:
        new_li2.append(j-mean_l2)
    print(new_li2)
    mult=[]
    for i in range(len(list1)):
        mult.append(new_li[i]*new_li2[i])
    summasion=0
    for i in mult:
        summasion+=i
    return summasion/len(list1)



    
x=list(map(int,input("ente the first list").split()))
    
y=list(map(int,input("ente the second list").split()))

print(covran(x,y))


        