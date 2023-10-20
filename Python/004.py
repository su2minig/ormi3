a = 10
if a >= 10:
    print('hello world')

if a > 10:
    print('hello world')
elif a < 20:
    print('good job')   # 이게 실행된다.


a = 30
if a == 10:
    print('hello world')
elif a < 20:
    print('good job')
else:
    print('else')   # 이게 실행된다.
# elif는 여러개 사용할 수 있다.
# elif와 else는 두개는 if없이 사용할 수 없다.

# class
class Car():
    max_speed = 300
    max_people = 5
    def start(self):
        print('출발')
    def stop(self):
        print('정지')

k9 = Car()
print(k9.max_speed) # 300
print(k9.max_people)    # 5

# class name 첫글자는 대문자로

class Car(object):
    max_speed = 300
    max_people = 5
    def start(self):
        print('출발')
    def stop(self):
        print('정지')
    def __str__(self):
        return 'hello world'
    def __init__(self):
        print('인스턴스가 생성되었습니다.')

class Hybrid(Car):  # class Car 상속
    battery = 1000
    batteryKM = 300

k4 = Hybrid()  # 인스턴스 생성
print(k4.max_speed) # 300
print(k4)   # hello world

