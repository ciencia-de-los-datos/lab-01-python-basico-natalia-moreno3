"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

# csv path
file_name = 'data.csv'
# open csv

with open(file_name, 'r') as f:
    # read csv with delimiter \t
    file = csv.reader(f, delimiter='\t')
    lines = [line for line in file]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    second_colum = [(int(line[1])) for line in lines]
    Sum = sum(second_colum)
        
    return Sum
# print(pregunta_01())

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    dict = {}
    for line in lines:
        dict[line[0]] = dict.get(line[0], 0) + 1
    
    list = [(key, value) for key, value in dict.items()]
    list = sorted(list, key=lambda x: x[0])

    return list
# print(pregunta_02())

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    dict = {}
    for line in lines:
        dict[line[0]] = dict.get(line[0], 0) + int(line[1])
    
    list = [(key, value) for key, value in dict.items()]
    list = sorted(list, key=lambda x: x[0])

    return list
# print(pregunta_03())

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    dict = {}
    for line in lines:
        month = line[2].split('-')[1]
        dict[month] = dict.get(month, 0) + 1
    
    list = [(key, value) for key, value in dict.items()]
    list = sorted(list, key=lambda x: x[0])

    return list
# print(pregunta_04())

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    dict = {}
    for line in lines:
        dict[line[0]] = dict.get(line[0], [])
        dict[line[0]].append(int(line[1]))

    list = [(key, max(value), min(value)) for key, value in dict.items()]
    list = sorted(list, key=lambda x: x[0])

    return list
# print(pregunta_05())


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    dict = {}
    for line in lines:
        pairs = line[4].split(',')
        for pair in pairs:
            key, value = pair.split(":")
            dict[key] = dict.get(key, [])
            dict[key].append(int(value))

    list = [(key, min(value), max(value)) for key, value in dict.items()]
    list = sorted(list, key=lambda x: x[0])

    return list
# print(pregunta_06())

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    dict = {}
    for line in lines:
        dict[line[1]] = dict.get(line[1], []) 
        dict[line[1]].append(line[0])
    
    list = [(int(key), value) for key, value in dict.items()]
    list = sorted(list, key=lambda x: x[0])

    return list
# print(pregunta_07())

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    dict = {}
    for line in lines:
        dict[line[1]] = dict.get(line[1], set()) 
        dict[line[1]].add(line[0])
    
    list = [(int(key), sorted(value, key=lambda x: x[0])) for key, value in dict.items()]
    list = sorted(list, key=lambda x: x[0])

    return list
# print(pregunta_08())

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    dict = {}
    for line in lines:
        pairs = line[4].split(',')
        for pair in pairs:
            key, _ = pair.split(":")
            dict[key] = dict.get(key, 0) + 1

    list = [(key, value) for key, value in dict.items()]
    list = sorted(list, key=lambda x: x[0])
    dict = {key: value for key, value in list}

    return dict
# print(pregunta_09())

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    list = []
    for line in lines:
        list.append((line[0], len(line[3].split(',')), len(line[4].split(','))))
    
    return list
# print(pregunta_10())

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    dict = {}
    for line in lines:
        pairs = line[3].split(',')
        for key in pairs:
            dict[key] = dict.get(key, 0) + int(line[1])

    list = [(key, value) for key, value in dict.items()]
    list = sorted(list, key=lambda x: x[0])
    dict = {key: value for key, value in list}

    
    return dict
# print(pregunta_11())


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    dict = {}
    for line in lines:
        pairs = line[4].split(',')
        for pair in pairs:
            _, value = pair.split(":")
            dict[line[0]] = dict.get(line[0], 0) + int(value)

    list = [(key, value) for key, value in dict.items()]
    list = sorted(list, key=lambda x: x[0])
    dict = {key: value for key, value in list}

    return dict
# print(pregunta_12())