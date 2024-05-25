def leer_glcs(file_path):
    with open(file_path, 'r') as file:
        # Leer el número de casos
        n = int(file.readline().strip())

        # Lista para almacenar todos los casos
        casos = []

        for _ in range(n):
            # Leer el número de no terminales
            k = int(file.readline().strip())

            # Diccionario para almacenar las producciones de cada no terminal
            producciones = {}

            for _ in range(k):
                # Leer cada línea de producción
                linea = file.readline().strip()
                no_terminal, produccion = linea.split('->')
                no_terminal = no_terminal.strip()
                alternativas = [alt.strip() for alt in produccion.split('|')]

                # Agregar las producciones al diccionario
                producciones[no_terminal] = alternativas

            # Agregar el caso a la lista de casos
            casos.append(producciones)

    return casos


# Uso del código con el archivo glcs.in
file_path = 'glcs.in'
casos = leer_glcs(file_path)

# Imprimir los casos leídos para verificar
for i, caso in enumerate(casos):
    print(f"Casos {i + 1}:")
    for no_terminal, producciones in caso.items():
        print(f"{no_terminal} -> {' | '.join(producciones)}")
    print()
