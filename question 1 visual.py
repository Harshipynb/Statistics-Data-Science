
import matplotlib.pyplot as plt
import numpy as np


month_data=["Jan","Feb","March","April"]
temp=[10,15,22,30]
humi=[76,78,86,88]
x=np.arange(len(month_data))

fig=plt.figure(figsize=(10,7))

plt.bar(x -0.2,temp,color="red",width=0.4,label="Temperature")

plt.bar(x +0.2,humi,color="blue", width=0.4,label="Humidity")

plt.xticks(x,month_data)

plt.xlabel("Temperature and Humidity")

plt.ylabel("Month")

plt.title("Average Temp and Humidity in a Particular Month")
plt.legend()

plt.show()