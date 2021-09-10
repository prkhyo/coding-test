





# <문제> 문자열 재정렬


# 1. 문제 설명
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어짐
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력
# 예를 들어 K1KA5CB7 이라는 값이 들어오면 ABCKK13을 출력




# 2. 문제 조건
# 난이도 1, 풀이시간 20분, 시간제한 1초, 메모리 제한 128MB
# 입력 조건: 첫째 줄에 하나의 문자열 s가 주어짐 (1<=s의 길이<=10000)
# 출력 조건: 첫째 줄에 문제에서 요구하는 정답을 출력





# 내가 짜본 코드  

s = input()
number = 0
alpha = ''

for c in s:
    if c.isdigit():
        number += int(c)
    else:
        alpha += c     

result_alpha = ''.join(sorted(alpha))

if number == 0: 
    print(result_alpha)
else:    
    print(result_alpha + str(number))





# 3. 문제 해결 아이디어
# 요구사항대로 충실히 구현하면 되는 문제
# 문자열이 입력되었을 때 문자를 하나씩 확인
#  숫자인 경우 따로 합계를 계산
#  알파벳인 경우 별도의 리스트에 저장
# 결과적으로 리스트에 저장된 알파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력하면 정답





# 4. 답안 예시  

data = input()    
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력 (리스트를 문자열로 변환하여 출력) 
print(''.join(result))   











