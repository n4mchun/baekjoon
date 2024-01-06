student_list = [int(input()) for _ in range(28)]
origin = [x for x in range(1, 31)]

no_submit_students = sorted(list(set(origin) - set(student_list)))
print(no_submit_students[0])
print(no_submit_students[1])