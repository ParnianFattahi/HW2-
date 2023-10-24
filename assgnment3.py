import math

op=input('enter op(+,-,*,/sin,cos,tan,cot,factorial,sqrt) : ')

sin=math.sin
cos=math.cos
tan=math.tan
fac=math.factorial
sqrt=math.sqrt

if op=='sin':
  a=float(input('enter number1 : '))
  r=sin(a)

if op=='cos':
  a=float(input('enter number1 : '))
  r=cos(a)

if op=='tan':
  a=float(input('enter number1 : '))
  r=tan(a) 

if op=='cot':
  a=float(input('enter number1 : '))
  b=tan(a)
  r=1/b


if op=='+':
   a=float(input('enter number1 : '))
   b=float(input('enter number 2:  '))
   r=a+b

if op=='-':
   a=float(input('enter number1 : '))
   b=float(input('enter number 2:  '))
   r=a-b

if op=='/':
   a=float(input('enter number1 : '))
   b=float(input('enter number 2:  '))
if b==0:
   b=float(input('enter number 2:  '))
   r=a/b
 
if  op=='*':
   a=float(input('enter number1 : '))
   b=float(input('enter number 2:  '))
   r=a*b


if op=='fac':
   if a<0:
      print('error')
   r=fac(a)

if op=='sqrt':
   r=sqrt(a)

print(r)