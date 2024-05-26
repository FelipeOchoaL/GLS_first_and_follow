#Funcion para leer el archivo de entrada
def leer_glcs(file_path):
    with open(file_path, 'r') as file:
        # Leer el número de casos
        n = int(file.readline().strip()) # este seria el primer numero que encontramos en el archivo

        # Lista para almacenar todos los casos
        casos = []

        for _ in range(n):
            # Leer el número de no terminales
            k = int(file.readline().strip()) # este seria el segundo numero que encontramos en el archivo

            # Diccionario para almacenar las producciones de cada no terminal
            producciones = {} # este seria el diccionario que almacenara las producciones de cada no terminal

            for _ in range(k): # este for se encargara de leer las producciones de cada no terminal
                # Leer cada línea de producción
                linea = file.readline().strip() # este linea contiene la produccion de un no terminal
                no_terminal, produccion = linea.split('->') # aca estamos separando el no terminal de la produccion
                no_terminal = no_terminal.strip()
                alternativas = [alt.strip() for alt in produccion.split('|')]

                # Agregar las producciones al diccionario
                if no_terminal not in producciones:
                    producciones[no_terminal] = []
                producciones[no_terminal].extend(alternativas)

            # Agregar el caso a la lista de casos
            casos.append(producciones)

    return casos


def compute_first(producciones):
    first = {nt: set() for nt in producciones}

    # Inicialización
    for nt in producciones:
        for produccion in producciones[nt]:
            if produccion[0].islower() or produccion[0] == 'ε':
                first[nt].add(produccion[0])

    # Propagación
    changed = True
    while changed:
        changed = False
        for nt in producciones:
            for produccion in producciones[nt]:
                i = 0
                while i < len(produccion):
                    symbol = produccion[i]
                    if symbol.isupper():
                        before = len(first[nt])
                        first[nt].update(first[symbol] - {'ε'})
                        if 'ε' in first[symbol]:
                            i += 1
                        else:
                            break
                        if before != len(first[nt]):
                            changed = True
                    else:
                        first[nt].add(symbol)
                        break

    return first


def compute_follow(producciones, start_symbol, first):
    follow = {nt: set() for nt in producciones}
    follow[start_symbol].add('$')

    changed = True
    while changed:
        changed = False
        for nt in producciones:
            for produccion in producciones[nt]:
                trailer = follow[nt].copy()
                for symbol in reversed(produccion):
                    if symbol.isupper():
                        before = len(follow[symbol])
                        follow[symbol].update(trailer)
                        if 'ε' in first[symbol]:
                            trailer.update(first[symbol] - {'ε'})
                        else:
                            trailer = first[symbol]
                        if before != len(follow[symbol]):
                            changed = True
                    else:
                        trailer = {symbol}

    return follow


def escribir_pr_sig(file_path, casos, first_sets, follow_sets):
    with open(file_path, 'w') as file:
        # Escribir el número de casos
        file.write(f"{len(casos)}\n")

        for producciones, first, follow in zip(casos, first_sets, follow_sets):
            # Escribir el número de no terminales
            k = len(producciones)
            file.write(f"{k}\n")

            # Escribir los conjuntos First
            for nt in producciones:
                primeros = ','.join(sorted(first[nt]))
                file.write(f"Pr({nt}) = {{{primeros}}}\n")

            # Escribir los conjuntos Follow
            for nt in producciones:
                siguientes = ','.join(sorted(follow[nt]))
                file.write(f"Sig({nt}) = {{{siguientes}}}\n")


def main(input_file_path, output_file_path):
    casos = leer_glcs(input_file_path)

    first_sets = []
    follow_sets = []

    for producciones in casos:
        first = compute_first(producciones)
        follow = compute_follow(producciones, list(producciones.keys())[0], first)

        first_sets.append(first)
        follow_sets.append(follow)

    escribir_pr_sig(output_file_path, casos, first_sets, follow_sets)


# Rutas a los archivos de entrada y salida
input_file_path = 'glcs.in'
output_file_path = 'pr_sig.out'
main(input_file_path, output_file_path)
