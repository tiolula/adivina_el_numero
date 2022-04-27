import juego

def main():
    jugar_una_vez_mas = 's'

    while jugar_una_vez_mas == 's':

        juego.eligir_numero_secreto()

        print('\n adivina el numero secreto!')
        
        intentos = 1

        while juego.intentar_adivinar(input('\n intente adivinar: ')) !=  'Ok':
            intentos = intentos + 1
            print('\n no! intenta una vez más!')

        print('en buena hora!')
        print('\n acertastes en ' + str(intentos) + ' intentos')

        jugar_una_vez_mas = input('\n tipea la letra s y apreta enter para jugar una vez más: ') 

if __name__ == "__main__":
    main()