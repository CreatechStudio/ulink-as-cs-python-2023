total_years = 90
total_days = total_years * 365.25

your_years = int(input('How old are you? '))
your_days = your_years * 365.25

remain_years = total_years - your_years
remain_days = int(total_days - your_days)
remain_weeks = round(remain_days / 7)
remain_months = remain_years * 12

print(f'You have \033[2m{remain_days}\033[0m days, \033[2m{remain_weeks}\033[0m weeks and \033[2m{remain_months}\033[0m months left.')

