practice_score = [int(i) for i in input().split()]
min_percent = [float(i) for i in input().split()]
practice_precent = min_percent[1]
attend_percent = min_percent[0]
n = int(input())
student = {}

for i in range(n):
    score = [int(x) for x in input().split()]
    _pass = score.count(1)
    percent = "{:.2f}".format((_pass*100) / len(score))
    student[i+1] = {
        'attend_score': float(percent),
        'practice_score': 0,
        'pass': True
    }

for i in range(n):
    score = [int(x) for x in input().split()]
    percent = "{:.2f}".format((sum(score)*100) / sum(practice_score))
    student[i+1]['practice_score'] = float(percent)

count = 0
for key, value in student.items():
    if not float(value['attend_score']) >= attend_percent and not float(value['practice_score']) >= practice_precent:
        count+=1
        student[key]['pass'] = False
print(count)
for key, value in student.items():
    if value['pass']:
        print(key, "{:.2f}".format(value['attend_score']), "{:.2f}".format(value['practice_score']))
    else:
        print(f"({key})", "{:.2f}".format(value['attend_score']), "{:.2f}".format(value['practice_score']))