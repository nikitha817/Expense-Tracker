import numpy as np
# [maths, physics, chemistry, biology, english]
subjects = ["Maths", "Physics", "Chemistry", "Biology", "English"]
students = ["Student 1", "Student 2", "Student 3"]
marks = np.array([[39, 58, 76, 95, 65],
                 [40, 59, 77, 96, 66],
                 [92, 44, 68, 88, 70]])
Average_marks = np.mean(marks, axis=1).round(2)
print("=" *50)
print("Student Marks Analysis")
print("=" *50)
print(f"{'Highest Marks':<25}: {np.max(marks)}")
print(f"{'Lowest Marks':<25}: {np.min(marks)}")
print(f"{'Average Marks':<25}: {np.mean(marks).round(2)}")
print(f"{'Highest Total Marks':<25}: {np.max(np.sum(marks, axis=1))}")
print(f"{'Lowest Total Marks':<25}: {np.min(np.sum(marks, axis=1))}")
print(f"{'Weakest subject':<25}: {subjects[np.argmin(np.sum(marks, axis=0))]}")
print(f"{'Strongest subject':<25}: {subjects[np.argmax(np.sum(marks, axis=0))]}")
print(f"{'Average Student Marks':<25}: {Average_marks}")
print(f"{'Grade ':<25}: {np.where(Average_marks >= 90, 'O', np.where(Average_marks >= 80, 'A', np.where(Average_marks >= 70, 'B', np.where(Average_marks >= 60, 'C', 'D'))))}")
print("=" *50)
print("Individual Student Analysis")
print("=" *50)
for i in range(len(students)):
    print(f"{students[i]}".center(50))
    print(f"{'Marks':<25}: {Average_marks[i]}")
    print(f"{'Grade ':<25}: {np.where(Average_marks[i] >= 90, 'O', np.where(Average_marks[i] >= 80, 'A', np.where(Average_marks[i] >= 70, 'B', np.where(Average_marks[i] >= 60, 'C', 'D'))))}")