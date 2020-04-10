import matplotlib.pyplot as plt

#1 point source==================


L=10
dl=0.1

n=int(L*2/0.1+1)

x=[-L+dl*i for i in range(n)]
y=[-L+dl*i for i in range(n)]

V=[[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        r=((-10+i*dl)**2+(-10+j*dl)**2)**0.5
        V[i][j]=10-r*2

plt.imshow(V,vmin=-10,vmax=10,extent=[-L,L,-L,L])
plt.colorbar()
plt.show()



cont=plt.contour(x,y,V,20)
plt.clabel(cont)
plt.show()



















'''
l=10
dl=0.1
extream=10

sources=[[[0,0]],[[0.01,0],[-0.01,0]],\
         [[-0.01,-0.01],[0.01,0.01],[-0.01,0.01],[0.01,-0.01]]]

n=int(l*2/dl)+1
pos=[[-l+i*dl for i in range(n)],[-l+i*dl for i in range(n)]]

tri=[0,0]

V=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        r2=0
        tri[0]=pos[0][j]
        tri[1]=pos[1][i]
        for g in range(2):
            r2+=tri[g]**2
        r=r2**0.5
        V[i][j]+=10-2*r
             
plt.imshow(V,vmin=-extream,vmax=extream,extent=[pos[0][0],pos[0][-1],pos[1][0],pos[1][-1]])
plt.colorbar()
plt.show()

cont=plt.contour(pos[0],pos[1],V,10)
plt.clabel(cont)
plt.show()
'''