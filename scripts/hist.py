import os
from tqdm import tqdm
import matplotlib.pyplot as plt
def hacer_histograma(longitudes):
    plt.hist(longitudes, bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Longitud del párrafo')
    plt.ylabel('Frecuencia (escala logarítmica)')
    plt.yscale('log')  # Usar escala logarítmica en el eje y
    plt.title('Longitudes de Abstracts')
    
    # Ajustar límites del eje x para empezar desde 0
    plt.xlim(left=0)
    
    # Agregar una etiqueta personalizada en el eje x en el valor 8192
    plt.text(8192, plt.gca().get_ylim()[1]*0.7, 'gemma-2b', color='red', ha='center')
    
    # Agregar una línea vertical roja en la posición de la etiqueta gemma
    plt.axvline(x=8192, color='red', linestyle='--')
    
    plt.show()


def contar_caracteres_parrafos_pares(documento):
    # Dividir el documento en párrafos
    parrafos = documento.split('\n')
    
    # Seleccionar los párrafos pares
    parrafos_pares = parrafos[1::2]  # Seleccionar desde el segundo párrafo hasta el final, de dos en dos
    
    # Inicializar la barra de progreso
    barra_progreso = tqdm(total=len(parrafos_pares), desc='Contando caracteres de párrafos pares')
    
    # Contar el número de caracteres de cada párrafo
    longitudes = []
    for parrafo in parrafos_pares:
        longitudes.append(len(parrafo))
        barra_progreso.update(1)  # Actualizar la barra de progreso
    barra_progreso.close()  # Cerrar la barra de progreso
    
    return longitudes

# Directorio donde se encuentra el archivo
directorio = '../dataset'

# Nombre del archivo
nombre_archivo = '5000000.txt'

# Abrir el documento
ruta_completa = os.path.join(directorio, nombre_archivo)
with open(ruta_completa, 'r', encoding='utf-8') as archivo:
    documento = archivo.read()

# Contar caracteres y hacer histograma como antes
longitudes = contar_caracteres_parrafos_pares(documento)
hacer_histograma(longitudes)
