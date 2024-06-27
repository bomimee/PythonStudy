# 초를 받아서 몇시간, 몇분, 몇초인지 출력하자

# ex 3999초 는 1시간 6분 29초 이다

time = int(input("input seconds: "))
print(time)
hours = time //3600
res = time % 3600
min = res //60
sec = res % 60
print("{0}초는 {1}시간 {2}분 {3}초 입니다. " .format(time, hours, res, min, sec))
