# Let's say we have some strings representing datetimes
datetime1 = '2023-01-01 23:12:13'
datetime2 = '2023-06-03 01:07:12'


print('datetime1', datetime1, 'type(datetime1)', datetime1)
print('datetime2', datetime2, 'type(datetime2)', datetime2)


# First, let's convert them to python's datetime type 
from datetime import datetime 
parsed_datetime1 = datetime.strptime(datetime1, '%Y-%m-%d %H:%M:%S')
parsed_datetime2 = datetime.strptime(datetime2, '%Y-%m-%d %H:%M:%S')
print('\nparsed_datetime1', parsed_datetime1, 'type(parsed_datetime1)', type(parsed_datetime1))
print('parsed_datetime2', parsed_datetime2, 'type(parsed_datetime2)', type(parsed_datetime2))

# Now, let's calculate the time elapsed. The type of this value will be datetime.timedelta
time_elapsed = parsed_datetime2 - parsed_datetime1
print('\ntime_elapsed', time_elapsed, 'type(time_elapsed)', type(time_elapsed))

# Now, let's express time elapsed in seconds 
seconds_elapsed = time_elapsed.total_seconds()
print('\nseconds_elapsed', seconds_elapsed, 'type(seconds_elapsed)', type(seconds_elapsed))
