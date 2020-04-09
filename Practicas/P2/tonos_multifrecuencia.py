import numpy as np
from scipy.io import wavfile

# Creamos un diccionario con la combinación de las frecuencias para sacar el dígito
# se ha pulsado
dtmf = {(697, 1209): "1", (697, 1336): "2", (697, 1477): "3", (770, 1209): "4",
        (770, 1336): "5", (770, 1477): "6", (852, 1209): "7", (852, 1336): "8",
        (852, 1477): "9", (941, 1209): "*", (941, 1336): "0", (941, 1477): "#",
        (697, 1633): "A", (770, 1633): "B", (852, 1633): "C", (941, 1633): "D"}

# Leémos el fichero y sacamos la frecuencia y los tonos del audio
Fs, s = wavfile.read('digitos.wav')

# Necesitamos establecer la precisión puesto que de lo contrario el toma los valores
# erróneos del audio debido al ruido de fondo
precision = 0.065
duracion = len(s)/Fs

# Calculamos el desplazamiento según la duración del audio y la precisión que hemos
# tenido que establecer y nos quedamos con la parte entera (operador //)
desplaz = int(len(s)//(duracion//precision))

# Vamos a extraer los tonos. Para ello, recorremos toda la información dando saltos
# de tamaño desplaz
for i in range(0, len(s)-desplaz, desplaz):
    r = s[i:i+desplaz]

    # Calculamos las frecuencias a las que debemos calcular la transformada. Los saltos
    # se producen según el desplazamiento que hemos declarado antes. Además calculamos
    # las frecuencias para asignarlas a las teclas
    Y = np.fft.fft(r)
    frecuencias = np.fft.fftfreq(r.size, d=1/Fs)

    # Frecuencias bajas. Establecemos el mínimo y el máximo
    inicio = np.where(frecuencias > 0)[0][0]
    fin = np.where(frecuencias > 1000)[0][0]

    # Extraemos el pico según la amplitud de la onda. Ese pico se corresponde con
    # el tono de la tecla que hemos marcada
    freq = frecuencias[inicio:fin]
    amplitud = abs(Y.real[inicio:fin])

    # Cogemos el peor valor como el inicial y a partir de este buscaremos uno mejor.
    # Para ello tomamos la frecuencia con mayor amplitud
    freq_baja = freq[np.where(amplitud == max(amplitud))[0][0]]

    # Necesitamos establecer una precisión porque de lo contrario coge
    # el ruido como sonidos provocados por una tecla
    diferencia = 10
    mejor = 0

    # Buscamos la frecuencia que tenga una menor diferencia con la frecuencia ideal,
    # utilizamos diferencia como pivote para calcular el mejor tono. Cada vez que
    # encontramos uno mejor, actualizamos la diferencia
    for f in [697, 770, 852, 941]:
        if abs(freq_baja-f) < diferencia :
            diferencia = abs(freq_baja-f)
            mejor = f

    # Nos quedamos con la mejor
    freq_baja = mejor

    # Ahora buscamos la frecuencia alta, igual que hemos hecho con la baja
    inicio = np.where(frecuencias > 1000)[0][0]
    fin = np.where(frecuencias > 1700)[0][0]

    freq = frecuencias[inicio:fin]
    amplitud = abs(Y.real[inicio:fin])

    freq_alta = freq[np.where(amplitud == max(amplitud))[0][0]]

    diferencia = 10
    mejor = 0

    # Buscamos la frecuencia más alta del tono que estamos tratando
    for f in [1209, 1336, 1477, 1633] :
        if abs(freq_alta-f) < diferencia :
            diferencia = abs(freq_alta-f)
            mejor = f

    freq_alta = mejor

    # Si  no encontramos ningún tono que tenga una frecuencia alta o baja que esté
    # por debajo del umbral de precisión que hemos impuesto no lo consideramos
    # y no lo codificamos como una tecla
    if freq_baja == 0 or freq_alta == 0:
        c = ""

    # En otro caso, mostramos el carácter que se corresponde con las frecuencias
    # que hemos calculado
    elif dtmf[(freq_baja,freq_alta)] != c:
        c = dtmf[(freq_baja,freq_alta)]
        print(c, end='', flush=True)
