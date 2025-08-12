student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for ss in student_scores:
    nilai_baru = ""
    if student_scores[ss] >= 90 and student_scores[ss] < 100:
        nilai_baru = "Sangat Baik"
    elif student_scores[ss] >= 80 and student_scores[ss] < 90:
        nilai_baru = "Baik"
    elif student_scores[ss] >= 70 and student_scores[ss] < 80:
        nilai_baru = "Cukup Baik"
    elif student_scores[ss] < 70:
        nilai_baru = "Jelek!"
    student_grades[f"{ss}"] = nilai_baru
for sg in student_grades:
    for ss in student_scores:
        print(f"Nilai dari {sg} = {student_scores[ss]} / {student_grades[sg]}")