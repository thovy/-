# 계산할 학점 합계
total_score = 0
# 과목 수
total_hakjeom = 0

grade_table = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score_table = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

while True:
    try:
        subject, hakjeom, grade = map(str, input().split());

        if grade != 'P':
            grade_idx = grade_table.index(grade)
            score = score_table[grade_idx]
            total_score += score * float(hakjeom)
            total_hakjeom += float(hakjeom)

    except EOFError:
        break;

answer = round(total_score / total_hakjeom, 6);
print(answer)