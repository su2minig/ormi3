# 반복문(while, for), 조건문(if, elif, else)

a = 10
while a < 15:
    print('hello world')
    a += 1  # 이게 없으면 무한루프

while a < 15:
    print('hello world')
    # a += 1  # 이게 없으면 무한루프
    if a > 9:
        break  # 루프를 빠져나온다.
else:
    print('hello python')  # 루프가 정상적으로 종료되었을 때 실행된다.

l = [10, 20, 30, 40]
s = {10, 20, 30, 40}
for i in l: # l의 자리는 순회가능한 객체(iterable)
    print(i) # 10, 20, 30, 40

for i in s:
    print(i) # 40, 10, 20, 30

d = {'one':1, 'two':2, 'three':3}
for i in d:
    print(i) # one, two, three 키값만 나온다.

for i in range(10): # 0 ~ 9
    print(i) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# range(시작, 끝, 증가값), range(start, stop, step)
print(range(10))    # range(0, 10)
print(type(range(10)))  # <class 'range'>
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(1, list(range(5, 10)))    # [5, 6, 7, 8, 9]
print(2, list(range(5, 10, 2))) # [5, 7, 9]
print(3, list(range(10, 5, -1)))    # [10, 9, 8, 7, 6]

for i in 'hello world':
    print(i)    # h, e, l, l, o, , w, o, r, l, d

for i in range(10):
    print(i)
    if i == 5:
        break 
else:
    print('good job') # break로 빠져나오면 실행되지 않는다.

l = list(range(101))
print(l)    # 0 ~ 100
ll = []
for i in range(10):
    ll.append(i)
print(ll)   # 0 ~ 9

ll = [i for i in range(10)] # 리스트 컴프리헨션

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i, '*', j, '=', i*j)
    print('{} X {} = {}'.format(i, j, i*j))

lll = ['{} X {} = {}'.format(i, j, i*j) for i in range(2, 10) for j in range(1, 10)]
print(lll) 

l = [(1, 10), (2, 20), (3, 30)]
for i in l:
    print(i)    # (1, 10), (2, 20), (3, 30) 튜플이 나온다.

for i, j in l:
    print(i, j) # 1 10, 2 20, 3 30 # 언패킹 튜플이 아니다.

for i, j in enumerate(range(100, 1000, 100), 1):
    print(i, j) # 1 100, 2 200, 3 300, 4 400, 5 500, 6 600, 7 700, 8 800, 9 900
    # 순위를 매길 때 사용한다.

for i in range(10):
    pass   # 아무것도 하지 않는다. 에러가 나지 않는다. 나중에 구현할 때 사용한다.
    continue    # 다음 루프로 넘어간다.
    print('hello world')    # 실행되지 않는다. 이유는 continue 때문이다.