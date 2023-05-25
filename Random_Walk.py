import random
import matplotlib.pyplot as plt

n=1000

x=[]
y=[]
x_new=0
y_new=0
for i in range(n):
    x_new= x_new+random.uniform(-1,1)
    y_new= y_new+random.uniform(-1,1)

    x.append(x_new)
    y.append(y_new)
  
plt.plot(x,y)
