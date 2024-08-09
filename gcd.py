def gcd(a,b):
	while b !=0:
		a,b=b, a%b
	return a
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

result=gcd(num1,num2)
print(f"the gcd of {num1} and {num2} is {result}")

----------------------------------
OUTPUT:
mlm@mlm-H81:~/Desktop/dsml$ python3 gcd.py
enter the first number:10
enter the second number:50
the gcd of 10 and 50 is 10
