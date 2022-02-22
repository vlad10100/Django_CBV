def add_time(start, duration, day=None):

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day is not None:
        day = day.lower()

    time_start, indicator = start.split(' ')
    hours_start, minutes_start = time_start.split(':')

    hours_duration, minutes_duration = duration.split(':')

    total_hours = int(hours_start) + int(hours_duration)
    total_minutes = int(minutes_start) + int(minutes_duration)

    count_minutes = 0
    day_counter = 0
    day_change = ''

    while total_minutes > 59:
        total_minutes = int(total_minutes - 60)
        count_minutes += 1

    if len(str(total_minutes)) < 2:
        total_minutes = '0' + str(total_minutes)

    total_hours += count_minutes

    while total_hours >= 12:
        day_counter += 1
        total_hours = abs(int(total_hours - 12))
        if indicator in "PM":
            indicator = "AM"
        else:
            indicator = "PM"
    day_counter /= 2

    if day_counter != 0:
        if day is None:
            if indicator in "AM":
                day_change = ' (next day)'

        if day_counter > 1:
            day_counter += 1
            day_counter = str(round(day_counter))
            day_change = ' (' + day_counter + ' days later)'

    if total_hours == 0:
        total_hours += 12

    if day in days:
        pos = days.index(day)
        day_identifier = round((int(day_counter) + pos) % 7)
        date = days[day_identifier]
        date = date.title()
        date = ', ' + str(date)
        if int(day_counter) == 1:
            day_change = ' (next day)'
    else:
        date = ''

    play = str(total_hours) + ':' + str(total_minutes) + ' ' + indicator + date + day_change
    return play
