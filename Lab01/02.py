s1 = int(input("Enter your exercise time 1: "))
s2 = int(input("Enter your exercise time 2: "))
s = s1+s2
h = s // 3600
s = s % 3600
m = s // 60
s = s % 60
print(f'It is {h} hours {m} minutes and {s} seconds.')