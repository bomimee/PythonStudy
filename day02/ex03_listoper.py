su1 = [1,2,3]
su2 = [4,5,6, "홍길동",8]
res = su1 + su2
print(res)

res = su1 *3

print(res)

res = str(su1[1]) + "hi"
print(res)

odd = [1,7,5,3,9]

print(odd.append(11))
print(odd)

#항목 수정

odd[2] =13

print(odd)

del odd[2]

odd.insert(2, 13)
print(odd)

odd.sort()
print(odd)

str = ['a', 'c', 'A', 'e','b','B','가','t', '1']
str.sort()
print(str)

str.reverse()
print(str)