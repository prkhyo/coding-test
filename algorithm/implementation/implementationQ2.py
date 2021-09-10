






# <문제> 왕실의 나이트


# 1. 문제 설명
# 행복 왕국의 왕실 정원은 체스판과 같은 8 x 8 좌표 평면임 -> 2차원 공간
# 왕실 정원의 특정한 한 칸에 나이트가 서있음
# 나이트는 매우 충성스러운 신하로서 매일 무술을 연마함
# 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없음
# 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있음
#   수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
#   수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
# 이처럼 8 x 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 
# 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성해라
# 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현함
#   c2에 있을 때 이동할 수 있는 경우의 수 -> 6가지
#   a1에 있을 때 이동할 수 있는 경우의 수 -> 2가지
  





# 2. 문제 조건
# 난이도 1, 풀이시간 20분, 시간제한 1초, 메모리 제한 128MB
# 입력 조건: 첫째 줄에 8 x 8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 
#           두 문자로 구성된 문자열이 입력됨. 
#           입력문자는 a1처럼 열과 행으로 이뤄짐.
# 출력 조건: 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력


# ( a 1 ) ( b 1 ) ( c 1 ) ( d 1 ) ( e 1 ) ( f 1 ) ( g 1 ) ( h 1 ) 
# ( a 2 ) ( b 2 ) ( c 2 ) ( d 2 ) ( e 2 ) ( f 2 ) ( g 2 ) ( h 2 ) 
# ( a 3 ) ( b 3 ) ( c 3 ) ( d 3 ) ( e 3 ) ( f 3 ) ( g 3 ) ( h 3 ) 
# ( a 4 ) ( b 4 ) ( c 4 ) ( d 4 ) ( e 4 ) ( f 4 ) ( g 4 ) ( h 4 ) 
# ( a 5 ) ( b 5 ) ( c 5 ) ( d 5 ) ( e 5 ) ( f 5 ) ( g 5 ) ( h 5 ) 
# ( a 6 ) ( b 6 ) ( c 6 ) ( d 6 ) ( e 6 ) ( f 6 ) ( g 6 ) ( h 6 ) 
# ( a 7 ) ( b 7 ) ( c 7 ) ( d 7 ) ( e 7 ) ( f 7 ) ( g 7 ) ( h 7 ) 
# ( a 8 ) ( b 8 ) ( c 8 ) ( d 8 ) ( e 8 ) ( f 8 ) ( g 8 ) ( h 8 ) 





# 내가 짜본 코드  

 
p = input()
dx = [1, -1, 1, -1, -2, -2, 2, 2]
dy = [2, 2, -2, -2, 1, -1, 1, -1] 
t =list(map(chr, range(97, 105)))
count = 0


for k in range(8):
    x = int(p[1]) + dx[k]
    y = ord(p[0]) + dy[k] 

    if x < 1 or x > 8 or y < 97 or y > 104:
        continue
    else:
        count += 1    
                   
print(count)





# 3. 문제 해결 아이디어
# 요구사항대로 충실히 구현하면 되는 문제
# 나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동이 가능한지 확인
#   리스트를 이용하여 8가지 방향에 대한 방향 벡터를 정의




# 4. 답안 예시  

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] 

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)        










