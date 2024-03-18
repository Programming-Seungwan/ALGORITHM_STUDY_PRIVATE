from sys import stdin as s
n = int(s.readline().strip())
studentList = []
for _ in range(n):
  studentName, korean, english, math = list(s.readline().strip().split())
  koreanInt = int(korean)
  englishInt = int(english)
  mathInt = int(math)
  studentList.append([studentName, koreanInt, englishInt, mathInt])

studentList.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))


for studentInfo in studentList:
  print(studentInfo[0])