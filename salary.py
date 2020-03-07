salary = int(input('what is your salary? '))
if salary >= 2000:
    tax = salary * 27/100
    net = salary - tax
else:
    tax = salary * 17/100
    net = salary - tax
print('Your Tax is: ', tax)
print('Your Net salary is: ', net)
