




# 그리디 알고리즘(탐욕법)
# 그리디 알고리즘은 현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미
# 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구함
# 그리디 해법은 그 정당성 분석이 중요
# 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지를 검토하는 과정이 꼭 필요


# [문제 상황] 루트 노드부터 시작하여 거쳐 가는 노드 값의 합을 최대로 만들고 싶습니다.


#                           5

#           7               10               8 

#       7   5   9         4   3          1   4   5


#         Q1. 최적의 해는 무엇인가요?                   5 -> 7 -> 9       => 총 합 21
#         Q2. 단순히 매 상황에서 가장 큰 값만 고른다면?  5 -> 10 -> 4      => 총 합 19
# => 단순히 매 상황에서 가장 큰 값만 고르는 후자의 경우가 그리디 알고리즘

# 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많음
# 하지만 코딩 테스트에서의 대부분의 그리디 문제는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 
# 이를 추론할 수 있어야 풀리도록 출제됨.
# => 즉, 탐욕법으로 얻은 해가 최적의 해가 되는 경우에 한에서 문제가 출제되는 경우가 많음.







# <문제> 거스름 돈

# 1. 문제 설명
# 본인은 음식점의 계산을 도와주는 점원
# 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정
# 손님에게 거슬러 주어야 할 돈이 N원 일 때 거슬러 주어야 할 동전의 최소 개수를 구해라
# 단, 거슬러 줘야 할 돈 N은 항상 10의 배수

# 2. 문제 해결 아이디어
# 최적의 해를 빠르게 구하기 위해서는 가장 큰 화폐 단위부터 돈을 거슬러 주면 됨
# N원을 거슬러 줘야 할 때, 가장 먼저 500원으로 거슬러 줄 수 있을 만큼 거슬러 줌
# 이후에 100원, 50원, 10원짜리 동전을 차례대로 거슬러 줄 수 있을 만큼 거슬러 주면 됨


# 3. 정당성 분석
# 가장 큰 화폐 단위부터 돈을 거슬러 주는 것이 최적의 해를 보장하는 이유는
# 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해
# 다른 해가 나올 수 없기 때문
# 그리디 알고리즘 문제에서는 이처럼 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지
# 검토할 수 있어야 함


# N = 1260일 때의 예시

# 내가 짜본 코드

n = 1260

fivehundred = n // 500
n -= (500 * fivehundred)

hundred = n // 100
n -= (100 * hundred)

fifty = n // 50
n -= (50 * fifty)

ten = n // 10
n -= (10 * ten)

print(fivehundred + hundred + fifty + ten)


# 4. 답안 예시

n = 1260 
coincount = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]

for coin in array:
    coincount += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(coincount)    


# 5. 시간 복잡도 분석
# 화폐의 종류가 k라고 할 때, 소스코드의 시간 복잡도는 o(k)
# 이 알고리즘의 시간 복잡도는 거슬러줘야 하는 금액과는 무관, 동전의 총 종류에만 영향을 받음







