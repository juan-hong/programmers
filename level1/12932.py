"""
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다
"""

"""
처음으로 리스트 컴프리핸션? 을 사용함
"""

def solution(n):
    return [int(x) for x in reversed(str(n))]

print(solution(12345))