heelooooooo
print('Today is 10.01.2020')
name_surname = input('Please, write your name and surname: ')
print('='*20)
print('Hello,', name_surname) 

day_of_birth = int(input('Please, tell me the day of your birthday: '))
month_of_birth = int(input('And month is: '))
year_of_birth = int(input('At which year you was born? '))

if (month_of_birth > 1) and (day_of_birth > 10):
	years = 2020 - year_of_birth - 1
	months = (years*12) +12 - month_of_birth
	days =  months*30 - day_of_birth + 40
elif (month_of_birth > 1) and (day_of_birth < 10):
	years = 2020-year_of_birth - 1
	months = years*12+ 13 - month_of_birth
	days = months*30+10-day_of_birth
elif (month_of_birth == 1) and (day_of_birth > 10):
	years = 2020 - year_of_birth - 1
	months = (years*12) + 12 - month_of_birth
	days =  months*30 + 40 - day_of_birth
elif (month_of_birth == 1) and (day_of_birth < 10):
        years = 2020 - year_of_birth
        months = (years*12)
        days =  months*30 + 10 - day_of_birth

print('-'*20)
print('Wow!', name_surname, 'you have', years, 'years old')
print('And you are living here for', months, 'months and', days, 'days!')

