import os
#   MENU PRINCIPAL  -   FUNCIÓN
def mainMenu():
    while True:
        clearScreen()
        print('\n')
        print('MÁQUINA EXPENDEDORA'.center(30, ' '))
        print('\n')
        print('CODIGO -   PRODUCTO    -   PRECIO')
        print('  A1   -   PINGÜINOS   -   $15.00')
        print('  B2   -   GANSITO     -   $10.00')
        print('  C3   -   SABRITAS    -   $12.00')
        print('  D4   -   CHOCOLATE   -   $10.00')
        print('  E5   -   DUVALIN     -   $7.00')
        print('  A6   -   GALLETAS    -   $12.00')
        print('  B7   -   REFRESCO    -   $15.00')
        print('  C8   -   PANDITAS    -   $10.00')
        print('  D9   -   MANTECADAS  -   $12.00')
        print('  E1   -   SANDWICH    -   $10.00')
        print('  A2   -   MENTAS      -   $15.00')
        print('  B3   -   MARUCHAN    -   $7.00')
        print('  S    -   SALIR')
        print('\nMonedas aceptadas: $1, $3, $6, $9')
        product = input('Ingresa el código del producto: ').upper()
        if product == 'S':
            print('Vuelva pronto :D')
            input('Presione Enter para continuar...')
            break
        validateCode(product)
#   VALIDAR CÓDIGO  -   FUNCIÓN
def validateCode(product):
    if product == 'A1' or product == 'B7' or product == 'A2':
        price = 15
        enterCoins(price)
    elif product == 'B2' or product == 'D4' or product == 'C8' or product == 'E1':
        price = 10
        enterCoins(price)
    elif product == 'C3' or product == 'A6' or product == 'D9':
        price = 12
        enterCoins(price)
    elif product == 'E5' or product == 'B3':
        price = 7
        enterCoins(price)
    else:
        print('Ingresa un codigo de producto válido.')
        input('Presione Enter para continuar...')
#   INTRODUCIR MONEDAS - FUNCIÓN - AUTÓMATA
def enterCoins(price):
    coins = []
    states = {
        'state0': 0,
        'state1': 1,
        'state2': 2,
        'state3': 3,
        'state4': 4,
        'state5': 5,
        'state6': 6,
        'state7': 7,
        'state8': 8,
        'state9': 9,
        'state10': 10,
        'state11': 11,
        'state12': 12,
        'state13': 13,
        'state14': 14,
        'state15': 15,
        'statePlus': range(15, 100)
    }
    while sum(coins) < price:
        coin = int(input('$ {} de $ {} | Ingresa una moneda ($1, $3, $6, $9) -> '.format(sum(coins), price)))
        if sum(coins) == states['state0']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state1']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state2']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state3']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state4']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state5']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state6']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state7']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state8']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state9']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state10']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state11']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state12']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state13']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state14']:
            if coin == 1:
                coins.append(1)
            elif coin == 3:
                coins.append(3)
            elif coin == 6:
                coins.append(6)
            elif coin == 9:
                coins.append(9)
            else:
                print('Ingresa una moneda válida.')
        elif sum(coins) == states['state15']:
            pass
        elif sum(coins) >= states['statePlus']:
            pass
    if sum(coins) >= price:
        clearScreen()
        print('$ {} ingresados de $ {}'.format(sum(coins), price))
        print('Orden de monedas: {}'.format(coins))
        print('Producto adquirido!')
        input('Presione Enter para continuar...')
#   LIMPIAR PANTALLA -   FUNCIÓN
def clearScreen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system('cls')
#       INICIO DEL PROGRAMA, USO DE FUNCIÓN MAIN
if __name__ == '__main__':
    mainMenu()