import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("vgsales.csv")
print(df)
a=df.loc[:,"Publisher"].tolist()
x=len(a)
print(x)
i=0
b=[]
while(i<x):
    if(a[i] not in b):
        b.append(a[i])
    i=i+1
print(b)
print(len(b))

c=[]
e=0
while(e<len(b)):
    j=0
    d=0
    while(j<x):
        if(b[e]==a[j]):
           d=d+df.loc[j,"NA_Sales"]
        j=j+1

    c.append(d)
    e=e+1
print(c)
c1=c.copy()
c1.sort(reverse=True)
print(c1)
n=[None]*579
for j in range(0,len(c)):
    for i in range(0, len(c)):
        if (c1[j] == c[i]):
            n[j] = b[i]
print(n)

f=[]
e=0
while(e<len(b)):
    j=0
    d=0
    while(j<x):
        if(b[e]==a[j]):
           d=d+df.loc[j,"EU_Sales"]
        j=j+1
    f.append(d)
    e=e+1
print(f)
f1=f.copy()
f1.sort(reverse=True)
print(f1)
n1=[None]*579
for j in range(0,len(c)):
    for i in range(0, len(c)):
        if (f1[j] == f[i]):
            n1[j] = b[i]
print(n1)

g=[]
e=0
while(e<len(b)):
    j=0
    d=0
    while(j<x):
        if(b[e]==a[j]):
           d=d+df.loc[j,"JP_Sales"]
        j=j+1
    g.append(d)
    e=e+1
print(g)
g1=g.copy()
g1.sort(reverse=True)
print(g1)
n2=[None]*579
for j in range(0,len(c)):
    for i in range(0, len(c)):
        if (g1[j] == g[i]):
            n2[j] = b[i]
print(n2)

h=[]
e=0
while(e<len(b)):
    j=0
    d=0
    while(j<x):
        if(b[e]==a[j]):
           d=d+df.loc[j,"Other_Sales"]
        j=j+1
    h.append(d)
    e=e+1
print(h)
h1=h.copy()
h1.sort(reverse=True)
print(h1)
n3=[None]*579
for j in range(0,len(c)):
    for i in range(0, len(c)):
        if (h1[j] == h[i]):
            n3[j] = b[i]
print(n3)

k=[]
e=0
while(e<len(b)):
    j=0
    d=0
    while(j<x):
        if(b[e]==a[j]):
           d=d+df.loc[j,"Global_Sales"]
        j=j+1
    k.append(d)
    e=e+1
print(k)
k1=k.copy()
k1.sort(reverse=True)
print(k1)
n4=[None]*579
for j in range(0,len(c)):
    for i in range(0, len(c)):
        if (k1[j] == k[i]):
            n4[j] = b[i]
print(n4)

x= np.array([1,2,3,4,5])
y= np.array(c1[0:5])
plt.plot(x,y,"*-")
plt.xlabel("Publisher",color="#000080")
plt.ylabel("Sales range",color="#FF13F0")
plt.title("NA_Sales Report",color="Red")
plt.grid()
plt.xticks([1,2,3,4,5],(n[0:5]),color="Green")
plt.show()

x= np.array([1,2,3,4,5])
y= np.array(f1[0:5])
plt.plot(x,y,"*-")
plt.xlabel("Publisher",color="#000080")
plt.ylabel("Sales range",color="#FF13F0")
plt.title("EU_Sales Report",color="Red")
plt.grid()
plt.xticks([1,2,3,4,5],(n1[0:5]),color="Green")
plt.show()

x= np.array([1,2,3,4,5])
y= np.array(g1[0:5])
plt.plot(x,y,"*-")
plt.xlabel("Publisher",color="#000080")
plt.ylabel("Sales range",color="#FF13F0")
plt.title("JP_Sales Report",color="Red")
plt.grid()
plt.xticks([1,2,3,4,5],(n2[0:5]),color="Green")
plt.show()

x= np.array([1,2,3,4,5])
y= np.array(h1[0:5])
plt.plot(x,y,"*-")
plt.xlabel("Publisher",color="#000080")
plt.ylabel("Sales range",color="#FF13F0")
plt.title("Other_Sales Report",color="Red")
plt.grid()
plt.xticks([1,2,3,4,5],(n3[0:5]),color="Green")
plt.show()

x= np.array([1,2,3,4,5])
y= np.array(k1[0:5])
plt.plot(x,y,"*-")
plt.xlabel("Publisher",color="#000080")
plt.ylabel("Sales range",color="#FF13F0")
plt.title("Global_Sales Report",color="Red")
plt.grid()
plt.xticks([1,2,3,4,5],(n4[0:5]),color="Green")
plt.show()





