


# 퀵 정렬 (Quick-Sorting)

<u>**기준 데이터를 설정**</u>하고 그 **기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법**
 
 → 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나<br>
 → 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘<br>
 → 가장 기본적인 퀵 정렬은 **첫 번째 데이터를 기준 데이터(Pivot)로 설정**
 
 
 ***
<br>


## 퀵 정렬 동작 예시
**[Steps 0]** 현재 피벗의 값은 '5'

+ 왼쪽에서부터 '5'보다 큰 데이터를 선택하므로 '7'이 선택 되고, 오른쪽에서부터 '5'보다 작은 데이터를 선택하므로 '4'가 선택 됨
+ 선택된 두 데이터의 위치를 서로 변경 

![quick1](/algorithm/resources/img/sorting/quick/quick1.png)

<br>

**[Steps 1]** 현재 피벗의 값은 '5'

+ 왼쪽에서부터 '5'보다 큰 데이터를 선택하므로 '9'이 선택 되고, 오른쪽에서부터 '5'보다 작은 데이터를 선택하므로 '2'가 선택 됨
+ 선택된 두 데이터의 위치를 서로 변경 
  
![quick2](/algorithm/resources/img/sorting/quick/quick2.png)

<br>

**[Steps 2]** 현재 피벗의 값은 '5'

+ 왼쪽에서부터 '5'보다 큰 데이터를 선택하므로 '6'이 선택 되고, 오른쪽에서부터 '5'보다 작은 데이터를 선택하므로 '1'가 선택 됨
+ 단, 이처럼 **위치가 엇갈리는 경우 '피벗'과 '작은 데이터'의 위치를 서로 변경**
  
![quick3](/algorithm/resources/img/sorting/quick/quick3.png)

<br>

**[Steps 3]** 분할 완료

+ '5'의 왼쪽에 있는 데이터는 모두 5보다 작고, 오른쪽에 있는 데이터는 모두 '5'보다 크다는 특징이 있음
+ 이렇게 **피벗을 기준으로 데이터 묶음을 나누는 작업을 '분할'**이라고 함
  
![quick4](/algorithm/resources/img/sorting/quick/quick4.png)

<br>

**[Steps 4]** 왼쪽 데이터 묶음 정렬

+ 왼쪽에 있는 데이터에 대해서 마찬가지로 정렬을 수행
  
![quick5](/algorithm/resources/img/sorting/quick/quick5.png)

<br>

**[Steps 5]** 오른쪽 데이터 묶음 정렬

+ 오른쪽에 있는 데이터에 대해서 마찬가지로 정렬을 수행
+ 이러한 과정을 반복하면 전체 데이터에 대해서 정렬이 수행됨
  
![quick6](/algorithm/resources/img/sorting/quick/quick6.png)

<br><br>


## 퀵 정렬이 빠른 이유: 직관적인 이해
+ 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 **O(NlogN)**를 기대할 수 있음
``` 너비 x 높이 = N x logN = NlogN ```

![quick7](/algorithm/resources/img/sorting/quick/quick7.png)




<br><br>

## 퀵 정렬의 시간 복잡도


+ 퀵 정렬은 평균의 경우 **O(NlogN)**의 시간 복잡도를 가짐 
+ 하지만 최악의 경우 **O(N²)**의 시간 복잡도를 가짐





  


  





