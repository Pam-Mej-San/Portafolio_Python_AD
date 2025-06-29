import pygame

class Emitir_Sonido:
    def __init__(self):
        pygame.mixer.init()  # Inicializa el mezclador de sonidos de pygame

    def Sonido_corto(self):
        # Cargar y reproducir el sonido corto
        pygame.mixer.music.load('/Users/pam/Desktop/Python_Portafolio/Código_Morse/audio/short-wav.wav')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Espera mientras se reproduce el sonido
            pygame.time.Clock().tick(10)

    def Sonido_largo(self):
        # Cargar y reproducir el sonido largo
        pygame.mixer.music.load('/Users/pam/Desktop/Python_Portafolio/Código_Morse/audio/long-wav.wav')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Espera mientras se reproduce el sonido
            pygame.time.Clock().tick(10)
