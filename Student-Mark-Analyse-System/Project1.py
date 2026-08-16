import numpy as np
# [maths, physics, chemistry, biology, english]
marks = np.array([[39, 58, 76, 95, 65],
                 [40, 59, 77, 96, 66],
                 [92, 44, 68, 88, 70]])
#print(type(marks[0][0]))
# print(marks.shape)
print(np.max(marks))
print(np.min(marks))
print(np.mean(marks))