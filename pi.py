from math import sqrt
import random
import matplotlib.pyplot as plt

point=0
point_num=10000

in_circle=[[],[]]
out_circle=[[],[]]

for i in range(point_num):
   x=random.uniform(-1,1)
   y=random.uniform(-1,1)
   distance = sqrt(x**2+y**2)

   if distance > 1:
      out_circle[0].append(x)
      out_circle[1].append(y)
   
   elif distance <=1:
      in_circle[0].append(x)
      in_circle[1].append(y)
pi=0
pi=4*(len(in_circle[0])/point_num)
print("pi number:",pi)

plt.scatter(out_circle[0],out_circle[1],s=1)
plt.scatter(in_circle[0],in_circle[1],s=1)
plt.show()