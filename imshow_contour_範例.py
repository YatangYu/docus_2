import matplotlib.pyplot as plt

L=10
dl=0.1
n=int(L*2/0.1+1)

x=[-L+dl*i for i in range(n)] #x,y軸
y=[-L+dl*i for i in range(n)]

V=[[0 for i in range(n)] for j in range(n)] #純量場

#以圓錐為例
for i in range(n):
    for j in range(n):
        r=((-10+i*dl)**2+(-10+j*dl)**2)**0.5
        V[i][j]=10-r*2

plt.imshow(V,origin='lower',vmin=-10,vmax=10,extent=[-L,L,-L,L]) #vmin,vmax可限制最大最小值,extent控制x,y座標軸,orign用以調整座標軸原點
plt.colorbar() #叫出色條colorbar
plt.show()



cont=plt.contour(x,y,V,20) #最後一個數字為等高線密度設定
plt.clabel(cont) #加上數字標記等高線
plt.show()
