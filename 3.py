
import matplotlib.pyplot as plt
import numpy as np 
# linspace 
x = np.linspace(0, 4* np.pi, 500)
y = np.cos(x)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.title(r'$f(x)=cos(x)$') 
plt.plot(x, y)
plt.grid()
plt.show()


