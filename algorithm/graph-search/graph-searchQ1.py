



# <문제> 음료수 얼려 먹기


# 1. 문제 설명
# N x M 크기의 얼음 틀이 있음
# 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성해라.
#   -> 연결 요소(Connected Component)를 찾는 문제라고 볼 수 있음

# 다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성
#   00110
#   00011
#   11111
#   00000





# 2. 문제 조건
# 난이도 1.5, 풀이시간 30분, 시간제한 1초, 메모리 제한 128MB
# 입력 조건: 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어짐 (1 <= N,M <= 1000)
#           두 번째 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어짐
#           이때 구멍이 뚫려 있는 부분은 0, 그렇지 않은 부분은 1
# 출력 조건: 한 번에 만들 수 있는 아이스크림의 개수를 출력





# 내가 짜본 코드  
n, m = map(int,input().split())
graph = []

for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)


def node_check(i,j):
    if i < 0 or i > n-1 or j < 0 or j > m-1:
        return False
    if graph[i][j] == 1:
        return False
    else:   
        graph[i][j] = 1
        node_check(i-1, j)
        node_check(i, j-1)
        node_check(i+1, j) 
        node_check(i, j+1)
        return True   
          
count = 0
for i in range(n):
    for j in range(m):
        if node_check(i,j) == True:
            count += 1

print(count)            
            



  
# 3. 문제 해결 아이디어
# 이 문제는 DFS 혹은 BFS로 해결할 수 있음
# 앞에서 배운 대로 얼음을 얼릴 수 있는 공간이 상, 하, 좌, 우로 연결되어 있다고 표현할 수 있으므로
# 그래프 형태로 모델링 할 수 있음

# 다음과 같이 3 x 3 크기의 얼음 틀이 있다고 가정
#   0 ㅡ 0 ㅡ 1
#   ㅣ   ㅣ   ㅣ
#   0 ㅡ 1 ㅡ 0
#   ㅣ   ㅣ   ㅣ
#   1 ㅡ 0 ㅡ 1 

# DFS를 활용하는 알고리즘
# (1) 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 
#    값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
# (2) 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복하면, 
#    연결된 모든 지점을 방문할 수 있음
# (3) 모든 노드에 대하여 1 ~ 2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트





# 4. 답안 예시  

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)    
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False    


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)









