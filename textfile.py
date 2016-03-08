def leelineas(filename):
    count = 0
    lineas = []

    try:
        fh = open(filename, "r")
        for line in fh:
            lineas.append(line.strip())
            count = count + 1
        print ("leidas ", count," lineas")
        return lineas
    except:
        print("No es posible leer el fichero: ", filename)

def leefichero(filename):
    count = 0
    txt = " "
    try:
        fh = open(filename, "r")
        texto = fh.read()
        return texto
    except:
        print("No es posible leer el fichero: ", filename)


def escribe(filename, linea):
    try:        
        f = open(filename, "w", encoding="utf-8")
        f.write(linea)
        f.close
    except:
        print("No es posible escribir el fichero: ", filename)

