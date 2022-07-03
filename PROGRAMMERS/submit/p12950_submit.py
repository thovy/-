# 채점을 시작합니다.
# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 28.3MB)
# 테스트 2 〉	통과 (1.26ms, 28.5MB)
# 테스트 3 〉	통과 (1.43ms, 28.3MB)
# 테스트 4 〉	통과 (1.85ms, 28.2MB)
# 테스트 5 〉	통과 (0.09ms, 28.7MB)
# 테스트 6 〉	통과 (0.15ms, 28.7MB)
# 테스트 7 〉	통과 (0.03ms, 28.6MB)
# 테스트 8 〉	통과 (0.11ms, 28.2MB)
# 테스트 9 〉	통과 (1.11ms, 28.8MB)
# 테스트 10 〉	통과 (0.79ms, 28.8MB)
# 테스트 11 〉	통과 (0.49ms, 28.6MB)
# 테스트 12 〉	통과 (0.70ms, 28.9MB)
# 테스트 13 〉	통과 (0.49ms, 28.5MB)
# 테스트 14 〉	통과 (0.64ms, 28.6MB)
# 테스트 15 〉	통과 (0.70ms, 28.8MB)
# 테스트 16 〉	통과 (0.72ms, 28.9MB)
# 테스트 17 〉	통과 (31.51ms, 41.7MB)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0


import numpy as np

def solution(arr1, arr2):
    arr1_array = np.array(arr1)
    arr2_array = np.array(arr2)

    answer = arr1_array + arr2_array
    answer = answer.tolist()
    return answer