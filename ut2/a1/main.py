import sys

money = int(sys.argv[1])

print('Entrada:', money, 'Salida: ')

print()

if money >= 50:
    bill50 = money//50
    money = money%50
    print('￮ Billete(s) de 50: ', bill50)
if money >= 20:
    bill20 = money//20
    money = money%20
    print('￮ Billete(s) de 20: ', bill20)
if money >= 10:
    bill10 = money//10
    money = money%10
    print('￮ Billete(s) de 10: ', bill10)
if money >= 2:
    coin2 = money//2
    money = money%2
    print('￮ moneda(s) de 2: ', coin2)
if money >= 50:
    coin1 = money//50
    money = money%50
    print('￮ modena(s) de 50: ', coin1)
print()
