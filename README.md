## GLS First and Follow 
Este programa esta hecho por Jacobo Giraldo y Felipe Ochoa <br>
IDE: PyCharm 2023.3.2 <br>

# Explicación del codigo:
**Resumen del Código**
Este proyecto en Python implementa los algoritmos para calcular los conjuntos FIRST y FOLLOW en la teoría de compiladores. El código se divide <br>
en varias funciones, cada una con una responsabilidad específica. El codigo lo implementamos de una manera no recursiva , si no atraves de un while  <br>
en cada una de las funciones para darle una aplicacion diferente al problema.

*Funciones*
- leer_glcs(file_path) <br>
Esta función lee un archivo de entrada que contiene una gramática libre de contexto (GLC) y la convierte en un formato más manejable para <br>
su posterior procesamiento. La gramática se almacena en un diccionario donde las claves son los no terminales y los valores son listas de las <br>
producciones posibles. <br>

- compute_first(producciones) <br>
Esta función calcula el conjunto FIRST para cada no terminal en la gramática. El conjunto FIRST de un no terminal es el conjunto de terminales <br>
que pueden aparecer al inicio de una cadena derivada de ese no terminal. <br>

- compute_follow(producciones, start_symbol, first) <br>
Esta función calcula el conjunto FOLLOW para cada no terminal en la gramática. El conjunto FOLLOW de un no terminal es el conjunto de terminales <br>
que pueden aparecer inmediatamente después de ese no terminal en una cadena derivada del símbolo inicial de la gramática. <br>

- escribir_pr_sig(file_path, casos, first_sets, follow_sets) <br>
Esta función escribe los conjuntos FIRST y FOLLOW calculados en un archivo de salida en un formato específico.

- main(input_file_path, output_file_path) <br>
Esta es la función principal que coordina todo el proceso. Lee la gramática del archivo de entrada, calcula los conjuntos FIRST y FOLLOW, y luego <br>
escribe los resultados en el archivo de salida.

# Uso:
Para usar este código, simplemente se debe ejecutar el archivo Main.py con las rutas a los archivos de entrada y salida como argumentos. El archivo <br>
de entrada debe contener una representación de una gramática libre de contexto (GLC), y el archivo de salida contendrá los conjuntos FIRST y FOLLOW <br>
calculados para cada no terminal en la gramática.
# Rutas a los archivos de entrada y salida
input_file_path = 'glcs.in'
output_file_path = 'pr_sig.out'
main(input_file_path, output_file_path)



