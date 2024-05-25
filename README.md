## GLS First and Follow 
Este programa esta hecho por Jacobo Giraldo y Felipe Ochoa <br>
IDE: PyCharm 2023.3.2 <br>

# Explicación del codigo:
**Primera parte** <br>
1. Apertura y lectura del archivo: <br>
Abrimos el archivo glcs.in y leemos la primera línea que contiene el número de casos n. <br>

2. Procesamiento de cada caso: <br>
- Para cada caso, leemos el número de no terminales k. <br>
- Creamos un diccionario producciones para almacenar las producciones de cada no terminal. <br>

3. Lectura de las producciones: <br>
- Leemos k líneas, cada una representando una producción. <br>
- Para cada línea de producción, separamos el no terminal del lado izquierdo (no_terminal) de las alternativas del lado derecho (produccion). <br>
- Dividimos las alternativas separadas por | y las limpiamos de espacios en blanco. <br>
- Agregamos las producciones al diccionario. <br>

4. Almacenamiento y salida: <br>
- Almacenamos cada caso en una lista casos. <br> 
- Imprimimos los casos para verificar que se han leído correctamente. <br>

