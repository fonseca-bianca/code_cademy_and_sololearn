from datetime import datetime
now = datetime.now()

print ('%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))

bool_two = not 3**4 < 4**3