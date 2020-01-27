def us_print():
	a=input('Введите первое число: ')
	while (not a.isdigit()) or (not int(a)>=1) :
		a=input('Допустимы только натуральные числа!\nВведите число еще раз: ')
	b=input('Введите второе число: ')
	while not b.isdigit() or int(b)<=0:
		b=input('Допустимы только натуральные числа!\nВведите число еще раз: ')
	sum_of_natural_numbers(a,b)
def sum_of_natural_numbers(a,b):
	sum=0
	a=int(a)
	b=int(b)
	if a <= b:
		for i in range(a,b+1):
			sum+=i
		print('Сумма натуральных чисел от', a,'до', b, 'равна', sum)
		answer()
	else:
		for i in range(b,a+1):
			sum+=i
		print('Сумма натуральных чисел от', b,'до', a, 'равна', sum)
		answer()
def answer():
	ans=input('Повторить заново (y/Y/Д/д) или выйти (n/N/Н/н) из программы? ')
	if ans == 'y' or ans == 'Y' or ans == 'Д' or ans == 'д':
		us_print()
	elif ans == 'n'or ans == 'N' or ans == 'Н' or ans == 'н':
		exit(0)
us_print()
