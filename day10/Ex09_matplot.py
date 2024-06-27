import matplotlib.pyplot as plt
import numpy as np
#한글깨진처림
# plt.rcParams["font.family"] = "Gothic"
# plt.rcParams['axes.unicode_minus'] =False
# plt.rcParams["font.size"] = 15
fig = plt.figure(figsize=(8,8))
ax1 = fig.add_subplot(1,1,1)

# names = ["Python", 'Java', 'Spring', 'Flask']
# score =[155, 301, 125, 98]

#ax1.plot(names, score, color="#f00")
#ax1.bar(names, score, color="#f00")

x= [5,8,10]
y= [12,16,6]
x2 =[6,9,11]
y2 =[6,15,7]

ax1.scatter(x,y, label="x")
ax1.scatter(x2,y2, label="x2")

ax1.set(title="scatter plot", xlabel="x_axis", ylabel="y_axis")
plt.show()

names = ["Python","Java","Spring","Flask"]
score = [95,85,90,80] 

plt.hist(names, bins=4)
plt.hist(score, bins=5)
plt.legend()
plt.show()

# figure = plt.figure(figsize=(4,5))
# data = fig.add_subplot(1,1,1)
# x1 = np.random.randn(1000)
# data.hist(x1, bins=10)
# data.set(title="sample", xlabel="class", ylabel="count")
# plt.show()