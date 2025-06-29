from Sonidos import Emitir_Sonido
from Diccionario import Diccionario
import time

class Procesador_Entrada:
    def procesar_entrada(self, entrada):
        miDiccionario = Diccionario()
        sonido = Emitir_Sonido()

        # Crear una lista de sonidos para la palabra
        lista_de_sonidos = []

        for i in entrada.upper():
            if i == " ":
                time.sleep(1)  # Pausa larga entre palabras
                continue

            clavemorse = miDiccionario.getMorse(i)  # Obtiene el código morse de la letra
            print(i, ' ' + clavemorse)

            # Agregar los sonidos de la letra a la lista
            for simbolo in clavemorse:
                if simbolo == '.':
                    lista_de_sonidos.append(sonido.Sonido_corto)  # Añade el sonido corto
                else:
                    lista_de_sonidos.append(sonido.Sonido_largo)  # Añade el sonido largo

        # Reproducir todos los sonidos de la lista de manera secuencial
        for sonido_func in lista_de_sonidos:
            sonido_func()  # Ejecuta el sonido (corto o largo)
            time.sleep(0.5)  # Espera entre sonidos (ajustar según sea necesario
