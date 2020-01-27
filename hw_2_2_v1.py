def us_print():
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    while True:
        try:
            sum_of_natural_numbers(int(float(a)), int(float(b)))
        except ValueError:
            print('Вы ввели не правильные числа, введите еще раз!')
            us_print()
            break
def sum_of_natural_numbers(a,b):
    sum = 0
    if a <= b:
        for i in range(1,b+1):
            sum+=i
        print('Сумма натуральных чисел от', a,'до', b, 'равна', sum)
        answer()
    else:
        for i in range(1,a+1):
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
