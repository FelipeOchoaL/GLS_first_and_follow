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


def main(file_path):
    casos = leer_glcs(file_path)

    for index, producciones in enumerate(casos):
        print(f"Casos {index + 1}:")
        for nt, prods in producciones.items():
            print(f"{nt} -> {' | '.join(prods)}")

        first = compute_first(producciones)
        follow = compute_follow(producciones, list(producciones.keys())[0], first)

        print("\nFirst sets:")
        for nt in first:
            print(f"First({nt}) = {first[nt]}")

        print("\nFollow sets:")
        for nt in follow:
            print(f"Follow({nt}) = {follow[nt]}")

        print("\n" + "=" * 50 + "\n")


# Ruta al archivo glcs.in
file_path = 'glcs.in'
main(file_path)