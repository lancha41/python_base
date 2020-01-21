a=input('Введите коф a= ')
while a.isalpha() or type(int(a))!=int:
        a=input('Поддерживаються только целые числа!\nВведите еще раз а= ')
b=input('Введите коф b= ')
while b.isalpha() or type(int(b))!=int:
        b=input('Поддерживаються только целые числа!\nВведите еще раз b= ')
c=input('Введите коф c= ')
while c.isalpha() or type(int(c))!=int:
        c=input('Поддерживаються только целые числа!\nВведите еще раз c= ')
a=float(a)
b=float(b)
c=float(c)
print('='*20)
if b**2 < 4*a*c:
	p=b**2-4*a*c
	s=(p.__abs__())**(0.5)
	x1=complex((-b+s*1j)/(2*a))
	x2=complex((-b-s*1j)/(2*a))
	print('Корни вашего уравнения комплексные: \n x1=', x1,'\n x2=', x2)
else:
	disq=(b**2-4*a*c)**(0.5)
	if disq>0:
		x1=(-b+disq)/(2*a)
		x2=(-b-disq)/(2*a)
		print('Корни вашего уравнения: \n x1=', x1,'\n x2=', x2)
	elif disq == 0:
		x=(-b)/(2*a)
		print('Решением вашего уравнение есть число:',x)

