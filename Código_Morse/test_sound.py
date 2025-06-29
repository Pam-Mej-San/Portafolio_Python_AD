import pygame
import time

# Inicializa pygame
pygame.mixer.init()

# Asegúrate de que la ruta al archivo de sonido es correcta
sound_path = '/Users/pam/Desktop/Python_Portafolio/Código_Morse/audio/short-wav.wav'

try:
    pygame.mixer.music.load(sound_path)
    print(f"El archivo de sonido {sound_path} ha sido cargado correctamente.")
except pygame.error as e:
    print(f"No se pudo cargar el archivo de sonido. Error: {e}")
    exit()

# Reproducir el sonido
pygame.mixer.music.play()

# Crear un objeto Clock de pygame para controlar el tiempo
clock = pygame.time.Clock()

# Esperar hasta que termine la reproducción del sonido
while pygame.mixer.music.get_busy():  # Mientras el sonido esté en reproducción
    clock.tick(10)  # Mantiene el proceso corriendo hasta que termine de sonar

print("El sonido se ha reproducido correctamente.")