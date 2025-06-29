from Obtenedor_entrada import Obtenedor_entrada
from Procesador import Procesador_Entrada

if __name__ == "__main__":
    
    entrada=Obtenedor_entrada()
    procesador= Procesador_Entrada()
    procesador.procesar_entrada(entrada.getEntrada())


