import sys

value = sys.argv[1]  # 문자열 그대로 받음

# 예시: 숫자로 처리
try:
    num = float(value)
    result = num * 10
    print(result)
except:
    print(f"입력받은 값: {value}")
