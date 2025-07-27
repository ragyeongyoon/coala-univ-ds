# 01_python_basics.py

# 숫자의 연산
print("[숫자의 연산 예시]")
a = 1
b = 5
print(a + b)   # 결과: 6
c = a - b
print(c)       # 결과: -4
c = b % 2
print(c)       # 결과: 1
c = b // 2
print(c)       # 결과: 2

# 문자의 연산
print("\n[문자의 연산 예시]")
a = "Hello"
b = "World"
print(a + b)  # 결과: HelloWorld
print("hello" * 3)  # 결과: hellohellohello

# 문자와 숫자 더하기
print("\n[문자와 숫자 더하기]")
a = 100
b = "원"
print(str(a) + b)  # 결과: 100원

# 입력문
print("\n[입력문 예시]")
name = input("이름을 입력해주세요 : ")
age = input("나이를 입력해주세요 : ")
print("[입력자의 정보 요약]")
print("이름은", name)
print("나이는", age)
age = int(age)
g_age = age - 1
print("만 나이는", g_age)
