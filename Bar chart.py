from turtle import color
import matplotlib.pyplot as plt

x={'math':20,'biology':15,'commerce':25,'arts':35}

sub=list(x.keys())
no_of_st=list(x.values())

fig=plt.figure(figsize=(10,5))

#create a bar graph

plt.bar(sub,no_of_st,color="#00e4ff",width=0.4)

plt.xlabel("Subjects")

plt.ylabel("No of Students ")

plt.title("Number of Students in each stream")

plt.show()