amount_due = 50
while amount_due > 0 :
 print(f'Нужная сумма: {amount_due}')
 coin = input("Вставьте монету: ")
 amount_due -=int(coin)
print(f'Ваша сдача: {amount_due}')
