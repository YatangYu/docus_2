import random as r

#計算骰子期望值
N=10000
s=0
for i in range(N):
    s+=r.randint(1,6)   #隨機生成1~6中任意整數，並加總

s/=N #除上總次數
print(s)    #期望值結果

#隨機浮點數產生
random_number=r.random()    #生成0~1隨機浮點數字
print(random_number)
print(80*random_number+20)    #乘上係數放大嶼平移即可得到想要區間中隨機數
#範例隨機數再20~100之間
