import datetime 
birthday = input('Введите свою дату рождения dd.mm.yyyy ')
print(f'Вы ввели: {birthday}')
day, month, year = birthday.split('.')
age_days = datetime.date.today()- datetime.date(int(year), int(month), int(day))
print(f'Число дней с вашего рождения: {age_days}')
#round_days = int(input("введите красивое число дней: "))
round_days = datetime.timedelta(days=int(input("введите красивое число дней: ")))
age_days_round = datetime.date(int(year), int(month), int(day)) + round_days
print(f"ваш юбилейный день {age_days_round}")