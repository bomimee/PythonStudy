#https://matplotlib.org

import matplotlib.pyplot as plt

#fig = plt.figure(figsize=(3,3))
#plt.show()

#fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
#plt.show()

#창분할
fig = plt.figure()
#1행 2열의 첫번째 
ax1 = fig.add_subplot(1,2,1)
#1행 2열의 두번째 
ax2 = fig.add_subplot(1,2,2)

plt.show()