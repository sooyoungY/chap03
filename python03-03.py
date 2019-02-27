# -*-coding:utf-8

# for 문 사용하기
# 기존 언어의 for 문과 다른 for ~in 문의 형태를 하고 있다.
# 자바에서는 for~in문과 같고 c#에서는foreach문과 같은 형태의 반복문
# for문의 조건절에 in 연산자를 사용하여 해당하는 리스트 및 튜플, 딕셔너리의 모든 요소를 카운트 변수 없이 출력할 수 있다.
# for문 사용시 괄호를 사용하지 않는다.

test_list = ["one", "two", "three"]

for i in test_list:
    print(i)

# 리스트 a의 요소가 튜플로 구성되어 있어 in 연산자에서 리스트의 값을 받는 부분을 튜플로 지정해야함
# 튜플로 변수 선언 및 초기화 하는 방식인(a,b) = (값1,값2)를 사용하여 리스트a의 요소 데이터를 대입받음
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first, last)

(a, b) = (3, 4)
# 문제 1 리스트 1~10 까지의 합을 구하는 프로그램 for문을 이용해 스크립트 제작
print("문제 1) 리스트 1~10 까지의 합을 구하는 프로그램 for문을 이용해 스크립트 제작")
a = [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]
for (a, s, d, f, g, h, j, k, l, z) in a:
    print("합 :{0} ".format(a + s + d + f + g + h + j + k + l + z))
    
a = [1]
count = 0
for i in a:
    while i < 11:
        count = count + i
        i += 1
print("합 :{0} ".format(count))

print()

marks = [90, 35, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("{0}번 학생은 합격입니다.".format(number))
    else:
        print("{0}번 학생은 불합격입니다.".format(number))

# for문에서 continue 사용
# while문에서의 continue 사용법과 동일함

print()

marks = [90, 35, 67, 45, 80]
number = 0

for mark in marks:
    number += 1

    if mark < 60:
        continue

    print("{0}번 학생 축하합니다.".format(number))

print()

marks = [90, 35, 67, 45, 80]
number = 0

for mark in marks:
    number += 1

    if mark < 70:
        break

    print("{0}번 학생 축하합니다.".format(number))
# for문과 range문을 이용하기
# range() 함수는 지정한 범위의 숫자의 리스트를 자동으로 생성
# rnage(시작숫자, 끝 숫자), 시작 숫자를 제외하며 0에서 지정한 끝 숫자까지 자동 생성
print()
print(range(1, 11))

sum = 0
for i in range(1, 11):
    sum += i
print(sum)

for i in range(2, 10):
    for j in range(1, 10):
        print("{0} X {1} = {2}".format(i, j, i * j))

# 사용자 입력을 받아 해당하는 단수의 구구단을 출력

# print()
# i = input("출력할 구구단을 입력하세요 : ")
# i = int(i)
# for j in range(1, 10):
#         print("{0} X {1} = {2} ".format(i, j, i * j),end = " ")

# 리스트 내포 사용하기
# 리스트에 for~in 문을 사용하여 리스트의 요소를 자동 생성하는 방식
a = [1, 2, 3, 4]
result = []

for num in a:
    result.append(num * 3)
print(result)

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print("리스트 내포 방식 출력 : {0}".format(result))

result = [num * 3 for num in a if num % 2 == 0]
print("리스트 내포 방식 for if 출력 : {0}".format(result))

# 문제3) listNum 이라는 리스에 숫자가 1부터 10까지 들어있다. 이 리스트를 리스트 내포 방식을 사용하여 복사하세요.
# 복사받을 리스트의 이름 : listCopy
print()
print("문제 3")
listNumber = list(range(1, 11))
print("listNumber : {0}".format(listNumber))
listCopy = [num for num in listNumber]
print("listCopy : {0}".format(listCopy))

result = [x * y for x in range(2, 10) for y in range(1, 10)]
print(result)