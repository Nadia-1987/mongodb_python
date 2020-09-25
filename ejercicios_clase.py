#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json

import tinymongo as tm
import tinydb

# Bug: https://github.com/schapman1974/tinymongo/issues/58
class TinyMongoClient(tm.TinyMongoClient):
    @property
    def _storage(self):
        return tinydb.storages.JSONStorage

db_name = 'secundaria'


def clear():
    conn = TinyMongoClient()
    db = conn[db_name]

    # Eliminar todos los documentos que existan en la coleccion secundaria
    db.secundaria.remove({})

    # Cerrar la conexión con la base de datos
    conn.close()


def fill(name, age, grade, tutor):
    print('Completemos esta tablita!')
    # Llenar la coleccion "estudiante" con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto completado por mongo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia insert_one o insert_many.

    conn = TinyMongoClient()
    db = conn[db_name]

    estudiante_json = {"name": name, "age": age, "grade": grade, "tutor" : tutor}
    db.secundaria.insert_one(estudiante_json)

    conn.close()

def show(fetch_all=True):
    print('Comprovemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia find para imprimir en pantalla
    # todos los documentos de la DB
    # Queda a su criterio serializar o no el JSON "dumps"
    #  para imprimirlo en un formato más "agradable"

    conn = TinyMongoClient()
    db = conn[db_name]

    
    if fetch_all is True:
        cursor = db.secundaria.find()
        data = list(cursor)
        json_string = json.dumps(data, indent=4)
        print(json_string)

  
    for doc in cursor:
        print(doc)

    
    conn.close()


def find_by_grade(grade):
    print('Operación búsqueda!')
    # Utilizar la sentencia find para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes debe imprimir
    # en pantalla unicamente los siguiente campos por cada uno:
    # id / name / age

    conn = TinyMongoClient()
    db = conn[db_name]

    
    estudiante_data = db.secundaria.find_one({"grade": grade})

   
    conn.close()
    return estudiante_data
    

def insert(student):
    print('Nuevos ingresos!')
    # Utilizar la sentencia insert_one para ingresar nuevos estudiantes
    # a la secundaria

    # El parámetro student deberá ser un JSON el cual se inserta en la db

    conn = TinyMongoClient()
    db = conn[db_name]

    estudiante_json = (student)
    db.secundaria.insert_one(estudiante_json)

    conn.close()




def count(grade):
    print('Contar estudiantes')
    # Utilizar la sentencia find + count para contar
    # cuantos estudiantes pertenecen el grado "grade"

    conn = TinyMongoClient()
    db = conn[db_name]

    count = db.secundaria.find({"grade": grade}).count()

    # Cerrar la conexión con la base de datos
    conn.close()
    return count


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # Borrar la db
    clear()

    fill('Angel', 60, 6, 'Angel')
    fill('Silvia', 56, 5, 'Noemi')
    fill('Marcos', 26, 4, 'Daniel')
    fill('Anabela', 37, 3, 'Noemi')
    fill('Juan', 34, 2, 'Pablo')
    show()

    grade = 3
    find_by_grade(grade)

    student = {'name':'Alma', 'age' : 11, 'grade' : 1, 'tutor':'Nadia'}
    insert(student)

    count(grade)
