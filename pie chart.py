from turtle import color
import matplotlib.pyplot as plt

x={'math':20,'biology':15,'commerce':25,'arts':35}

sub=list(x.keys())
no_of_st=list(x.values())

fig=plt.figure(figsize=(10,5))

#create a bar graph

plt.pie(no_of_st,labels=sub)

plt.title("Number of Students in each stream")

plt.show()