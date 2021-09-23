


# 선택 정렬 (Selection-Sorting)

 처리되지 않은 데이터 중에서 **가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복**
 
 → 매번 현재 범위에서 가장 작은 데이터를 골라서 제일 앞쪽으로 보내주는 것<br>
 → 매번 가장 작은 데이터를 찾기 위해 탐색 범위 만큼 데이터를 하나씩 확인해야하기 때문에 선형 탐색을 수행하는 것과 동일<br>
 → 탐색 범위는 반복할 때마다 줄어들게 됨<br>
('**이중 반복문**'을 이용해서 이러한 선택 정렬을 구현할 수 있음) 
 
 ***
<br>


## 선택 정렬 동작 예시
**[Steps 0]** 정렬할 데이터를 준비
  
![selection1](/algorithm/resources/img/sorting/selection/selection1.png)


**[Steps 1]** 처리되지 않은 데이터 중 가장 작은 '0'을 선택해 가장 앞의 '7'과 바꿈
  
![selection2](/algorithm/resources/img/sorting/selection/selection2.png)


**[Steps 2]** 처리되지 않은 데이터 중 가장 작은 '1'을 선택해 가장 앞의 '5'과 바꿈
  
![selection3](/algorithm/resources/img/sorting/selection/selection3.png)


**[Steps 3]** 처리되지 않은 데이터 중 가장 작은 '2'을 선택해 가장 앞의 '9'과 바꿈
  
![selection4](/algorithm/resources/img/sorting/selection/selection4.png)


**[Steps 4]** 처리되지 않은 데이터 중 가장 작은 '3'을 선택해 가장 앞의 '7'과 바꿈
  
![selection5](/algorithm/resources/img/sorting/selection/selection5.png)


**[Steps 5]** 이러한 과정을 반복하면 다음과 같이 정렬이 완료됨
  
![selection6](/algorithm/resources/img/sorting/selection/selection6.png)

  + 정렬되지 않은 데이터가 하나 남았을 때는 앞쪽으로 보내봤자 자기 자신의 위치와 동일 하기 때문에 마지막인 경우에는 처리하지 않아도 전체 데이터가 성공적으로 정렬됨


<br>

## 선택 정렬 소스코드 예제

- **이중 for문**를 사용하여 선택 정렬 구현

```python

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    # 파이썬에서는 두원소의 위치를 바꾸는 스와프 연산을 아래와 같이 별도의 표준 라이브러리를 호출하지 않고 한 줄로 간단히 표현할 수 있음   
    array[i], array[min_index] = array[min_index], array[i] # 스와프
         
print(array)

# 실행 결과 : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```  



<br>

## 선택 정렬의 시간 복잡도

+ 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 함
+ 구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산 횟수는 다음과 같음<br>
  ```  N + (N - 1) + (N - 2) + ... + 2  ```
+ 이는 (N² + N - 2) / 2 로 표현할 수 있는데, 빅오 표기법에 따라서 **O(N²)** 이라고 작성


  





