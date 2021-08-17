



# 함수
# 함수한 특정한 작업을 하나의 단위로 묶어 놓은 것을 의미
# 함수를 사용하면 불필요한 소스코드의 반복을 줄일 수 있음.


# 함수의 종류
# 1. 내장 함수: 파이썬이 기본적으로 제공하는 함수 (ex)input(),print(),..
# 2. 사용자 정의 함수: 개발자가 직접 정의하여 사용할 수 있는 함수 


# 함수 정의
# 프로그램에는 똑같은 코드가 반복적으로 사용되어야 할 때가 많음
# 함수를 사용하면 소스코드의 길이를 줄일 수 있음
# 매개변수(parameter): 함수 내부에서 사용할 변수, 인자로부터 값을 넘겨받는 변수
# 반환 값: 함수에서 처리 된 결과를 반환

# def 함수명(매개변수):
#     실행할 소스코드
#     return 반환 값

# 호출 방법 -> 함수명(인자)
# 인자(argument): 함수를 호출할때 매개변수로 넘겨줄 값




# 더하기 함수 예시(1) - 반환 값이 존재하는 사용자 정의 함수
def add(a, b):
    return a + b

print(add(1, 2))     # 3

# 더하기 함수 예시(2) - 반환 값이 없는 사용자 정의 함수

def add(a, b):
    print('함수의 결과:', a + b)

add(5, 6)    # 함수의 결과: 11






# 파라미터 지정하기
# 파라미터의 변수를 직접 지정할 수 있음
# 이 경우 매개변수의 순서가 달라도 상관 없음

def minus(a, b):
    print('함수의 결과:', a - b)

minus(b = 4, a = 8)      # 함수의 결과: 4
minus(a = 8, b = 4)      # 함수의 결과: 4






# global 키워드
# global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고,
# 함수 바깥에 선언된 변수를 바로 참조하게 됨

a = 0

def func():
    global a   # 함수 바깥에 선언된 변수 a를 참조하겠다
    a += 1

for i in range(10):  # 0 ~ 9  => 10번 반복
    func()


print(a)     # 10     



# 함수 내부에 지역 변수로써 선언된 변수의 이름과 함수 바깥에 선언된 전역 변수의 이름이
# 동일할 경우 그 함수의 내부에서는 지역변수로 선언된 변수가 우선적으로 참조됨


array = [1, 2, 3, 4, 5]

def func():
    array = [3, 4, 5]
    array.append(6)
    print('내부 print:', array)  

func()                          # 내부 print: [3, 4, 5, 6]     --> 지역 변수 array 참조
print('외부 print:', array)     # 외부 print: [1, 2, 3, 4, 5]   --> 전역 변수 array 참조




array = [1, 2, 3, 4, 5]

def func():
    global array                # 함수 바깥에 선언된 변수 array를 참조하겠다
    array.append(6)
    print('내부 print:', array)  

func()                          # 내부 print: [1, 2, 3, 4, 5 , 6]  --> 전역 변수 array 참조
print('외부 print:', array)     # 외부 print: [1, 2, 3, 4, 5 , 6]  --> 전역 변수 array 참조








# 여러 개의 반환 값
# 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있음

def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var  
    # 자동으로 반환해야 할 값들이 묶여서 한꺼번에 반환  -> 패킹


a, b, c, d = operator(7, 3)   
# 함수를 호출하는 곳에서는 반환된 값들을 차례대로 변수 a, b, c, d에 초기화  -> 언패킹

print(a, b, c, d)       # 10   4   21   2.3333333333333335






