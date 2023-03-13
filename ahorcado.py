import random
disenoConsola = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      💀  |
     /|\  |
     / \  |
          |
    =========''']

personaNoAhorcada = '''
    🏆
     \O/
      |
     / \  '''


misPalabras = [
    'anahuac',
    'informatica',
    'computadora',
    'teclado',
    'inteligencia',
    'artificial',
    'programacion',
    'python'
]


def imprimirAhorcado(disenoConsola, incorrectas, correctas, palabraCorrecta):
    espacios = '_' * len(palabraCorrecta)
    for i in range(len(palabraCorrecta)):
        if palabraCorrecta[i] in correctas:
            espacios = espacios[:i] + palabraCorrecta[i] + espacios[i+1:]
    adivinado = ''
    for letra in espacios:
        adivinado += letra + ' '
    print('\n🤔 Adivina: '+adivinado, end='\n\n')
    print(disenoConsola[len(incorrectas)])
    letrasIncorrectas = ''
    for letra in incorrectas:
        letrasIncorrectas += letra + ', '
    print('\n❌ Letras incorrectas (' + str(len(incorrectas)) + '): ' +
          letrasIncorrectas+'\n')


if __name__ == "__main__":
    print('Bienvenido al ahorcado Anáhuac\n')
    print('INSTRUCCIONES: \nPuedes ingresar una o más letras a la vez.\nNo se permiten números ni caracteres especiales.\n\n¡Buena suerte!')
    incorrectas = ""
    correctas = ""
    palabraCorrecta = misPalabras[random.randint(0, len(misPalabras) - 1)]
    gameOver = False
    ganados = 0
    perdidos = 0
    while True:
        imprimirAhorcado(disenoConsola, incorrectas,
                         correctas, palabraCorrecta)

        letraOFrase = ""

        while len(letraOFrase) == 0:
            print('Ingresa letra o frase:')
            letraOFrase = input()
            letraOFrase = letraOFrase.lower()

        print('\033c')

        for letra in letraOFrase:
            if letra in (incorrectas + correctas):
                if len(letraOFrase) == 1:
                    print('Ya elegiste: ' + letra)
            elif letra not in 'abcdefghijklmnopqrstuvwxyz':
                print('Elije una letra.')
            else:
                if letra in palabraCorrecta:
                    correctas = correctas + letra
                    letrasEncontradas = True
                    for i in range(len(palabraCorrecta)):
                        if palabraCorrecta[i] not in correctas:
                            letrasEncontradas = False
                            break
                    if letrasEncontradas:
                        print(personaNoAhorcada+'\n\nVictoria, encontraste la palabra: "' +
                              palabraCorrecta+'" con ' + str(len(incorrectas)) + ' fallos y ' + str(len(correctas)) + ' correctos.')
                        gameOver = True
                        ganados += 1
                else:
                    incorrectas = incorrectas + letra
                    if len(incorrectas) == len(disenoConsola) - 1:
                        imprimirAhorcado(disenoConsola, incorrectas,
                                         correctas, palabraCorrecta)
                        print('¡Lo mataste!\nTuviste ' + str(len(incorrectas)) + ' errores y ' +
                              str(len(correctas)) + ' correctas, la palabra correcta era "' + palabraCorrecta + '"')
                        gameOver = True
                        perdidos += 1

        if gameOver:
            print('\n¿Deseas jugar de nuevo? (S = si, cualquier otra tecla = no)')
            if input().lower() == 's':
                print('\033c')
                incorrectas = ""
                correctas = ""
                gameOver = False
                palabraCorrecta = misPalabras[random.randint(
                    0, len(misPalabras) - 1)]
            else:
                print('\033c')
                print('Juegos ganados: ' + str(ganados) +
                      '\nJuegos perdidos: ' + str(perdidos))
                print('\n\n¡Hasta la próxima!')
                break
