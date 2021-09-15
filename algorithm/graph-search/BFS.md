


# BFS(Breadth-First-Search)

 BFS는 **너비 우선 탐색**이라고도 부르며 그래프에서 **가까운 노드부터 우선적으로 탐색하는 알고리즘**
  
 → 큐 자료구조를 이용하여 구현 <br>
 → 특정 조건에서의 최단 경로를 구하는 문제를 해결할 때 효과적으로 사용될 수 있음
 
 ***
<br>

 
## 구체적인 동작 


   1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
   2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리.
      방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

<br>

## BFS 동작 예시
**[Steps 0]** 그래프 준비
  
![dfs1](/algorithm/resources/img/dfs1.png)

   + 그래프의 방문 기준: 번호가 낮은 인접 노드부터 방문
   + 시작노드: 1
   

**[Steps1]** 시작 노드인 '1'을 큐에 삽입하고 방문 처리

![bfs1](/algorithm/resources/img/bfs1.png)

**[Steps2]** 큐에서 노드 '1'을 꺼내 방문하지 않은 인접 노드인 '2', '3', '8' 을  큐에 삽입하고 방문 처리

![bfs2](/algorithm/resources/img/bfs2.png)

**[Steps3]** 큐에서 노드 '2'를 꺼내 방문하지 않은 인접 노드인 '7'을 큐에 삽입하고 방문 처리

![bfs3](/algorithm/resources/img/bfs3.png)

**[Steps4]** 큐에서 노드 '3'을 꺼내 방문하지 않은 인접 노드 '4', '5'를 큐에 삽입하고 방문 처리

![bfs4](/algorithm/resources/img/bfs4.png)

**[Steps5]** 큐에서 노드 '8'을 꺼내고 방문하지 않은 인접 노드가 없으므로 무시

![bfs5](/algorithm/resources/img/bfs5.png)

**[Steps6]** 이러한 과정을 반복해서 실행

![bfs6](/algorithm/resources/img/bfs6.png)

 - **전체 노드의 탐색 순서**(큐에 들어간 순서): 1 → 2 → 3 → 8 → 7 → 4 → 5 → 6

<br>

## BFS 소스코드 예제

- **큐 자료구조**를 사용하여 BFS구현

```python

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
# 일반적으로 그래프 문제가 출제되면 노드의 번호가 1번 부터 시작하는 경우가 많기 때문에 인덱스 0에 대한 내용은 비워둘 것(사용 X)
#   => 문제에 나와있는 노드의 번호를 graph리스트의 인덱스와 매핑할 때, 
#      인덱스에 1을 더하는 방식이 아닌 인덱스 0을 사용하지 않는 방식을 사용하는 것이 더 직관적!
# 1번 인덱스부터 해당 노드에 인접한 노드를 리스트에 초기화
graph = [
  [], 
  [2, 3, 8], 
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]


# 각 노드가 방문된 정보를 표현 (1차원 리스트)
# 실제 노드에 대한 인덱스는 1 ~ 8까지지만 인덱스를 0을 사용하지 않도록 하기 위해 1만큼 더 큰 크기로 1차원 리스트를 초기화
visited = [False] * 9


from collections import deque

# DFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 정의된 BFS함수 호출
bfs(graph, 1, visited)


# 실행 결과 : 1 2 3 8 7 4 5 6

```
             