# 집합(Set) - 중복된 요소 허용 안함, 순서가 없음, 중괄호({})로 사용
x = {2,4,3,1,5}
print(x)
y = {'aaa','bbb','ccc'}
print(y)

# set 함수 이용해서 생성 - 리스트, 튜플 등의 객체를 받아 중복되지 않은 요소들로 이루어진 집합으로 변환
x = set([2,4,3,1,5])
print(x)
y = set(['aaa','bbb','ccc'])
print(y)

# 집합 연산자
    # | -> 두 집합의 모든 요소를 포함하는 집합을 만드는 연산자 (합집합)
    # & -> 두 집합에 공통으로 포함된 요소들로 이루어진 집합을 만드는 연산자 (교집합)
    # - -> 첫번째 집합에는 있지만 두번째 집합에는 없는 요소들로 이루어진 집합을 만드는 연산자 (차집합)
    # ^ -> 두 집합 중 하나에만 속하는 요소들로 이루어진 집합을 만드는 연산자 (대칭 차집합)
x = {1,2,3}
y = {3,4,5}
print(x | y)
print(x & y)
print(x - y)
print(x ^ y)

# 부분 집합 / 상위 집합 연산자
x = {1,2}
y = {1,2,3}
z = {1,2,3}
print(x <= y)
print(x < y)
print(y <= z)
print(y < z)

# in 연산자
x = {1,2,3,4}
print(1 in x)
print(5 in x)
print(1 not in x)
print(5 not in x)

# len 함수
s = {1,2,3}
print(len(s))

# min / max 함수
print(max(s))
print(min(s))

# bool 함수
print(bool(set()))
print(bool({1,2}))

# 집합 함수
    # union -> 두 집합의 모든 요소를 포함하는 집합을 만드는 연산자 (합집합)
    # intersection -> 두 집합에 공통으로 포함된 요소들로 이루어진 집합을 만드는 연산자 (교집합)
    # difference -> 첫번째 집합에는 있지만 두번째 집합에는 없는 요소들로 이루어진 집합을 만드는 연산자 (차집합)
    # symmetric_difference -> 두 집합 중 하나에만 속하는 요소들로 이루어진 집합을 만드는 연산자 (대칭 차집합)
x = {1,2,3}
y = {3,4,5}
print(x.union(y))
print(x.intersection(y))
print(x.difference(y))
print(x.symmetric_difference(y))

# 부분 집합 / 상위 집합 함수
    # issubest <
    # issuperset >
    # isdisjoint - 공통된 요소가 1개라도 있으면 false
x = {1,2}
y = {1,2,3}
z = {3,4}
print(x.issubset(y))
print(y.issubset(x))
print(x.isdisjoint(z))

# 요소 추가 함수 add, update
x = {1,2}
x.add(3)
print(x)
x.add(2)
print(x)

x = {1,2}
x.update([3,4])
print(x)

# 요소 제거 함수 remove
x = {1,2}
x.remove(2)
print(x)

print()

# 사전 Dictionary - Key와 Value 쌍으로 데이터를 저장하는 비시퀀스 자료형, 중복 허용 안함, 순서 무관, 중괄호로 생성
x = {10:'aaa', 20:'bbb', 25:'ccc'}
print(x)

# dict 함수 사용하여 생성 - 리스트, 튜플 등 반복 가능한 객체를 받아 사전으로 변환
x = [(10,'aaa'),(20,'bbb'),(25,'ccc')]
y = dict(x)
print(y)

# 키값 사용한 조회
x = {10:'aaa', 20:'bbb', 25:'ccc'}
print(x[10])

# 키-값 추가 또는 기존 키-값 수정
x = {'aaa':1, 'bbb':2, 'ccc':3}
x['ddd'] = 4
x['bbb'] = 5
print(x)

# in 연산자 - key 가 존재하는지 확인
x = {10:'aaa', 20:'bbb', 25:'ccc'}
print(10 in x)
print('aaa' in x)

# len 함수
print(len(x))

# min / max 함수
print(max(x))
print(min(x))

# bool 함수
print(bool({}))
print(bool({10:'aaa',20:'bbb'}))

# keys 함수 - 사전에 등록된 모든 키를 반환
print(x.keys()) 

# values 함수 - 사전에 저장된 모든 값을 반환
print(x.values())   

# items 함수 - 사전에 저장된 모든 키-값 쌍을 튜플 형태로 반환
print(x.items())

# get 함수 - 주어진 키에 대응하는 값을 반환
print(x.get(10))
print(x.get(30))

# clear 함수 - 사전에 저장된 모든 항목을 삭제
x.clear()   
print(x)

# pop 함수 - 특정 키를 제거하고 그 키에 대응하는 값을 반환
x = {10:'aaa', 20:'bbb', 25:'ccc'}
print(x.pop(20))
print(x)

# 실습문제 p153
#1
a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(a & b)

#2
a = {10,20,30}
a.add(40)
print(a)

#3
a = {10,20,30,40}
print(max(a))

#4
a = {5,10,15}
b = {5,10,15,20}
print(a<b)

#5
a = {'a':1, 'b':2, 'c':3}
print(a['b'])

#6
a['d'] = 4
print(a)

#7
a = {'a':1, 'b':2, 'c':3}
print('d' in a)

#8
a = {1,2,3}
a.add(4)
print(a)

#9
a = {'x':10, 'y':20, 'z':30}
a.pop('y')
print(a)

#10
a = {'a':1, 'b':2, 'c':3}
a['d'] = 4
print(a)


