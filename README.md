calculate shamsi date from epoch seconds unix time
---

# algorithm

algorithm consists of 3 parts:

1. calculate number of days and years passed since unix date.
2. leap years: fix the numbers by calculating leap years and adding or decreasing some values from them.
3. calculate month amd day of month to get the full date.

more detailed version is this:

1. first we convert epoch to local. for Iran it will be epoch + 3:30':00"
2. we calculate number of days passed since unix time.
3. we decrement number `78` from number of days. because we want our start point to be 1349-01-01 in shamsi. but unix time starts from 1348-10-11 in shamsi.
4. we calculate number of years passed by dividing number of days by 365 which is number of days in a non-leap calendar year. we also calculate remaining days in the last year.
5. then we calculate number of leap years passed since 1349 and decrement the value from remaining days. if number gets negative, we add 365 to it and decrease number of years passed by 1.
6. finally, we calculate month and day of month from number of days passed in year.