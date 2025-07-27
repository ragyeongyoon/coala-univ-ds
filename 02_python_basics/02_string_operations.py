# 02_string_operations.py

# 문자열 인덱싱
print("[문자열 인덱싱 예시]")
string1 = "브이넥 라이트 다운 베스트"
print(string1[0])  # 브
print(string1[1])  # 이
print(string1[2])  # 넥
print(string1[-1])  # 트
print(string1[-2])  # 스
print(string1[-3])  # 베

# 문자열 슬라이싱
print("\n[문자열 슬라이싱 예시]")
print(string1[0:4])
print(string1[5:])
print(string1[-6:-1])

# replace 함수
print("\n[replace 함수 예시]")
print(string1.replace("라이트", "헤비"))
print(string1)  # 원본은 변하지 않음
string1 = string1.replace("라이트", "헤비")
print(string1)  # 변경된 값 재할당 후 출력

# strip 함수
print("\n[strip 함수 예시]")
string2 = "     25,990원       "
string2 = string2.strip()             #공백 제거
string2 = string2.replace("," , "") #, 제거
string2 = string2[:-1]             #'원' 제거하기
print(string2)

# 문자열에서 원 단위 숫자 추출
cleaned = string2.strip().replace(",","")
print(cleaned)  # 25990
