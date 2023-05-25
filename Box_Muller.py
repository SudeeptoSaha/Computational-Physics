import random
import matplotlib.pyplot as plt
import math

n= 16384
u=[]
v=[]
x=[]
y=[]
for i in range(n):
  u0= random.uniform(0,1)
  v0= random.uniform(0,1)
  u.append(u0)
  v.append(v0)
  x0= math.sqrt(-2 * math.log(u0))*math.cos(2 * math.pi * v0)
  y0= math.sqrt(-2 * math.log(u0))*math.sin(2 * math.pi * v0)


  x.append(x0)
  y.append(y0)

#Plot Graphs
plt.figure(figsize=(10,4))

plt.subplot(121)
plt.scatter(u,v)
plt.subplot(122)
plt.scatter(x,y)

plt.tight_layout()
plt.show()


