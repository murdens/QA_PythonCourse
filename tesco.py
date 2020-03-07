Product = input('Enter which product: ')
Quantity = input('Enter quantity: ')
Price = input('Enter price: ')
Amount = int(Quantity) * float(Price)
Vat = Amount * 10/100
print('Total amount ', Amount)
print('Total VAT ', Vat)
print('Total Bill ', (Amount + Vat))
