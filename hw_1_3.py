num1= input('Напиши число: ')
print('Целое число - ', int(num1))
print('Комлпексное число - ', complex(num1))
print('Логическое значение числа - ', bool(num1))
print('Твое число как строка - ', str(num1))
num2= input('Напиши еще число: ')
print('Целое число * - ', int(num1)*int(num2))
print('Комлпексное число * - ', complex(num1)*complex(num2))
print('Логическое значение чисел * - ', bool(num1)*bool(num2))
print('int + float ', int(num1)+float(num2))
print(' int*complex ', int(num1)*complex(num2))
print(' int*float ', int(num1)*float(num2))
print(' float*complex ', float(num1)*complex(num2))
print(' str+str ', str(num1)+str(num2))

