Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("MENU".center(60,"*"))
****************************MENU****************************
>>> print(format("menu",'*=60'))
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(format("menu",'*=60'))
ValueError: '=' alignment not allowed in string format specifier
>>> print(format("menu",'*^60'))
****************************menu****************************
>>> y=12.767827
>>> print(format(y,'.2f'))
12.77
>>> #write program to print no of days in a month
>>> m=eval(input("enter month number")
       if (m=1,3,5,7,8,11,12):
