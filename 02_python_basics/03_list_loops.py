# 03_list_loops.py

# 리스트 기본
print("[리스트 선언 및 인덱싱]")
HumanList = ["인간0", "인간1", "인간2", "인간3", "인간4", "인간5"]
print(HumanList)
print(HumanList[0])
print(HumanList[1])

# 리스트 슬라이싱
print("\n[리스트 슬라이싱]")
print(HumanList[1:3]) #인덱스 직전까지만 출력됨
print(HumanList[-4:-1])
print(HumanList[3:])
print(HumanList[:4])

# 데이터 추가
print("\n[append 함수 예시]")
HumanList.append("이방인1")
print(HumanList)
HumanList.append("이방인2")
print(HumanList)

# 데이터 삭제
print("\n[del 함수 예시]")
del HumanList[0]
print(HumanList)
del HumanList[0]
print(HumanList)

# 리스트 길이
print("\n[len 함수 예시]")
print(len(HumanList))     #리스트 전체의 길이
print(len(HumanList[0]))  #첫번째 문자열 길이

# 반복문 - 횟수 기반
print("\n[for i in range]")
for i in range(0, 10, 2): #a부터 시작해서 b 이전까지, c씩 증가
    print(i)
    print("반복문을 배워봅시다")

# 반복문 - 리스트 기반
print("\n[리스트 반복문]")
HumanList = ["인간0", "인간1", "인간2", "인간3", "인간4"]
print("----인간 명단----")
for i in range(len(HumanList)): #for i in range(6)
    print(HumanList[i])
print("명단 출력 끝")

print("----바로 출력 방식----")
for j in HumanList:
    print(j)
print("명단 출력 끝")
