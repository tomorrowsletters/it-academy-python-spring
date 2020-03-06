# Write function that converts 24h format of time to 12h format.
def time_converter(time):
    time = time.replace(':', ' ')
    time = time.split()
    time = [int(time[0]), time[1]]
    hours = ''
    minutes = ''
    if time[0] < 12 and time[0] != 0:
        hours += str(time[0])
        minutes += str(time[1])
        return '{}:{} a.m.'.format(hours, minutes)
    else:
        if time[0] % 2 == 0 and time[0] != 12 and time[0] != 0:
            hours += str(int(time[0] - 12))
            minutes += str(time[1])
            return '{}:{} p.m.'.format(hours, minutes)
        elif time[0] == 12:
            hours += str(int(time[0]))
            minutes += str(time[1])
            return '{}:{} p.m.'.format(hours, minutes)
        elif time[0] == 0:
            hours = '12'
            minutes += str(time[1])
            return '{}:{} a.m.'.format(hours, minutes)
        else:
            hours += str(int(time[0] / 2))
            minutes += str(time[1])
            return '{}:{} p.m.'.format(hours, minutes)


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and
    # not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
