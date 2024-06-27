import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(1,1,1)

#평균 0, 표준편차 1 표준정규분포
x=np.random.randn(1000)
#히스토그램
ax.hist(x, bins=10) 

ax.set(title="histogram", xlabel="x_axis", ylabel="y_axis")
plt.show()

names = ["Python","Java","Spring","Flask"]
score = [95,85,90,80] 

figure = plt.figure(figsize=(4,5))
data = fig.add_subplot(1,1,1)
x1 = np.random.randn(1000)
data.hist(x1, bins=10)
data.set(title="sample", xlabel="class", ylabel="count")
plt.show()