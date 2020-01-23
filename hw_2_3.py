def fib():
	f1=1
	f2=1
	str1='1 1'
	print(str1) 
	a=input('скок хош? ')
	while int(a)>0:
		for i in range(0,int(float(a))):
			f3=f1+f2
			str1=str1 + ' ' + str(f3)
			f1=f2
			f2=f3
		print(str1)
		a=input('скок хош? ')
fib()
