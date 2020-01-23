#1__________________________________________________________
def compound_interest():
  principal_amount = int(input("Insert the amount investing: "))
  nom_interest = float(input("Insert the interest rate: "))
  y = int(input("Times compounded per year: "))
  t = int(input("How many years?: "))
  tmp = (nom_interest) + 1
  final_capital = (principal_amount * (tmp**y))
  print("Final capital: " + str(final_capital))

compound_interest()


#2__________________________________________________________
def triangular_num():
  n = int(input("Insert nth triangular number you wanna see: "))
  for i in range(1,n+1):
    triangular_num = round(i*(i+1)/2)
    print(str(i) + "\t" + str(triangular_num))
triangular_num()


#3_________________________________________________________
lst = [5, 6, 8, 12, 17, 99, 104]
def even_dig_counter(lst):
  cnt = 0
  for i in lst:
    if i % 2 == 0:
      cnt += 1
  return cnt
even_dig_counter(lst)


#4_________________________________________________________
numbers = [2, 3, 4]
def square_sum(lst):
  res = 0
  for i in lst:
    res += i**2
  print(res)
square_sum(numbers)


#5_______________________________________________________
def factorial():
  n = -1
  while(n < 0 or type(n)!=int):
    n = int(input("Insert an integer: "))
    if (n<0 or type(n)!=int):
      print("Error! Try again!")
  print(fac(n))
def fac(n):
  if n == 0:
    return 1
  elif n == 1:
    return n
  else:
    return n * fac(n-1)
factorial()


#6_______________________________________________________
def gradeConverter():
  n=-1
  while(n<0 or n>100):
    n = int(input("Insert the grade: "))
    if (n<0 or n>100):
      print("Error! Try again!")
  if n > 89:
    print('A')
  elif n > 79:
    print('B')
  elif n > 69:
    print('C')
  elif n > 59:
    print('D')
  else:
    print('F')
gradeConverter()


#7______________________________________________________
def dayConverter():
  n=-1
  days = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
  while(n<1 or n>7):
    n = int(input("Insert a day number: "))
    if (n<1 or n>7):
      print("Error! Try again!")
  print(days[n])
dayConverter()


#8_____________________________________________________
def digitCounter():
  digits_n = 1
  n=-1
  while(n<0):
    n = int(input("Insert a positive number: "))
  while (n > 9):
    n //= 10
    digits_n += 1
  print("Number of digits: " + str(digits_n))
digitCounter()


#9_____________________________________________________
def is_prime():
  n=-1
  while(n<0):
    n = int(input("Insert a positive number: "))
  if n == 1:
    return False
  for i in range(2,round(n/2)):
    if n%i == 0:
      return False
  return True
is_prime()
