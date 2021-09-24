


# 삽입 정렬 (Insertion-Sorting)

 처리되지 않은 데이터를 하나씩 골라 **적절한 위치에 삽입**
 
 → 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작<br>
 
 
 ***
<br>


## 삽입 정렬 동작 예시
**[Steps 0]** 첫 번째 데이터 '7'은 그 자체로 정렬이 되어 있다고 판단하고, 두 번째 데이터인 '5'가 어떤 위치로 들어갈지 판단
  
![insertion1](/algorithm/resources/img/sorting/insertion/insertion1.png)

  + '7'의 왼쪽으로 들어가거나 오른쪽으로 들어가거나 두 경우만 존재

<br>

**[Steps 1]** 이어서 '9'가 어떤 위치로 들어갈지 판단
  
![insertion2](/algorithm/resources/img/sorting/insertion/insertion2.png)
<br>

**[Steps 2]** 이어서 '0'이 어떤 위치로 들어갈지 판단
  
![insertion3](/algorithm/resources/img/sorting/insertion/insertion3.png)
<br>

**[Steps 3]** 이어서 '3'이 어떤 위치로 들어갈지 판단
  
![insertion4](/algorithm/resources/img/sorting/insertion/insertion4.png)
<br>

**[Steps 4]** 이러한 과정을 반복하면 다음과 같이 정렬이 완료됨
  
![insertion5](/algorithm/resources/img/sorting/insertion/insertion5.png)


<br>

## 삽입 정렬 소스코드 예제

- **이중 for문**를 사용하여 삽입 정렬 구현
- **매번 왼쪽에 있는 원소와 비교**해서 현재 삽입하고자 하는 원소가 더 작다면 바로 왼쪽에 있는 원소와 위치를 바꿔주는 방법을 이용하여 결과적으로 해당 원소가 어떤 위치에서 멈추면 되는지를 설정해 줌으로써 삽입 정렬을 수행

```python

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):   # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
                                # j는 삽입하고자 하는 원소의 위치를 의미                             
        if array[j] < array[j - 1]:   # 한 칸씩 왼쪽으로 이동
                                      #삽입하고자 하는 원소가 자신의 왼쪽에 있는 원소보다 작다면 
            array[j], array[j - 1] = array[j - 1], array[j]   #스와프
        else:   # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break      
         
print(array)

# 실행 결과 : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```  



<br>

## 삽입 정렬의 시간 복잡도


+ 삽입 정렬의 시간 복잡도는 **O(N²)** 이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩되어 사용됨
+ 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작함<br>
   → 최선의 경우 **O(N)** 의 시간 복잡도를 가짐<br>
   → 예를 들어 이미 정렬되어 있는 상태에서 다시 삽입정렬을 수행할 경우, <br>
   삽입하고자 하는 원소를 왼쪽에 있는 데이터와 비교했을 때 자신이 더 크기 때문에 각 원소가 들어가 위치를 고를 때 수행하는 선형 탐색이 멈춰지게 됨<br>  → 그러한 탐색과정이 바로 멈춰지기 때문에 탐색 과정이 단순히 상수 시간으로 대체되어 전체 정렬을 위한 시간 복잡도가 O(N)이 되는 것





  





