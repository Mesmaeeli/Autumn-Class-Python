grade = [19,13,9,12,18,20]

"""for sub in grade:
   if sub < 10:
      print('failed')
      break
   print(sub, 'passed')

else:
   print('done')
"""
"""
index = 0
while index < len(grade):
   if grade[index] < 10:
      print('failed')
      index += 1
      continue 
   print(grade[index],'passed')
   index += 1

else:
   print('done')


if 10 > 0:
   pass
"""
"""
def func(Num):
	if Num == 1:
		return 1
	else:
		return Num * func(Num -1)
"""
"""
Num1 = int(input('adad aval ro vared konid: '))
Num2 = int(input('adad dovvom ro vared konid: '))
try:
   print(Num1 /Num2)
   print(Num3)
except(AssertionError):
   d = input
except(NameError):
   print('moteghayer nashenakhte')
"""
def julian_date(d,m,y):
   months = [31,28,31,30,31,30,31,31,30,31,30,31]
   result = 0
   try:
      assert d < 31
   except:
      d = int(input('ruz kamtar az 31 bashad'))
      
           
