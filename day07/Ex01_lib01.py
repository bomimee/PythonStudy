# 표준 라이브러리 : 파이썬을 설치할 때 자동으로 설치 되는 라이브러리

import datetime, time, calendar
day1 = datetime.date(2021,12,14)
day2 = datetime.date(2023,4,5)

# 두 날짜의 차이 : 
diff = day2 - day1
print(diff)
print(diff.days)

day = datetime.date(2024,5,8)
print(day.weekday()) # 요일 : 0=>월요일, 6=>일요일
print("-" * 50)

# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴
print(time.time())
# 연,월,일,시,분초,의 형태로 변경해주는 함수
print(time.localtime())
# 튜플 형태로  날짜와 시간을 알아보기 쉬운 형태로 리턴
print(time.asctime(time.localtime(time.time())))
print(time.ctime())

# 시간에 관련된 세밀한 표현하는 여러가지 포맷코드 사용
# time.strftime('출력할 형식 포맷코드', time.localtime(time.time()))
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%X', time.localtime(time.time())))
print("-" * 50)

# 보통 반복문에서 일정한 시간 간격을 두고 실행할 때 : sleep
for i in range(10):
    print(i, end=' ')
    time.sleep(1)  # 1초
print()
print("-" * 50)

# 1-12 달력
calendar.prcal(2024)
# 5월 달력
calendar.prmonth(2024,5)
# 요일 ; 0 =>월요일
print(calendar.weekday(2024,5,8))



