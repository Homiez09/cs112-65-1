def read_hour():
    return int(input("Enter hour: "))

def read_minute():
    return int(input("Enter minute: "))

def read_second():
    return int(input("Enter second: "))

def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def time_elapsed(start, finish):
    total = abs(start - finish)
    hour = total//3600
    minute = (total - (hour*3600))//60
    second = total - (hour*3600) - minute*60
    return f"{hour:.0f} hours {minute:.0f} minutes {second:.0f} seconds."

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))