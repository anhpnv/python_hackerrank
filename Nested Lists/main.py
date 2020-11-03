if __name__ == '__main__':
    student_score = []
    score_student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_score.append([name, score])
        score_student.append(score)
    score_student = sorted(list(set(score_student)))
    score_student = score_student[1]
    final_student = []
    for n in student_score:
        if n[1] == score_student:
            final_student.append(n[0])
    final_student = sorted(final_student)
    print(*final_student,sep='\n')
    