# This python file is to get the start and end timeframe of the last 30 days.
# The start time is from first date of last month at 00:00:00 o'clock to first date of current month at 00:00:00 o'clock.
# For instance, today is 07.12.2025, the timeframe of last 30 days is from '2025-11-01T00:00:00.000Z' to '2025-12-01T00:00:00.000Z'
# There is special case as if this month is Jan such as 13.01.2025, the timeframe of last 30 days is from '2024-12-01T00:00:00.000Z' to '2025-01-01T00:00:00.000Z'

from datetime import datetime

# Get today datetime information
today = datetime.now()
# Extract the month value from today 
this_month = today.month

# '1' means 'Jan', '2' means 'Feb' ... '12' means 'Dec'
month_start_end_time = {
    1:
        {
            'start': '01-01T00:00:00.000Z',
            'end': '02-01T00:00:00.000Z'
    },
    2:
        {
            'start': '02-01T00:00:00.000Z',
            'end': '03-01T00:00:00.000Z'
    },
    3:
        {
            'start': '03-01T00:00:00.000Z',
            'end': '04-01T00:00:00.000Z'
        },
    4:
        {
            'start': '04-01T00:00:00.000Z',
            'end': '05-01T00:00:00.000Z'
        },
    5:
        {
            'start': '05-01T00:00:00.000Z',
            'end': '06-01T00:00:00.000Z'
        },
    6:
        {
            'start': '06-01T00:00:00.000Z',
            'end': '07-01T00:00:00.000Z'
        },
    7:
        {
            'start': '07-01T00:00:00.000Z',
            'end': '08-01T00:00:00.000Z'
        },
    8:
        {
            'start': '08-01T00:00:00.000Z',
            'end': '09-01T00:00:00.000Z'
        },
    9:
        {
            'start': '09-01T00:00:00.000Z',
            'end': '10-01T00:00:00.000Z'
        },
    10:
        {
            'start': '10-01T00:00:00.000Z',
            'end': '11-01T00:00:00.000Z'
        },
    11:
        {
            'start': '11-01T00:00:00.000Z',
            'end': '12-01T00:00:00.000Z'
        },
    12:
        {
            'start': '12-01T00:00:00.000Z',
            'end': '01-01T00:00:00.000Z'
    }
}
# Example: if this month is Jan 2025 (01.2025), the start time is '2024-12-01T00:00:00.000Z', and end time is '2025-01-01T00:00:00.000Z'
#

def get_start_time():
    if this_month == 1:
        start_time = str(today.year - 1) + '-' + month_start_end_time[12]['start']
    else:
        start_time = str(today.year) + '-' + month_start_end_time[this_month - 1]['start']
    return start_time


def get_end_time():
    if this_month == 1:
        end_time = str(today.year) + '-' + month_start_end_time[12]['end']
    else:
        end_time = str(today.year) + '-' + month_start_end_time[this_month - 1]['end']
    return end_time


def get_last_month():
    if this_month == 1:
        last_month = '12' + '.' + str(today.year - 1)
    elif this_month < 11:
        last_month = '0' + str(today.month - 1) + '.' + str(today.year)
    else:
        last_month = str(today.month - 1) + '.' + str(today.year)
    return last_month
