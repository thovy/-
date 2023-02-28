from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    # fraction 을 이용해 분수 만들기 - fraction(분자,분모)
    a = Fraction(numer1, denom1)
    b = Fraction(numer2, denom2)
    
    # 분자는 a.numerator, 분모는 a.denominator
    # 더하기
    result = a+b
    
    # 분자 분모 answer 에 넣기
    answer.append(result.numerator)
    answer.append(result.denominator)
    
    return answer