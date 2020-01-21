print('Today is 10.01.2020')
name_surname = input('Please, write your name and surname: ')
print('='*20)
print('Hello,', name_surname) 

day_of_birth = int(input('Please, tell me the day of your birthday: '))
month_of_birth = int(input('And month is: '))
year_of_birth = int(input('At which year you was born? '))

i1 = int((month_of_birth - 14) / 12)
jd = day_of_birth - 32075
jd += int((1461 * (year_of_birth + 4800 + i1)) / 4)
jd += int((367 * (month_of_birth - 2 - (12 * i1))) / 12)
jd -= int((3 * int((year_of_birth + 4900 + i1) / 100)) / 4)
i = int((1 - 14) / 12)
jd1 = 10 - 32075
jd1 += int((1461 * (2020 + 4800 + i)) / 4)
jd1 += int((367 * (1 - 2 - (12 * i))) / 12)
jd1 -= int((3 * int((2020 + 4900 + i) / 100)) / 4)
days=jd1-jd
years=days//360
months=days//30
print('-'*20)
print('Wow!', name_surname, 'you have', years, 'years old')
print('And you are living here for', months, 'months and', days, 'days!')

