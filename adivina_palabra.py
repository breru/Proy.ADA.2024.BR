from random import choice

def elegir_palabra(lista_palabras):
    palabra_aleatoria = choice(lista_palabras)
    print(palabra_aleatoria)
    return palabra_aleatoria.upper()

def pedir_letra():
    letra_seleccionada = input("Elige una letra: ")
    if not letra_seleccionada.isalpha() or len(letra_seleccionada) != 1:
        print("Por favor, ingresa una letra válida.")
        return pedir_letra()
    else:
        letra_seleccionada = letra_seleccionada.upper()
        return letra_seleccionada
def valida_letra(letra_seleccionada, vidas, aciertos):
    if letra_seleccionada in letra_a_adivinar:
        aciertos += 1

        if aciertos == len(letra_a_adivinar): 
            print("Ganaste")
    else:
        print("Esa letra no se encuentra en la palabra")
        if letra_seleccionada in letras_incorrectas:
            print("Esa letra ya fue elegida y no se encuentra en la palabra")
            return vidas, aciertos
        
        letras_incorrectas.append(letra_seleccionada)
        print(letras_incorrectas)
        vidas = vidas - 1 
# validar si quedan vidas restantes
        print(f"Te quedan {vidas} vidas")
    return vidas, aciertos
        


lista_palabra_oculta = ["almohada" , "guitarra" , "monitor" , "mate" , "espejo" , "tambor" , "telefono" , "sol" , "frambuesa" , "mochila" , "casa" , "ladrillo"]

palabra_oculta = elegir_palabra(lista_palabra_oculta)

vidas = 2
aciertos = 0

letras_incorrectas = []

print("*~*~*~*~*~*~*~*~*~*~*~*")

print("Bienvenidx al Juego.")

print("*~*~*~*~*~*~*~*~*~*~*~*")

print("Deberás adivinar la palabra oculta. \n\n Comencemos")

letra_a_adivinar = set(palabra_oculta)

#lista_incorrectas []
#if letra_seleccionada (no está):
#   lista_incorrectas.append(letra_seleccionada)

#if letra_seleccionada in lista_incorrectas:
#   print("Esa letra ya fue elegida y no se encuentra en la palabra")
#(no tiene que restar vida)

while vidas >=1 and aciertos < len(letra_a_adivinar):
    letra_ingresada = pedir_letra()

    vidas, aciertos = valida_letra(letra_ingresada, vidas, aciertos)

    

