# -*-coding:utf-8

# if문
# 기존 언어의 if문과 거의 동일
# if(조건문 {})
#       실행할 코드
# }

# 파이썬은 조건문 부분에 괄호가 없음
# 파이썬은 코드 블럭 대신 : 기호를 사용
# 실행할 코드 부분의 들여쓰기를 반드시 해야함
# 파이썬에서 들여쓰기 부분이 다르면 실행 오류가 발생함
# if~ else if ~ else 문의 경우 else if의 명령어가 elif로 되어있음(사용하는 방법은 동일)

# 이렇게 들여쓰기를 통한 소스의 제어는 다른사람들과의 협업 시 모두 동일한 패턴의 소스로 개발이 가능하기 때문에 프로그램의 유지 보수가 쉬움
money = 1
if money:
    print("택시 gogo")
    print("타고 가자")
else:
    print("걸어 gogo")

print()
money = 1
if money:
    print("택시 gogo")
print("타고 가자")#if문이 아님

print()
money = 1
if money:
    print("택시를")
    print("타고")
        # print("가자") 주석 풀면 오류 발생함

# 비교연산자
# 기본 비교 연산자 <, >, <=, >=, ==,!=
# 다른언어의 비교 연산자와 동일함
print()
x = 3
y = 2
print("x > y : {0}".format(x > y))
print("x < y : {0}".format(x < y))
print("x = y : {0}".format(x == y))
print("x != y : {0}".format(x != y))

# 파이썬의 and, or, not, in 연산자
# 기존 다른 언어의 연산자 : &&(and), ||(or), !(not)
# 사용방법은 동일
# if(a > 5 && a < 10){}
print()
a = 8

if a > 5 and a < 10:
    print("a는 5보다 크고 10보다 작다")

if a > 0 or a < 10:
    print("a는 0보다 크거나 10보다 작다")

if not a == 10:
    print("a는 10이 아니다")

# in연산자
# 리스트나 튜플, 문자열 안에 지정한 데이터가 있는지 확인하는 연산자
# if문과 사용할 경우에는 해당 리스트나 튜플, 문자열에 지정한 데이터가 있는지 확인하는 용도로 사용
# for문에서 사용할 경우 해당 리스트나 튜플, 딕셔너리에서 처음부터 끝까지의 요소를 하나씩 꺼내오는 용도로 사용
a = [1, 2, 3]

if (2 in a):
    print("리스트 a에 숫자 2가 포함되어 있음")

for value in a:
    print(value)

print("1dms fltmxm [1, 2, 3]에 포함되어 있음 : {0}".format(1 in [1, 2, 3]))

print("1dms fltmxm [1, 2, 3]에 포함되어 있지 않음 : {0}".format(1 not in [1, 2, 3]))

print()

pocket = ["paper", "cellphone", "money"]
if "money" in pocket:
    print("택시 타고 가라")
else:
    print("걸어 가라")

# pass
# 반복문에서 사용하느 continue와 비슷한 기능을 가진 명령어로 if문에서 특별한 작업을 하지 않을 경우 사용
# 기존 언어에서 if문에서 실행애야할 코드 부분을 코브 블럭으로 감싸거 있는 형태이기 때문에 실행 되어야 할 영역이 명확함
# 실행 되어야 하는 영역이 명확하기 때문에 코드블럭 내에 아무런 실행 코드가 없어도 오류가 발생하지 않는다.
# 파이썬은 if문 내에 아무런 실행 코드가 없을 경우 의도적으로 실행 코드의 입력이 없는 것인지 아닌지를 판단할 수 없기에 (코드블럭 대신 들여쓰기를 통하여 구분하기 때문) pass라는 명령어를 사용하여 어떠한 실행도 하지 않는다고 명시함

print()
if "money" in pocket:
    pass
else:
    print("걸어 가라")

# elif문
# 파이썬에서는 기존 언어의 if~else if~else 문을 elif문으로 표현함
# 사용방법은 기존 언어와 동일함

print()
pocket = ["paper", "cellphone"]

card = 1 #숫자형은 0이 아니면 무조거 True
if "money" in pocket:
    print("택시를 타고 가라")
elif "카드":
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# 문제 1 ) 성적표를 출력하는 프로그램 작성
# 조건 1 . 95이상 A+, 90 이상 A, 85이상 B+, 80이상 B 형태로 해서 60이하는 F 
# 조건 2 . 출력시 점수와 등급을 화면에 출력
# 조건 3 . elif 문을 사용하여 프로그램 작성
print()
print("예제문제")
score = input("점수를 입력하세요 : ")
score = int(score)

if score >= 95:
    print("A+등급 입니다. 점수는 {0} 입니다".format(score))
elif score >= 90:
    print("A등급 입니다. 점수는 {0} 입니다".format(score))
elif score >= 85:
    print("B+등급 입니다. 점수는 {0} 입니다".format(score))
elif score >= 80:
    print("B등급 입니다. 점수는 {0} 입니다".format(score))
elif score >= 75:
    print("C+등급 입니다. 점수는 {0} 입니다".format(score))
elif score >= 70:
    print("C등급 입니다. 점수는 {0} 입니다".format(score))
else:
    print("D등급 입니다. 점수는 {0} 입니다".format(score))