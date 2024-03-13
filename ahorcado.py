from random import choice

palabras=['panadero','dinosaurio','helipuerto','tiburon']
vidas=6
letras_correctas=[]
letras_incorrectas=[]
aciertos=0
juego_terminado=False

def elegir_palabra(lista_palabra):
    palabras_elegida=choice(lista_palabra)
    letras_unicas= len(set(palabras_elegida))

    return palabras_elegida,letras_unicas


def pedir_letra():
    letra_elegida=''
    es_valida=False
    abecedario='abcdefghijklmnopqrstuvwxyz'

    while not es_valida:
        letra_elegida=input('Elige una letra:').lower()
        if letra_elegida in abecedario and len(letra_elegida)==1:
            es_valida=True
        else:
            print('No has elegido una letra correcta')

    return letra_elegida

def motrar_nuevo_tablero(palabra_elegida):

    lista_oculta=[]

    for letra in palabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida,palabra_oculta,vidas,coincidencias):
    fin=False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print('Ya has elegido esa letra intenta con otra')
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas==0:
        fin=perder()
    elif coincidencias==letras_unicas:
        fin=ganar(palabra_oculta)

    return vidas,fin,coincidencias

def perder():
    print('Te has quedado sin vidas')
    print('La palabra oculta era '+palabra)

    return True

def ganar(palabra_descubierta):
    motrar_nuevo_tablero(palabra_descubierta)
    print("Felicidades has encontrado la palabra")
    return True

palabra,letras_unicas=elegir_palabra(palabras)

while not juego_terminado:
    print('\n'+'*'*20+'\n')
    motrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: '+ '-'.join(letras_incorrectas))
    print(f'Vidas:{vidas}')
    print('\n' + '*' * 20 + '\n')
    letra=pedir_letra()

    intentos,terminado,aciertos=chequear_letra(letra,palabra,vidas,aciertos)
    juego_terminado=terminado