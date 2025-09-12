#문자열
a, b, c, d = "abc", 'abc', '123', "123"
print(a,b,c,d)

x = "she's gone"
print(x)
y = '"Python" is fun'
print(y)

x = "she\"s gone"
print(x)
y = "\"Python\" is fun"
print(y)

x = "she's gone"
print(x)
y = """"Python" is fun"""
print(y)

x = "첫 번째 줄\n두 번째 줄\n세 번째 줄"
print(x)

x = "첫 번째 줄\n" \
    "두 번째 줄\n" \
    "세 번째 줄"
print(x)

print()

x = """첫 번째 줄
두 번재 줄
세 번째 줄"""
print(x)

a = "abc"
print("%s" % a)
b = "x"
print("%c %s" % (b, b))
print("%c%%" %b)

x = "abc"
print("%-10s %10s" %(x, x))
print("%2s" %x)

a = 'abc'
print(f"{a}")
print(f"{{{a}}}")

#생략하고 format함수 이용해서 하는걸로 넘어간다
a = 'abc'
print("{0}".format(a))
print("{{{0}}}".format(a))

x = 'abc'
print("{:<10} {:^10} {:>10}".format(x,x,x))
print("{:x<10} {:y^10} {:z>10}".format(x,x,x))
print("{:2s}".format(x))

#문자열 인덱싱
s = 'Hello'
print(s[0], s[1], s[2], s[3], s[4])
print(s[-5], s[-4], s[-3], s[-2], s[-1])

#문자열 슬라이싱(순방향)
s = 'Hi Python'
print(s[1:8:2])
print(s[1:8:])
print(s[1::2])
print(s[1::])
print(s[:8:2])
print(s[:8:])
print(s[::2])
print(s[::])

#역방향 굳이 해야되노?

#문자열과 함께 사용하는 연산자
# + = 문자열 연결, * = 문자열 반복
a, b = "Hello", "World"
print(a+b)
print(a*3)

#비교 연산자 -> == != < <= > >= -> 대문자가 소문자보다 값이 작음. 앞에있는 알파벳이 값이 작음. 한글은 앞에있는게 값이 작음.
#대입 연산자 -> = += *=
a += b
print(a)
a *=2
print(a)

# in 연산자
print("Hello" in "Hello Python")
print("hello" in "Hello Python")
print("Hello" not in "Hello Python")
print("hello" not in "Hello Python")

# len 함수 - 문자열의 문자 개수 반환
s = 'Hello'
print(len(s))

# min / max 함수 - 가장 작은 / 큰 문자 반환
s = 'hello'
print(max(s))
print(min(s))

# bool 함수 - 빈 문자열 - false, 그 외 - true
print(bool(''))
print(bool(""))
print(bool('sdsd'))

# count 함수 - 문자열에서 해당되는 문자열의 문자 개수를 세는 함수
# str.count(sub, start, end)
x = "hahaha"
print(x.count('h'))
print('hahah'.count('h'))
print('hahaha'.count('h', 1, 5))
print(x.count('ah'))

# upper 함수 - 모든 알파벳을 대문자로 변환
x = 'Hello Python'
print(x.upper())   
print(x)
y = x.upper()
print(y)

# lower 함수
print(x.lower())
print(x)

# isalnum 함수 - 문자열이 알파벳 또는 숫자로만 구성되어 있으면 true, 아니면 false
x = 'HelloPython'
print(x.isalnum())
y = 'Hello123'
print(y.isalnum())
z = '12 3'
print(z.isalnum())

# isalpha - 문자열이 알파벳으로만 구성되어있으면 true
# isdigit = 함수열이 수자면 true

# find 함수 - 문자열에서 특정 문자열(또는 문자)의 시작 위치(인덱스)를 찾는 함수
# str.find(sub,start,end)
x = 'hahaha'
print(x.find('h'))
print(x.find('h',1,5))
print(x.find('ah'))
print(x.find('world'))

# split 함수 - 문자열을 매개변수로 전달된 문자인 구분자(기본값은 공백)를 기준으로 나누어 리스트로 변환하는 함수
# str.split(sep, maxsplit)
x = 'Hello Python World'
print(x.split())
print(x)
x = x.split()
print(x)
y = 'aaa,bbb,ccc'
y= y.split(',')
print(y)
z = 'aaa,bbb,ccc'
print(z.split(',',1))

# strip / lstrip / rstrip 함수 - 문자열의 양쪽 끝에서 특정 문자(기본값은 공백)를 제거하는 함수
# str.strip(chars)
x = ' Hello Python '
x = x.strip()
print(x)
y = '!!Hello Python!!'
y = y.strip('!')
print(y)
x = ' Hello Python '
print(x.lstrip())
print(x.rstrip())
y = '!!Hello Python!!'
print(y.lstrip('!'))
print(y.rstrip('!'))

# replace 함수 = 문자열 내에서 특정 문자열을 다른 문자열로 바꾸는 함수
# str.replace(old,new,count)
x = 'Hello Python'
print(x.replace('Python','World'))
print(x)
x = x.replace('Python','World')
print(x)
y = 'Hello Python Python'
y = y.replace('Python','World')
print(y)
z = 'Hello Python Python'
result = z.replace('Python','World',1)
print(result)

print()

# 리스트
a = [1, 2, 3, True, 'ABC', 'DEF']
print(a)
b = list((1,2,3, True, False, 'ABC', 'EDF'))
print(b)

# 리스트 인덱싱
a = [10,20,30,40,50]
print(a[0],a[1],a[2],a[3],a[4])
print(a[-5],a[-4],a[-3],a[-2],a[-1])

# 리스트 슬라이싱(순방향)
# list[start:stop:step] - start: 슬라이싱이 시작되는 인덱스, stop: 슬라이싱이 끝나는 인덱스, step: 몇칸씩 건너뛸지에 대한 값
a = [10,20,30,40,50,60,70,80,90]
print(a[1:8:2])
print(a[1:8:])
print(a[1::2])
print(a[1::])
print(a[:8:2])
print(a[:8:])
print(a[::2])
print(a[::])

# 리스트 슬라이싱(역방향) 을 굳이 해야하노

# 리스트 값 수정
# list[index] = value
a = [1,2,3,4,5]
a[1] = 9
print(a)

# 리스트 값 여러개 수정
# list[start:end] = new_values
a = [1,2,3,4,5]
a[1:4] = [6,7,8]
print(a)
a[1:3] = [2,3,4,5]
print(a)

# 리스트 값 삭제
# del list[index]
a = [1,2,3,4,5]
del a[1]
print(a)

# 리스트 값 여러개 삭제
# del list[start:end]
a = [1,2,3,4,5]
del a[1:4]
print(a)

# 리스트 연산자
a = [10,20,30,40,50]
b = ['ab','cd','ef','gh']
print(a+b)
print(a*3)

a = [1,2,3]
b = [4,5,6]
print(a == b)
print(a != b)
print(a < b)
print(a >= b)

a = [10,20,30]
b = [15,25,35]
a += b
print(a)
a *= 2
print(a)

a = [10,20,30]
print(10 in a)
print(15 in a)
print(10 not in a)
print(15 not in a)

# len 함수 - 리스트 내의 요소의 개수 알려줌
a = [10,20,30,40,50]
print(len(a))

# min / max 함수 - 리스트에서 가장 작은 / 큰 값 알려줌
a = [10,30,20,50,40]
print(max(a))
print(min(a))

# bool 함수 - 빈 리스트는 false, 그 외엔 true
print(bool([]))
print(bool([1,2]))

# count 함수 - 리스트 내의 특정 값의 개수를 알려줌
    # list.count(value)
a = [10,20,30,10,20,30]
print(a.count(10))
print(a.count(5))

# index 함수 - 해당 요소가 처음으로 등장하는 인덱스 번호를 알려줌
    # list.index(value, start, end)
a = [10,20,30,10,20,30]
print(a.index(20))
print(a.index(30,3))

# append 함수 - 리스트 마지막 요소 뒤에 값을 추가함
    # list.append(value)
a = [1,2,3]
a.append(4)
print(a)

# extend 함수 - 리스트의 끝에 다른 리스트나 튜플, 문자열을 추가함
    # list.extend(value)
a = [1,2,3]
b = [4,5,6]
b.extend(a)
print(b)
a.extend('abc')
print(a)

# insert 함수 - 리스트의 특정 위치에 요소를 삽입함
    # list.insert(index, value)
a = [10,20,30]
a.insert(1, 15)
print(a)

# copy 함수 - 리스트를 복사함
    # list.copy()
a = [1,2,3]
b = a.copy()
b[0] = 10
print(a)
print(b)

# remove 함수 - 리스트에서 첫 번째로 나타나는 특정 요소를 제거함
    # list.remove(value)
a = [1,2,3,2,4]
a.remove(2)
print(a)

# pop 함수 - 리스트에서 특정 인덱스에 있는 요소를 제거하고 그 값을 반환함
    # list.pop(index) - index를 지정하지 않으면 리스트의 마지막 요소를 제거하고 값을 반환함
a = [10,20,30,40,50]
print(a.pop())
print(a)
print(a.pop(1))
print(a)

# reverse 함수 - 리스트의 요소를 역순으로 재배열함
a = [1,2,3,4,5]
a.reverse()
print(a)

# sort 함수 - 리스트의 항목들을 기준에 따라 정렬함
    # list.sort(key, reverse) - key : 정렬 기준을 정의하는 함수, reverse : 정렬 방식(True:내림차순, False:오름차순) 설정. 기본값은 오름차순
a = [3,1,4,1,5,9,2]
a.sort(reverse=True)
print(a)
b = ['cherry','banana','apple','durian']
b.sort(key=len)
print(b)

# clear 함수 - 리스트를 모두 제거
a = [1,23,4,5]
a.clear()
print(a)

# 다차원 리스트
a = [[1,2], [3,4], [5,6]]
print(a)
print(a[0])
print(a[1][0])
b = [[1,2,3],[4,5],[6,7,8,9]]
print(b[0])

# 튜플 - 변경할 수 없는 자료형
    # 튜플명 = (요소1,) - 한개의 요소일 경우
    # 튜플명 = (요소1,요소2,) - 여러개 요소일 경우
a = (1,2,3, True, False, 'ABC', 'DEF')
print(a)
a = (10,20,30,40,50)
print(a[0],a[1],a[2],a[3],a[4])
print(a[1:4:2])

print()

# 실습문제 p126
#1
a = "Python Program"
print(a[1],a[-1])

#2
a = [10,20,30,40,50]
print(a[0],a[4])

#3
a = [1,2,3,4,5]
print(a[1:4:])

#4
a = input('문자열 입력 : ')
print(a[1:-1:])

#5
a = input('문자열 입력 : ')
print(len(a))

#6
a = input('문자열 입력 : ')
print(a.upper())

#7
a = input('문자열 입력 : ')
b = input('문자열 입력 : ')
print(b in a)

#8
a = input('문자열 입력 : ')
print(a[::-1])

#9
a = 'Hello, World!'
print(a[::-1])

#10
a = "Python is fun"
print(a.split())

#11
a = [1,2,3,4,5]
a.reverse()
print(a)

#12
a = input('문자열 입력 : ')
print(a == a[::-1])

#13
a = [20,30,10,70,30]
a.remove(max(a))
a.remove(min(a))
print(a)