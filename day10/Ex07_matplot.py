import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# ax.set_xlim([0., 10.]) # x축이 0-10까지
# ax.set_ylim([0.5, 2.5]) # y축
# ax.set_title('matplot sample', size=15)
# ax.set_xlabel('x_axis', size=10)
# ax.set_ylabel('y_axis', size=10)
#ax.set(xlim=[0.,5.], ylim=[-0.5,5.5], title='sample', xlabel='x', ylabel='y')  #이 경우 사이즈 지정 못함

ax.set_xlim([0., 8.]) # x축이 0-10까지
ax.set_ylim([0., 40.]) # y축

# ax.plot(4,20, 'o', c='r') #marker => ^, *, o, x
# ax.plot(2,10, 'x', c='green') #marker => ^, *, o, x

x= np.array([1,3,5,7])
y= np.array([10,25,15,30])

#ax.plot(x,y,'bo') #bo => 색, 마커 한번에 지정
ax.scatter(x,y, marker='*', color="red") #bo => 색, 마커 한번에 지정
plt.show()