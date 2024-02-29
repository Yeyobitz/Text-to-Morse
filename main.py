# Este programa lo que hará será traducir epañol a morse y viceversa
# Autor: Diego "Yeyo" Quiñones Montecinos

# Diccionario de traducción
español_a_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    'Á': '.--.-', 'É': '..-..', 'Í': '..', 'Ó': '---.', 'Ú': '..--', 'Ñ': '--.--',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', '¿': '..-.-', '¡': '--...-', ' ': '/'
}

# Conseguimos el input del usuario
user_string = input("Ingrese el texto que desea traducir: ")

# Función para traducir el texto
def traducir(user_string):
    morse_string = ""
    for char in user_string:
        if char.upper() in español_a_morse:
            morse_string += español_a_morse[char.upper()] + " "
        else:
            morse_string += char + " "
    return morse_string.strip()

# importamos la librería de sonido
import winsound
import time

# función para convertir el morse a sonidos
def morse_a_sonido(morse_string):
    for char in morse_string:
        if char == ".":
            winsound.Beep(800, 200)
        elif char == "-":
            winsound.Beep(800, 600)
        elif char == " ":
            time.sleep(0.5)
        else:
            pass

# Imprimimos el resultado
print(traducir(user_string))
morse_a_sonido(traducir(user_string))

