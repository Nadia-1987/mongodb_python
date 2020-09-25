# Ejercicios de profundización [Python]
EL propósito de este ejercicio es que el alumno ponga sus habilidades de NoSQL junto con otras adqueridas a lo largo de la carrera como el manejo de request API JSON.

# Enunciado
El objetivo es realizar un ejercicio muy similar al realizado en el pasado con la API de jsonplaceholder. Deberan consumir toda la información que retorna el request de la API y almacenarla en una db.

url = https://jsonplaceholder.typicode.com/todos

Deberá generar una base de datos NoSQL con Mongo que posea los siguientes campos:
- userId --> [número] id del usuario
- id --> [número] id de la consulta (no es necesario que sea el "_id" de Mongo)
- title --> [texto] nombre del título
- completed --> [bool] completado o no el título

## clear()
Deben crear una función "clear" la cual borre todos los campos existentes en la DB, esto les permitirá realizar cada prueba desde cero.

## fill()
Deben crear una función "fill" que lea los datos provenientes del JSON request y complete la base de datos. Si se fijan los datos que retorna el JSON en el request son exactamente los mismos que se solicitan en el ejercicio, por lo que pueden insertar el JSON tal cual les llega de la API en la base de datos (todos juntos o uno por uno)

## title_completed_count(userId)
Deben crear una función que lea la DB (find) y cuente (count) cuantos usuarios con "userId" han completado sus títulos. Para esto sentencia "find" de Mongo deberá tener dos campos condicionales (userId y completed) y utilizar el método count para contar los casos favorables.

## Esquema del ejercicio
Deben crear su archivo de python y crear las funciones mencionadas en este documento. Deben crear la sección "if _name_ == "_main_" y ahí crear el flujo de prueba de este programa:
```
if __name__ == "__main__":
  # Borrar DB
  clear()

  # Completar la DB con el JSON request
  fill()

  # Buscar autor
  userId = 5
  title_completed_count(userId)

```
