import csv

# Abre el archivo CSV
with open('complementos.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    # Itera sobre cada fila del archivo
    for row in reader:
        # Busca la fila que contiene 'cliente1'
        if 'cliente1' in row:
            # Cuenta los valores 'Nada' en esa fila
            count_nada = row.count('Nada')
            n=count_nada
            preciocomplementos=(4-n)*4
            print("El precio de los complementos es: ", preciocomplementos, "€")
            print("El precio de la pizza es de: ", 8, "€")
            preciototal=preciocomplementos+8
            print("El precio total es de: ", preciototal, "€")
            if preciototal == 24:
                print("Al haber pedidO entrante, pizza, bebida y postre forma un menu individual de tarifa reducida, el nuevo precio es de 20 euros")
                preciototal=20
            break  # Termina el bucle una vez que se encuentra 'cliente1'
    else:
        print("No se encontró 'cliente1' en el archivo.")