
# 리스트 관련 메서드

# append()
# 리스트에 원소 삽입
# 변수명.append()             
# 시간복잡도 o(1)

a = [1,4,5]
a.append(6)
print(a) # [1,4,5,6]  



# sort() 
# 정렬 기능 
# 변수명.sort()                -> 오름차순 
# 변수명.sort(reverse = True)  -> 내림차순
# 시간복잡도 o(NlogN)

a = [1,4,5]
a.sort();
print(a) # [1,4,5] 
a.sort(reverse = True)
print(a) # [5,4,1] 




# reverse()
# 리스트의 원소의 순서를 모두 뒤집어 놓음           
# 변수명.reverse()            
# 시간복잡도 o(N)

a = [1,4,5,7,8]
a.reverse()
print(a) # [8,7,5,4,1]  




# insert()
# 특정한 인덱스 위치에 원소를 삽입
# 변수명.insert(삽입할 위치 인덱스, 삽입할 값)  
# 시간복잡도 o(N)

a = [1,4,5]
a.insert(0,6)
print(a) # [6,1,4,5]  
a.insert(2,9)
print(a) # [6,1,9,4,5]




# count()
# 리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용
# 변수명.count(특정 값)              
# 시간복잡도 o(N)

a = [1,4,5,7,1,1]
print(a.count(4)) # 1  
print(a.count(1)) # 3  




# remove()
# 특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러개면 하나만 제거
# 변수명.remove(특정 값)                                            
# 시간복잡도 o(N)                    

a = [1,4,5,8,3,8]
a.remove(5)
print(a) # [1,4,8,3,8]  

a = [1,4,5,8,3,8]
a.remove(8) 
print(a) # [1,4,5,3,8]  8이 여러개일 경우 앞에서부터 해당 원소 하나만 제거됨



# 리스트에서 특정 값을 가지는 원소 모두 제거하기

a = [1,2,3,4,5,5,5]

remove_set = {3,5} # 집합 자료형
result = [i for i in a if i not in remove_set]
print(result) #[1,2,4]











      


 