



# 실전에서 유용한 표준 라이브러리



# 1. 내장 함수
# 별도의 import 구문 없이도 사용 가능한 함수
# 기본 입출력 함수부터 정렬 함수까지 기본적인 함수를 제공
# 파이썬에서 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능을 포함


# 자주 사용되는 내장 함수

# sum(): 다수의 데이터를 포함한 리스트나 튜플 등에 대해 그 원소들의 합을 반환
result = sum([1, 2, 3, 4, 5])
print(result)   # 15

# min(): 다수의 데이터에서 가장 작은 값을 반환
# max(): 다수의 데이터에서 가장 큰 값을 반환
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print('가장 작은 수:', min_result)  # 가장 작은 수: 2
print('가장 큰 수:', max_result)    # 가장 큰 수: 7

# eval(): 사람의 입장에서 수식으로 표현된 식에 대해 그것을 계산한 결과를 수 형태로 반환
result = eval("(3 + 5) * 7")
print(result)   # 56

# sorted() : 내부적으로 리스트와 같은 반복 가능한 객체가 들어왔을 때 각 원소를 정렬한 결과를 반환
result = sorted([9, 1, 8, 5, 4])   # ==> 오름 차순 정렬된 값 반환
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)   # ==> 내람 차순 정렬된 값 반환
print(reverse_result)  # [9, 8, 5, 4, 1]

# sorted() with key : key 속성으로 정렬 기준을 명시해줄 수 있음
# 정렬 기준은 일반적으로 람다 함수의 형태로 간단하게 넣어주는 경우가 많음
array = [('하니', 50), ('초코', 32), ('효진', 78)]
result = sorted(array, key=lambda x: x[1], reverse=True) # 각 튜플 원소의 두번째 원소를 기준으로 정렬
print(result)   # [('효진', 78), ('하니', 50), ('초코', 32)]






# 2. itertools
# 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공
# 특히 순열과 조합 라이브러리는 코딩 테스트에서 자주 사용 
# => 모든 경우의 수를 고려해야하는 완전 탐색 문제 유형에서 소스코드를 매우 간결하게 작성할 수 있도록 함


# 순열과 조합
# 모든 경우의 수를 고려해야 할 때 효과적으로 사용할 수 있는 라이브러리

# 순열(permutations): 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
# {'A', 'B', 'C'}에서 세 개를 선택하여 나열하는 경우 => 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA' 
# 순열의 수 구하는 공식:
# nPr = n * (n - 1) * (n - 2) *...* (n - r + 1)

from itertools import permutations  # itertools에 정의되어 있는 permutations라이브러리 사용

data = ['A', 'B', 'C'] # 데이터 준비

result = list(permutations(data, 2)) #  모든 순열 구하기 (n = 3, r = 2)
print(result) # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]


# 조합(combinations): 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
# {'A', 'B', 'C'}에서 순서를 고려하지 않고 두 개를 뽑는 경우 => 'AB', 'AC', 'BC'
# 조합의 수 구하는 공식:
# nCr = n * (n - 1) * (n - 2) *...* (n - r + 1)   /   r!

from itertools import combinations  # itertools에 정의되어 있는 combinations라이브러리 사용

data = ['A', 'B', 'C', 'D'] # 데이터 준비

result = list(combinations(data, 3)) #  2개를 뽑는 모든 조합 구하기(n = 4, r = 3)
print(result) # [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]



# 중복 순열과 중복 조합

# 중복 순열(product)
from itertools import product # itertools에 정의되어 있는 product라이브러리 사용

data = ['A', 'B', 'C']  # 데이터 준비

result = list(product(data, repeat = 2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), 
              # ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]  


# 중복 조합(combinations_with_replacement)
from itertools import combinations_with_replacement  # itertools에 정의되어 있는                  
                                                     # combinations_with_replacement 함수 사용

data = ['A', 'B', 'C']  # 데이터 준비

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]






# 3. heapq
# 힙(Heap) 자료구조를 제공
# 일반적으로 우선순위 큐 기능을 구현하기 위해 사용 
# 최단 거리 알고리즘에서 많이 활용






# 4. bisect
# 이진 탐색(Binary Search) 기능을 제공
# 기본적인 형태의 이진 탐색 기능이 필요할 때 효과적으로 사용 가능






# 5. collections
# 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함

# 카운터(Counter)
# 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공함
# 리스트와 같은 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지를 알려줌.

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])   # 'blue'가 등장한 횟수 출력 => 3
print(counter['green'])  # 'green'이 등장한 횟수 출력 => 1
print(dict(counter))     # 사전 자료형으로 반환 => {'red': 2, 'blue': 3, 'green': 1}






# 6. math
# 필수적인 수학적 기능을 제공
# 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함


# 최대 공약수와 최대 공배수

# 최대 공약수
# 두 수의 약수 중 가장 큰 값
# 최대 공약수를 구해야 할 때는 math 라이브러리의 gcd() 함수를 이용할 수 있음.
# math.gcd(1, 2) ==> 1과 2의 최대 공약수 출력

# 최소 공배수
# 두 수의 공통된 배수 중 가장 작은 값
# 최소 공배수는 두 수의 곱 // 두 수의 최대 공약수
# 1 * 2 // math.gcd(1, 2) ==> 1과 2의 최소 공배수 출력


import math  # math에 정의되어 있는 함수를 사용 

#최소 공배수(LCM)를 구하는 함수를 정의
def lcm(a, b):
    return a * b // math.gcd(a, b)

print(math.gcd(21, 14)) # 최대 공약수(GCD) 계산   => 7
print(lcm(21, 14))      # 최소 공배수(LCM) 계산   => 42



# /   => 나누기(출력 값 소수점 반영 float)
# //  => 나누기(출력 값 소수 자리 제거  int)







