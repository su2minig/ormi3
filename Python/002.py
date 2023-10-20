# 리스트, 튜플, 딕셔너리, 셋

l = [100, 200, 300, 400, 500]
print(l)
print(type(l))  # <class 'list'>
# 변경이 가능한 자료형
# 순서가 있는 자료형
print(l[1]) # 200
l[2]    # 300

l.append(600)   # 맨 뒤에 추가
l.clear()   # 모두 삭제
l.copy()    # 복사
l.count(100)    # 100의 개수 100은 아규먼트
l.extend([700, 800])    # 리스트를 확장
print(l)    # [100, 200, 300, 400, 500, 600, 700, 800]
print(l.index(100)) # 0
l.insert(3, 1000)   # 3번째 자리에 1000을 삽입
l.pop() # 맨 뒤의 값을 꺼내고 삭제
l.append(100)   # 맨 뒤에 추가
l.remove(100)   # 100을 삭제
print(l)    # [200, 300, 400, 500, 600, 700, 800, 100]
l.reverse() # 뒤집기
l.sort()    # 정렬
# sorted(l)  # 정렬된 리스트를 리턴
# reversed(l)    # 뒤집힌 리스트를 리턴

t = (100, 200, 300)
print(t)    # (100, 200, 300)
print(type(t))  # <class 'tuple'>

# 변경이 불가능한 자료형
# 순서가 있는 자료형

t[0] = 1000 # 에러  변경이 불가능한 자료형
t = (l, 200, 300)   # 튜플 안에 리스트를 넣을 수 있다.
t[0][0] = 1000  # 가능 참조가능한 자료형이 들어가 있기 때문에

s = {100, 200, 300, 300, 300, 300}
print(s)    # {200, 100, 300}
print(type(s))  # <class 'set'>
# 순서가 없는 자료형
# 중복이 없는 자료형
s = {100, 200, 300, 400, 500}
ss = {1, 2, 3, 4, 5}
print(s.union({ss})) # {1, 2, 3, 4, 5, 100, 200, 300, 400, 500}
# 유니온은 합집합

# d = {key: value}

d = {'one': 10, 'two': 20}
# 순서가 없는 자료형
# 키의 중복이 없는 자료형
print(d['one']) # 10 
print(type(d))  # <class 'dict'>

print(d.values())   # dict_values([10, 20])
print(d.keys()) # dict_keys(['one', 'two'])
print(d.items())    # dict_items([('one', 10), ('two', 20)])
l = list(d.items())
print(l[0][1])  # 10

jeju = {'banana': 5000, 'orange': 2000}
seoul = jeju.copy() # 이렇게하면 seoul과 jeju는 다른 주소값을 가진다.
busan = jeju    # 이렇게하면 주소값을 복사하는 것이다.
print(id(jeju)) # 140539379481984
print(id(busan))    # 140539379481984
print(id(seoul))    # 140539379482048
jeju['orange'] = 1000
print(seoul)   # {'banana': 5000, 'orange': 2000
print(busan)  # {'banana': 5000, 'orange': 1000} # 주소값을 복사했기 때문에