import os
from tqdm import tqdm
import matplotlib.pyplot as plt

def hacer_histograma(longitudes):
    plt.hist(longitudes, bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Número de palabras en abstracts')
    plt.ylabel('Frecuencia (escala logarítmica)')
    plt.yscale('log')  # Usar escala logarítmica en el eje y
    plt.title('Número de palabras por abstract')

    # Ajustar límites del eje x para empezar desde 0
    plt.xlim(left=0)

    plt.text(8192, plt.gca().get_ylim()[1]*0.7, 'gemma-2b', color='red', ha='center')
        
    # Agregar una línea vertical roja en la posición del límite de palabras
    plt.axvline(x=8192, color='red', linestyle='--')
    
    plt.show()

def contar_palabras_parrafos_pares(documento):
    # Dividir el documento en párrafos
    parrafos = documento.split('\n')
    
    # Seleccionar los párrafos pares
    parrafos_pares = parrafos[1::2]  # Seleccionar desde el segundo párrafo hasta el final, de dos en dos
    
    # Inicializar la barra de progreso
    barra_progreso = tqdm(total=len(parrafos_pares), desc='Contando palabras de párrafos pares')
    
    # Contar el número de palabras de cada párrafo
    num_palabras = []
    for parrafo in parrafos_pares:
        palabras = parrafo.split()  # Dividir el párrafo en palabras
        num_palabras.append(len(palabras))  # Contar el número de palabras y añadirlo a la lista
        barra_progreso.update(1)  # Actualizar la barra de progreso
    barra_progreso.close()  # Cerrar la barra de progreso
    
    return num_palabras

# Directorio donde se encuentra el archivo
directorio = '../dataset'

# Nombre del archivo
nombre_archivo = '1000000.txt'

# Abrir el documento
ruta_completa = os.path.join(directorio, nombre_archivo)
with open(ruta_completa, 'r', encoding='utf-8') as archivo:
    documento = archivo.read()

# Contar palabras y hacer histograma como antes
num_palabras = contar_palabras_parrafos_pares(documento)
hacer_histograma(num_palabras)

