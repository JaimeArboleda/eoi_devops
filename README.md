# Introducción

Tenemos que crear una aplicación que simule el lanzamiento de dados. Con el objetivo de instalar dependencias usaremos la libreria dice (https://pypi.org/project/dice/). 

Dentro del código debemos implementar una función que reciba los argumentos amount y sides. Está función devolverá una lista de tamaño "amount" en el que cada elemento sea el resultado de lanzar un dado de "sides" caras. 

Esta función se llamará con los parámetros, amount=5 y sides=6 y mostrará los resultados como "Lanzamiento {número de lanzamiento} número obtenido {resultado lanzamiento}" con un sleep de 5 segundos entre lanzamientos. 

Como el objetivo de la actividad no es el desarrollo de código, si lo necesitáis, podéis partir del código disponible en (https://github.com/megmontero/devops-a1). 


# Tareas

## Crear Repositorio en GitHub 

En este apartado tendréis que registraros en GitHub y crear un nuevo repositorio público (podéis utilizar el nombre que queráis). En los siguientes apartados trabajaremos con este repositorio.

## Código 

* En la rama **main**: 
  * Tendremos que realizar un primer commit con el fichero Readme.md describiendo lo que hará nuestra aplicación.
  * Crearemos un segundo commit. Con el código.
  * En un tercer commit haremos un cambio en el mensaje de salida (cualquier cambio es válido).
  * Haremos un revert del último commit.
* (Opcional) En la rama **feature/rol**:
  * Crear una nueva rama feature/rol a partir de main.
  * Modificar el dado para que tenga 20 caras.
  * Volver a main y modificar el código para que se realicen 6 lanzamientos.
  * Mergear este cambio en la rama feature/rol.

Es importante que todos los cambios se actualicen en el repositorio remoto.

Unicamente se entregará la url del repositorio creado. 