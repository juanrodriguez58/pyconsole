import sqlite3

# Tabla de contadores

def creaTabla():
    sqlOrder = "CREATE TABLE cicle (direccion TEXT, tipo TEXT, count1 INTEGER, count2 INTEGER)"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Tabla creada")
    except:
        return("Error al insertar el registro")


def borraTabla():
    sqlOrder = "DROP TABLE cicle"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Tabla borrada")
    except:
        return("Error al insertar el registro")

def insertaCount(dire, tipo , c1, c2):
    sqlOrder = " INSERT INTO cicle (direccion, tipo, count1, count2) VALUES (?,?,?,?)"
    dire2 = dire.strip('"')
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder,(dire2, tipo,c1,c2))
        conn.commit()
        return("Registro insertado")
    except:
        return("Error al insertar el registro")

def borraCount(dire):
    sqlOrder = " DELETE cicle WHERE direccion ='" + dire + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Registro borrado")
    except:
        return("Error al borrar el registro")

def actualizaCount1(dire,c1):
    sqlOrder = 'UPDATE cicle SET count1 = ? WHERE  direccion = ?'
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder(c1, dire))
        conn.commit()
        return("Registro actualizado")
    except:
        return("Error al actualizar el registro")

def actualizaCount2(dire,c2):
    sqlOrder = 'UPDATE cicle SET count2 = ? WHERE  direccion = ?'
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder, (c2, dire))
        conn.commit()
        return("Registro actualizado")
    except:
        return("Error al actualizar el registro")

def consultaCount1(dire):
    count=0
    sqlOrder = 'SELECT * FROM cicle WHERE direccion = ?'
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder, (dire, ))
        count = cur.fetchone()[2]
        return count
    except:
        print("Error en la lectura1")
    return count

def consultaCount2(dire):
    sqlOrder = 'SELECT * FROM cicle WHERE direccion = ?'
    count = 0
    try:
        print("Busco contador 2:",  sqlOrder)
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder, (dire, ))
        count = cur.fetchone()[3]
    except:
            print("Error en la lectura2")
            count = 0
    return count

def consultaPendientes():
    sqlOrder = "SELECT direccion FROM cicle WHERE count1 = 1"
    lista = []
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        for fila in cur:
            lista.append(fila[0])
    except:
            lista.append("No encuentro registros")
    return lista


def consultaTodos():
    sqlOrder = "SELECT * FROM cicle ORDER BY count2 DESC"
    lista = []
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        for fila in cur:
            lista.append(fila)
    except:
            lista.append("No encuentro registros")
    return lista

# Tabla de imagenes

def creaTablaImg():
    sqlOrder = "CREATE TABLE img (direccion TEXT, tipo TEXT)"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Tabla creada")
    except:
        return("Error al insertar el registro")


def borraTablaImg():
    sqlOrder = "DROP TABLE img"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Tabla borrada")
    except:
        return("Error al insertar el registro")

def insertaImg(dire, tipo):
    sqlOrder = " INSERT INTO img (direccion, tipo) VALUES (?,?)"
    dire2 = dire.strip('"')
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder,(dire2, tipo,c1,c2))
        conn.commit()
        return("Registro insertado")
    except:
        return("Error al insertar el registro")

def borraImg(dire):
    sqlOrder = " DELETE img WHERE direccion ='" + dire + "'"
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        conn.commit()
        return("Registro borrado")
    except:
        return("Error al borrar el registro")


def consultaTipoImg(tipo):
    count=0
    sqlOrder = 'SELECT direccion FROM img WHERE tipo = ?'
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder, (dire, ))
        count = cur.fetchone()
        return count
    except:
        print("Error en la lectura1")
    return count

def consultaImg(dire):
    count=0
    sqlOrder = 'SELECT tipo FROM img WHERE direccion = ?'
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder, (dire, ))
        count = cur.fetchone()
        return count
    except:
        print("Error en la lectura1")
    return count

def consultaTodosImg():
    sqlOrder = "SELECT direccion FROM img"
    lista = []
    try:
        conn = sqlite3.connect('enlaces.sqlite3')
        cur = conn.cursor()
        cur.execute(sqlOrder)
        for fila in cur:
            lista.append(fila)
    except:
            lista.append("No encuentro registros")
    return lista


