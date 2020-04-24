import numpy as np
import matplotlib.pyplot as plt

v1=[0,0,1]

l=0.0405
dl=0.005
n=int(l*2/dl)+1
x=[-l+i*dl for i in range(n)]
y=[-l+i*dl for i in range(n)]
u=[[0 for j in range(n)] for i in range(n)]
v=[[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):  
        v2=[x[j],y[i],0]
        b=np.cross(v1,v2)   #計算v1,v2之外積
        u[i][j]=b[0]
        v[i][j]=b[1]
        

plt.streamplot(np.array(x),np.array(y),np.array(u),np.array(v))
plt.axis([-l,l,-l,l])   #用以限制繪圖範圍 與xlim,ylim功能相當，但實際使用時可能會有些許差別
plt.show()

plt.quiver(x,y,u,v,color='b',width=0.005)   #包含方向與大小之向量圖，color可調整顏色，width調整箭頭寬度
plt.axis([-l,l,-l,l])
plt.show()



