# Este programa traducirá texto a morse 
# Autor: Diego "Yeyo" Quiñones Montecinos

import winsound
import time
from tkinter import *

texto_a_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    'Á': '.--.-', 'É': '..-..', 'Í': '..', 'Ó': '---.', 'Ú': '..--', 'Ñ': '--.--',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', '¿': '..-.-', '¡': '--...-', ' ': '/'
}
def traducir_a_morse(user_string):
    morse_string = ""
    for char in user_string:
        if char.upper() in texto_a_morse:
            morse_string += texto_a_morse[char.upper()] + " "
        else:
            morse_string += char + " "
    return morse_string.strip()

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

def traducir():
    texto = entrada_usuario.get("1.0", "end-1c")  
    morse = traducir_a_morse(texto) 
    salida_morse.delete("1.0", "end")
    salida_morse.insert("end", morse) 

def reproducir_sonido():
    morse = salida_morse.get("1.0", "end-1c") 
    morse_a_sonido(morse) 

ventana = Tk()
ventana.title("Yeyo's texto a Morse")
ventana.geometry("500x300")

# Etiqueta de entrada
etiqueta_entrada = Label(ventana, text="texto a morse", font= 'Calibri 24 bold')
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
