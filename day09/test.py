import matplotlib.pyplot as plt

names = ["Python", "Java", "Spring", "Flask"]
score = [95, 85, 90, 80] 

# 이름에 대한 히스토그램 그리기
plt.figure(figsize=(8, 6))
plt.bar(names, score, color='skyblue')
plt.xlabel('Names')
plt.ylabel('Score')
plt.title('Score by Name')
plt.show()