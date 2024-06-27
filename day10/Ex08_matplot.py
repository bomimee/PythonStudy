import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1) #1행2열 첫번째
ax2 = fig.add_subplot(1,2,2) #1행2열 두 번째

ax1.set_xlim([0., 10.]) # x축이 0-10까지
ax1.set_ylim([0.5, 2.5]) # y축
ax1.set_title('matplot sample', size=15)
ax1.set_xlabel('x_axis', size=10)
ax1.set_ylabel('y_axis', size=10)
ax2.set(xlim=[0.,5.], ylim=[-0.5,5.5], title='sample', xlabel='x', ylabel='y')  #이 경우 사이즈 지정 못함
plt.show()