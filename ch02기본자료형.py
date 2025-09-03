#논리형

print()

print(True == True)
print(True == False)
print(True != True)
print(True != False)
print(True < True)
print(True < False)
print(True <= True)
print(True <= False)
print(True > False)

print()

print(True and True)
print(True and False)
print(False and False)

print()

print(True or True)
print(True or False)
print(False or False)

print()

print(not True)
print(not False)

print()

#숫자형
#정수형 - 소수점 없는 양수, 음수, 0
a, b, c = 24, -3, 0
print(a,b,c)

#2진수 - 숫자앞에 0b
#8진수 - 숫자앞에 0o
#16진수 - 숫자앞에 0x
a, b, c = 0b101, 0o507, 0xA2F
print(a, b, c)

#실수형 - 소수점이 있는 숫자
a, b, c, d, e = 3.14, -2.15, 1.0, 2, 3.
print(a, b, c, d, e)

#숫자형
a = 123
print("%d" %a)
b = 2748
print("%o %d %x %X" % (b,b,b,b))
c = 3.14
print("%f %f" % (c, -2.))

# %형식화 - 정수형 출력 시, %와 d 사이에 숫자를 넣으면 지정한 폭만큼 자리를 확보함.
a = 123
print("%-12d %12d" % (a, a))
print("%-012d %012d" % (a, a))
print("%2d" % a)

a = 123.456
print("%-12f %12f" % (a, a))
print("%.4f" % a)
print("%-12.1f %12.4f" % (a, a))
print("%-012.1f %012.4f" % (a, a))
print("%3.2f" % a)

print()
# 문자열 앞에 f를 붙이면 중괄호와 변수 이름만으로 문자열에 원하는 변수를 삽입할 수 있다
a, b = 123, 3.14
print(f"{a}")
print(f"{a} {b}")

a = 123
print(f"{a:<12} {a:^12} {a:>12}")
print(f"{a:x<12} {a:x^12} {a:x>12}")
print(f"{a:2}")

print()

a = 123.456
print(f"{a:<12} {a:^12} {a:>12}")
print(f"{a:.4f}")
print(f"{a:<12.1f} {a:^12.1f} {a:>12.1f}")
print(f"{a:x<12.1f} {a:x^12.1f} {a:x>12.1f}")
print(f"{a:3.2f}")

#format 함수
a, b = 123, 3.14
print("{0}" .format(a))
print("{0} {1}" .format(a, b))

print()

a = 123
print("{:<12} {:^12} {:>12}".format(a, a, a))
print("{:y<12} {:y^12} {:y>12}".format(a, a, a))
print("{:2}".format(a))

a = 123.456
print("{:<12} {:^12} {:>12}".format(a,a,a))
print("{:.4f}".format(a))
print("{:<12.1f} {:^12.1f} {:>12.1f}".format(a,a,a))
print("{:_<12.1f} {:_^12.1f} {:_>12.1f}".format(a,a,a))
print("{:3.2f}".format(a))

print()

# +,-,*,/,//(몫),%(나머지),**(거듭제곱)
a, b = 5, 3
print(a+b, a-b, a*b, a/b)
print(a//b, a%b, a**b)

# ==(같은지 비교), !=(다른지 비교), <,>,<=,>=
print(7==7)
print(7==8)
print(7!=7)
print(7!=8)
print(7<7)
print(7<8)
print(7<=7)
print(7<=8)

print()

# 논리연산자 and, or not
print(7==7 and 7==7)
print(7==7 and 7==8)
print(7==8 and 7==8)

print()

print(7==7 or 7==7)
print(7==7 or 7==8)
print(7==8 or 7==8)

print()

print(not 7==7)
print(not 7==8)

print()
# 대입연산자 / 복합대입연산자
# = : 왼쪽의 변수에 오른쪽의 값을 대입
# += : 왼쪽의 변수에 오른쪽의 값을 더한 후, 그 결과값을 왼쪽의 변수에 대입
# -= : 왼쪽의 변수에 오른쪽의 값을 뺀 후, 그 결과값을 왼쪽의 변수에 대입
# *= : 왼쪽의 변수에 오른쪽의 값으로 곱한 후, 그 결과값을 왼쪽의 변수에 대입
# /= : 왼쪽의 변수에 오른쪽의 값으로 나눈 후, 그 결과값을 왼쪽의 변수에 대입
# %= : 왼쪽의 변수에 오른쪽의 값으로 나눈 후, 그 나머지을 왼쪽의 변수에 대입
# **= : 왼쪽의 변수에 오른쪽의 값으로 제곱한 후, 그 결과값을 왼쪽의 변수에 대입
# //= : 왼쪽의 변수에 오른쪽의 값으로 나눈 후, 그 몫을 왼쪽의 변수에 대입
a, b = 5, 3
a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)
a %= b
print(a)
a **= b
print(a)
a //= b
print(a)

#연산자 우선순위
a = not 2**3 + 5 >= 0
print(a)

#자료형 확인
print(type(True))
print(type(1))
print(type(3.14))


#실습문제 p65
#1
a, b, c = 10, -5, 0
print(a, b, c)

#2
a, b, c = 0b101, 0o123, 0xABC
print(a, b, c)

#3
a = int(input("입력1 : "))
b = int(input("입력2 : "))
# print(a)
# print(b)
print(a*b)

#4
a = int(input("입력1 : "))
b = int(input("입력2 : "))
print(a > 5 and b > 5)

#5
a = int(input("입력1 : "))
b = int(input("입력2 : "))
print("몫 : ", a//b); print("나머지 : ", a%b)

#6
a, b = 123, 3.14
print("%d %.1f" % (a, b))

#7
a = int(input("입력1: "))
b = int(input("입력2: "))
c = int(input("입력3: "))
print(a >= 0 or b >= 0 or c >= 0)

print()
