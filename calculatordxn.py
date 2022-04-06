def calculator():
   print('Calculator1.0 written in Python, © CC-BY-SA 4.0')
   no1 = int(input('First number: '))
   operation = input('''
   Add math operation
   + for addition
   - for subtraction  
   * for multiplication
   / for division.
   enter:  ''')
   no2 = int(input('Second number: '))
  
 
   if operation == '+':
      print(  no1 + no2)
   elif operation == '-':    
      print(  no1 - no2)
   elif operation == '*':   
      print(  no1 * no2)
      
   elif operation == '/':    
      print(  no1 / no2)
      
   		
calculator()
def calcagain():
	tryagain = input('Calculate again? (y/n case sensitive)) ')
	if tryagain == 'y':
		calculator()
	elif tryagain == 'Y':
		calculator()
	elif tryagain == 'n':
		print('Thank you for using this calculator! ')
   

calcagain()
calculator()
calcagain()
calculator()
calcagain()
calculator()
calcagain()
calculator()