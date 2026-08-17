import numpy as np
# [maths, physics, chemistry, biology, english]
subjects = ["Maths", "Physics", "Chemistry", "Biology", "English"]
students = np.array(["Student 1", "Student 2", "Student 3"])

marks = np.array([[39, 58, 76, 95, 65],
                 [40, 59, 77, 96, 66],
                 [92, 44, 68, 88, 70]])
Average_marks = np.mean(marks, axis=1).round(2)
Grade = np.where(Average_marks >= 90, 'O', np.where(Average_marks >= 80, 'A', np.where(Average_marks >= 70, 'B', np.where(Average_marks >= 60, 'C', 'D'))))
def display_summary():
    print("=" *50)
    print("Student Marks Analysis".center(50))
    print("=" *50)
    print(f"{'Average Marks':<25}: {np.mean(marks).round(2)}")
    print(f"{'Highest Total Marks':<25}: {np.max(np.sum(marks, axis=1))}")
    print(f"{'Lowest Total Marks':<25}: {np.min(np.sum(marks, axis=1))}")
display_summary()
def display_subject_analysis():
    print("=" *50)
    print("Subject Analysis".center(50))
    print("=" *50)
    print(f"{'Weakest subject':<25}: {subjects[np.argmin(np.mean(marks, axis=0))]}")
    print(f"{'Strongest subject':<25}: {subjects[np.argmax(np.mean(marks, axis=0))]}")
    print(f"{'Average Student Marks':<25}: {Average_marks}")
display_subject_analysis()
def display_Student_analysis():
    print("=" *50)
    print("Individual Student Analysis".center(50))
    print("=" *50)
    print(f"{'Highest Marks':<25}: {np.max(marks)}")
    print(f"{'Lowest Marks':<25}: {np.min(marks)}")
    for i in range(len(students)):
        print(f"{students[i]}".center(50))
        print(f"{'Marks':<25}: {Average_marks[i]}")
        print(f"{'Grade ':<25}: {Grade[i]}")
display_Student_analysis()
print(f"{'Students with Maths >= 80':<35}: {np.where(marks[0,:] >= 80, students)}")
print(f"{'Students with English >= 90':<35}: {marks[:,-1] >= 90}")