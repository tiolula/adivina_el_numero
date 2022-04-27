import adivina_el_numero

def main():
    jugar_una_vez_mas = 's'

    while jugar_una_vez_mas == 's':

        adivina_el_numero.nuevo_juego()

        print('\n adivina el numero secreto!')
        
        intentos = 1

        while adivina_el_numero.jugar(input('\n intente adivinar: ')) !=  'Ok':
            intentos = intentos + 1
            print('\n no! intenta una vez más!')

        print('en buena hora!')
        print('\n acertastes en ' + str(intentos) + ' intentos')

        jugar_una_vez_mas = input('\n tipea la letra s y apreta enter para jugar una vez más: ') 

if __name__ == "__main__":
    main()