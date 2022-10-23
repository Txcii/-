import matplotlib.pyplot as plt
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)
y = np.cos(x)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)
plt.title(r'$f(x)=cos(x)$') 
plt.plot(x, y)
#plt.show()

x1 = [t*0.375*np.pi for t in x]
y1 = np.cos(x1)
plt.subplot(1,2,2)

plt.title(r'$f(x)=cos(\omega x), \omega = \frac{3}{8} \pi$') 
plt.plot(x1, y1)
plt.show()