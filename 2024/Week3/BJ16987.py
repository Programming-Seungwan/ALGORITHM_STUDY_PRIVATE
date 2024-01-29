from sys import stdin as s
s = open('./input.txt', 'rt')

number = int(s.readline().strip())
eggList = [list(map(int, s.readline().strip().split())) for _ in range(number)]

print(eggList)