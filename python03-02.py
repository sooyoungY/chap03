# # # -*-coding:utf-8

# # # 반복문 while, for
# # # 기존 언어의 while문과 기능과 사용법이 동일함
# # # while문 외부에 카운트 변수를 선언, while 내부에 변수를 카운트, while 문 옆에 조건을 입력
# # # while의 조건 부분에 괄호를 사용하지 않음
# # # 들여쓰기를 맞춰줘야함

# # treeHit = 0
# # while treeHit < 10:
# #     treeHit += 1 #변수 카운트
# #     print("나무를 {0} 번 찍었습니다".format(treeHit))
# #     if treeHit == 10:
# #         print("나무 넘어값니다.")

# # # 반복문 탈출하기(break)
# # # break를 만나면 가장 가까운 반복문에서 탈출함
# print()

# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다")
#     coffee -= 1
#     print("남은 커피의 양은 {0} 개입니다".format(coffee))
#     # not연산자를 사용하여 coffee의 값이 0이 아닐 경우는 그냥 넘어가고, coffee 값이 0일 경우 아래의 내용을 실행
#     if not coffee:
#         print("커피가 다 떨어졌습니다. 중지합니다.")
#         break

# # while (money > 0){
# #     System.out.println();

# #     if (!coffee){
# #         break;
# #     }
# # }

# coffee = 10
# while True:
#     money = int(input("돈을 넣어주세요"))
#     if money == 300:
#         print("돈을 받았으니 커피를 줍니다")
#         coffee -= 1
#         print("남은 커피의 양은 {0} 개입니다".format(coffee))
#     elif money > 300:
#         print("거스름돈 {0}을 주고 커피를 줍니다".format(money-300))
#         coffee -= 1
#         print("남은 커피의 양은 {0} 개입니다".format(coffee))
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 {0} 개입니다".format(coffee))
#     if not coffee:
#         print("커피가 다 떨어졌습니다. 중지합니다.")
#         break

# # 조건에 맞지 않을 경우 처음으로 돌아가기(continue)
# # 기존에 다른 언어의 continue문과 기능과 사용법이 동일함

# a = 0

# while a < 10:
#     a += 1
    
#     if a % 2 == 0:
#         continue
#     print(a)

# # 사용자 입력한 숫자에 해당하는 구구단을 출력

# # n = input("단 수를 입력 하세요 : ")
# # n = int(n)

# # m = 1

# # while m < 10:
# #     print("{0} X {1}= {2}".format(n, m, n * m))
# #     m += 1

# # 2중 와일문을 사용해서 구구단 전체 출력
# m = 1

# while m < 10:
#     n = 1
#     while n < 10:
#         print("{0} X {1} = {2}".format(m, n, m * n))
#         n += 1
#     m += 1
    
# while문과 list를 사용하여 로또 번호 자동 생성 프로그램 만들기
import random
lotto = []

print("로또 추첨 시작합니다")
while len(lotto) < 6:
    num = random.randint(1, 45) 
    if num not in lotto:
        lotto.append(num)
lotto.sort()
print("당첨 예상 번호 %s" %lotto)

