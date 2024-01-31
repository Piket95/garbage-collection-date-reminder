import icalendar
from icalendar import Calendar
from datetime import datetime
import os

# def print_hi(name):
#     print(f'Hi, {name}')


if __name__ == '__main__':
    # print_hi('PyCharm')

    # init the calendar
    cal = Calendar()

    # configuration
    cal.add('version', '2.0')

    # open file
    file = open('./data/Abfuhrtermine.ics', 'rb')
    filecal = icalendar.Calendar.from_ical(file.read())

    for event in filecal.walk('vevent'):
        print('Desc: ', event.get('description'))
        print('Start: ', event.decoded('dtstart'))
        print('End: ', event.decoded('dtend'))

    file.close()

# TODO:
#  - process only events in the future
#  - show windows notification one day before the event
#       - show description, which trash and custom text like tomorrow or in two days for example
#  - make a test ical for testing (generated every time i run this script with dates for tomorrow, in two days and 2 or 3 further in the future?!)