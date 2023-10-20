a = 2019
b = 9
c = 24
# 2019/09/24
print(a, b, c, sep='/')
print(a, b, c, end='-')

a = 10
b = '10'
print(str(a) + b) # 1010 형변환

a = True
b = False
print(type(a)) # <class 'bool'>
print(bool(' ')) # True
print(bool('')) # False
print(bool('1')) # True
print(bool('0')) # True
print(bool('-1')) # True
print(bool(None)) # False

a = 3
b = 10
print(a + b)    # 13
print(a - b)    # -7
print(a / b)    # 0.3
print(b // a)   # 3
print(a * b)    # 30
print(b ** a)   # 1000 
print(a % b)    # 3

a = 10
b = 3
print(a > b)    # True
print(a < b)    # False
print(a >= b)   # True
print(a <= b)   # False
print(a == b)   # False
print(a != b)   # True

a = True    # 1
b = False   # 0
print(a and b)  # False
print(a or b)   # True
print(not a)    # False
print(not b)    # True

# 할당연산
a = 10
a = a + 10  
a += 10
print(a)    # 30

# bit 연산
a = 40 # 00101000
b = 14 # 00001110
print(a & b)    # 8
# &, |, ^, ~
print(bin(a))[2:].zfill(6)   # 0b101000
print(bin(b))[2:].zfill(6)   # 0b001110
# 101000
# 001110
# 001000

def f(x, y):    # x와 y는 파라미터
    z = x + y
    return z
print(f(10, 20))    # 10과 20은 아규먼트

def ff():
    print('1')
    print('2')
    print('3')
    # return None
print(4)
print(ff())    # 4 1 2 3 None (함수ff에 return 값이 없기 때문에 None)

def circle(r):
    width = r * r * 3.14
    return width
print(circle(10))   # 314.0

a = 10
def aplus():
    # global a  # 전역변수 a를 사용하겠다 글로벌은 주의해서 사용해야함
    a += 10
    return a
print(aplus())  # global a를 사용하지 않으면 에러 발생 이유는 함수 내부에서 a를 찾지 못하기 때문에

