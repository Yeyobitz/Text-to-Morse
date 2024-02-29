# Este programa traducirá epañol a morse 
# Autor: Diego "Yeyo" Quiñones Montecinos

# Importamos las librerías necesarias
import winsound
import time
from tkinter import *

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

# Función para traducir el texto
def traducir_a_morse(user_string):
    morse_string = ""
    for char in user_string:
        if char.upper() in español_a_morse:
            morse_string += español_a_morse[char.upper()] + " "
        else:
            morse_string += char + " "
    return morse_string.strip()

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

# Creamos una interfaz para que el usuario pueda interactuar con el programa
# Creamos la ventana
ventana = Tk()
ventana.title("Traductor de Español a Morse")

def traducir():
    texto = entrada_usuario.get("1.0", "end-1c")  # Obtiene el texto del usuario
    morse = traducir_a_morse(texto)  # Utiliza tu función existente
    salida_morse.delete("1.0", "end")  # Limpia el área de salida
    salida_morse.insert("end", morse)  # Muestra el Morse en el área de salida

# Función para reproducir el Morse como sonido
def reproducir_sonido():
    morse = salida_morse.get("1.0", "end-1c")  # Obtiene el Morse del área de salida
    morse_a_sonido(morse)  # Utiliza tu función existente

ventana = Tk()
ventana.title("Yeyo's Español a Morse")

# Etiqueta de entrada
etiqueta_entrada = Label(ventana, text="Ingrese su texto aquí:")
etiqueta_entrada.pack()

# Campo de entrada del usuario
entrada_usuario = Text(ventana, height=5, width=50)
entrada_usuario.pack()

# Botón de traducción
boton_traducir = Button(ventana, text="Traducir a Morse", command=traducir)
boton_traducir.pack()

# Área de salida para el Morse
salida_morse = Text(ventana, height=5, width=50)
salida_morse.pack()

# Botón de reproducción de sonido
boton_sonido = Button(ventana, text="Reproducir Sonido", command=reproducir_sonido)
boton_sonido.pack()

ventana.mainloop()
