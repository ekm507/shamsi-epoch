import time

epoch_float = time.time()
epoch = int(epoch_float)
epoch_local = epoch + 3 * 60 * 60 + 30 * 60
epoch = epoch_local
# epoch = 45*86400

seconds_in_minute = 60
minutes_in_hour = 60
hours_in_day = 24
seconds_in_hour = seconds_in_minute * minutes_in_hour
seconds_in_day = seconds_in_hour * hours_in_day

seconds_in_astronomical_year = 31557600
seconds_in_calendar_year = seconds_in_day * 365

days_epoch = epoch // seconds_in_day
years_epoch = epoch // seconds_in_calendar_year

# when epoch is 0, date is: 1348-10-11
first_unix_year = 1348
first_unix_month_of_year = 10
first_unix_day_of_month = 11
number_of_leapyears_passed = 7
days_in_months = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 30]

def calculate_date_from_days(days: int) -> tuple:
    days_remaining = days
    if days_remaining > 366:
        return 0
    
    months = 0
    while days_remaining > days_in_months[months]:
        days_remaining = days_remaining - days_in_months[months]
        months += 1
    return (months + 1, days_remaining)

def is_leap_year(year:int):
    leap_years_mods = [1, 5, 9, 13, 17, 21, 26, 30]
    if year % 33 in leap_years_mods:
        return True
    else:
        return False

def get_number_of_leapyears_since_1348(year:int):
    # number_of_leapyears_before_1348 = 1348 //
    n = 0
    for y in range(1348, year + 1):
        if is_leap_year(y):
            n += 1
    return n

year_now = first_unix_year + years_epoch
seconds_remaining_in_year = epoch % seconds_in_calendar_year

# add 321 days to convert 1348-10-11 into 1349-00-00
days_from_unixyear_to_1349 = 78

# days_remaining_in_year = seconds_remaining_in_year // seconds_in_day
days_epoch_from_1349 = days_epoch - days_from_unixyear_to_1349
# days_remaining_in_year = days_epoch % 365 - get_number_of_leapyears_since_1348(year_now)
days_passed_in_year = (days_epoch_from_1349 - get_number_of_leapyears_since_1348(year_now)) % 365


if is_leap_year(year_now):
    days_in_this_year = 366
else:
    days_in_this_year = 365


if days_passed_in_year >= days_in_this_year:
    days_passed_in_year -= days_in_this_year
    year_now += 1

seconds_in_today = epoch % seconds_in_day
hour = seconds_in_today // seconds_in_hour
minute = (seconds_in_today % seconds_in_hour) // seconds_in_minute
seconds = (seconds_in_today % seconds_in_hour % seconds_in_minute)


print(year_now, calculate_date_from_days(days_passed_in_year))

print(epoch, days_epoch, year_now, days_passed_in_year)
print(f'{hour}:{minute}:{seconds}')
print(get_number_of_leapyears_since_1348(1402))