



# 조건문
# 조건문은 프로그램의 흐름을 제어하는 문법
# 조건문을 이용해 조건에 따라서 프로그램의 로직을 설정할 수 있음.

# if 조건식 :
#    조건식이 true일 경우 실행할 코드 (들여쓰기가 적용되어 있어야 함)

x = 15
if x >= 10:
  print("x >= 10")   #실행 

if x >= 0:
  print("x >= 0")    #실행 

if x >= 30:
  print("x >= 30")   #미실행  




# 파이썬에서는 코드의 블록(Block)을 들여쓰기로 지정
# 만약 조건식이 true일 때, if문 바로 아래 같은 들여쓰기를 가진 부분이 차례로 모두 실행됨
# 조건문 내부에 또 다른 조건문 가능

score = 85

if score >= 70:                 # score가 70점 이상일 때 실행
  print("성적이 70점 이상입니다.")
  if score >= 90:                 # score가 70점 이상이면서 90점 이상일 때 실행
    print("우수한 성적입니다.")
else:                           # score가 70점 미만일 때 실행
  print("성적이 70점 미만입니다.")
  print("조금 더 분발하세요.")

print("프로그램을 종료합니다.")  # --> 무조건 실행


# 들여쓰기
# 탭을 사용하는 쪽과 공백 문자(space)를 여러 번 사용하는 쪽으로 두 진영이 있음.
# 파이썬 스타일 가이드라인에서는 4개의 공백 문자를 사용하는 것을 표준으로 설정하고 있음.



# 조건문의 기본 형태
# 조건문의 기본적인 형태 ==>  if ~ elif ~ else
# 조건문을 사용할 때 elif 혹은 else 부분은 경우에 따라서 사용하지 않아도 됨

if 조건문 1:
    조건문 1이 True일때 실행되는 코드
elif 조건문 2:
    조건문 1에 해당하지 않고, 조건문 2가 True일 때 실행되는 코드
else:
    위의 모든 조건문이 모두 True 값이 아닐 때 실행되는 코드




a = 5

if a >= 0:
    print("a >= 0")        # 실행
elif a >= -10:        
    print("0 > a >= -10")  # 미실행
else:
    print("-10 > a")       # 미실행          

    

               
# 성적 구간에 따른 학점 출력 예제
# 성적이 90점 이상일때: A
# 성적이 90점 미만, 80점 이상일 때: B
# 성적이 80점 미만, 70점 이상일 때: C
# 성적이 70점 미만일 때: F

score = 85

if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")   # 실행
elif score >= 70:
    print("c학점")
else:
    print("F학점")            





# 비교 연산자
# 비교 연산자는 특정한 두 값을 비교할 때 이용
# 대입 연산자(=)와 같음 연산자(==)의 차이점 유의할 것.

#    비교 연산자         설명
#      X == Y           X와 Y가 서로 같을 때 참(True)이다.
#      X != Y           X와 Y가 서로 다를 때 참(True)이다.
#      X > Y            X가 Y보다 클 때 참(True)이다.
#      X < Y            X가 Y보다 작을 때 참(True)이다.
#      X >= Y           X가 Y보다 크거나 같을 때 참(True)이다.
#      X <= Y           X가 Y보다 작거나 같을 때 참(True)이다.




# 논리 연산자
# 논리 연산자는 논리 값(True/False)사이의 연산을 수행할 때 사용

#    논리 연산자         설명
#      X and Y          X와 Y가 모두 참(True)일 때 참(True)이다.
#      X or Y           X와 Y중에 하나만 참(True)이어도 참(True)이다.
#      not X            X가 거짓(False)일 때 참(True)이다.


if True or False:  # 둘 중에 하나만 참 이어도 참
    print("Yes")   # --> 실행


a = 15

if a <= 20 and a >=0:   # 둘 모두 참 이어야 참
    print("Yes")      
# a <= 20 --> 참 
# a >=0 -->참
# 실행





# 파이썬의 기타 연산자
# 다수의 데이터를 담는 자료형을 위해 in 연산자와 not in 연산자가 제공
# 리스트, 튜플, 문자열, 딕셔너리 모두에서 사용이 가능

# in 연산자와 not in 연산자           설명
#     X in 리스트                    리스트 안에 X가 들어가 있을 때 참(True)이다.
#     X not in 문자열                문자열 안에 X가 들어가 있지 않을 때 참(True)이다.






# 파이썬의 pass 키워드
# 아무것도 처리하고 싶지 않을 때 pass 키워드를 사용
# (ex) 디버깅 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분을 비워놓고 싶은 경우

score = 86

if score >= 80:
    pass  # 나중에 작성할 소스코드 (현재는 아무 것도 처리되지 않음)
else:
    print("성적이 80점 미만입니다.")

print("프로그램을 종료합니다.")





# 조건문의 간소화

# 1. 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있음
# 콜론(:) 오른쪽에다가 해당 조건식이 참일 경우 실행할 코드를 써주면 됨.
score = 85
if score >= 80: result = "Success"
else: result = "Fail"

print(result)   # Success
 

# 2. 조건부 표현식은 if ~ else문을 한 줄에 작성할 수 있도록 해줌.
# if 조건식이 가운데 들어가는 점 주의!
# "조건식이 참일 때 실행할 코드" if 조건식 else "조건식이 거짓일 때 실행할 코드"
score = 85
result = "Success" if score >= 80 else "Fail"
# score >= 80 --> True일 경우 "Success"가, False일 경우 "Fail"이 result에 담기게 됨

print(result)   # Success






# 파이썬 조건문 내에서의 부등식
# 다른 프로그래밍 언어와 다르게 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용할 수 있음.
# (ex)  표현하고 싶은 수학의 부등식:   0 < X < 20 
#       일반적인 다른 프로그래밍 언어에서의 부등식 사용:    X > 0 and X < 20 
#       파이썬에서의 부등식 사용:    X > 0 and X < 20    와     0 < X < 20     
#          --> 파이썬에서는 두 방법 모두 사용 가능 하며, 둘 모두 같은 결과를 반환함.   


# 코드 스타일 1
x = 15
if x > 0 and x < 20:
    print("x는 0이상 20미만의 수입니다.")


# 코드 스타일 2
x = 15
if 0 < x < 20:
    print("x는 0이상 20미만의 수입니다.")

# 다른 언어를 다룰 때 헷갈리지 않도록  x > 0 and x < 20 와 같이 비교 연산자 사이에 
# and, or 등의 연산자가 들어가는 형태의 코드를 사용하는 것을 권장. 





