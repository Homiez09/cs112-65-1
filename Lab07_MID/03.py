day = int(input())
hour = int(input())
minute = int(input())

text = ""
if (hour >= 22 and minute > 0) or (hour == 4 and hour == 0):
    text += "good-night-"
elif (hour >= 18 and minute > 0) or (hour == 22 and minute == 0):
    text += "good-evening-"
elif (hour >= 12 and minute > 0) or (hour == 18 and minute == 0):
    text += "good-afternoon-"
elif (hour >= 4 and minute > 0) or (hour == 12 and minute == 0):
    text += "good-morning-"
else: 
    text += "good-night-"

if day == 1:
    text += "sunday.png"
elif day == 2:
    text += "monday.png"
elif day == 3:
    text += "tuesday.png"
elif day == 4:
    text += "wednesday.png"
elif day == 5:
    text += "thursday.png"
elif day == 6:
    text += "friday.png"
elif day == 7:
    text += "saturday.png"
    
print(text)