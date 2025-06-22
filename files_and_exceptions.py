def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    #Se declara el diccionario donde se guardara como clave el product_name y como value, una lista de los product_price
    prices_of_products = {}
    
    try:
        #Se intenta leer el archivo
        with open(filename, 'r') as file:

            #Se obtienen un array de los productos con la forma: (product_name:product_price)
            rows = file.read().split(';')

            #se iteran los productos
            for product in rows:

                #proteccion ante el ; duplicados o el final
                if not product:
                    continue

                print(product)
                #Se consigue separar los valores de: (product_name:product_price)
                product_info = product.split(':')

                print(product_info)

                #Se guarda el nombre del producto
                product_name = product_info[0]

                #Se guarda el precio del producto
                product_price = float(product_info[1])

                #Si el nombre del producto esta dentro del diccionario
                if product_name in prices_of_products:

                    #agrega a la lista de precios el precio iterado
                    prices_of_products[product_name].append(product_price)
                else: #Si no esta el nombre del producto dentro del diccionario

                    #Se crea una lista con el precio iterado
                    prices_of_products[product_name] = [product_price]
    #Si surge un error de tipo FileNotFoundError
    except FileNotFoundError:

        #Se retorna que no existe el archivo
        raise FileNotFoundError(f'{filename} no existe')
      
    #retorna el diccionario con los precios
    return prices_of_products


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """

    #Iteramos el diccionario de data
    for product, prices in data.items():

        #Conseguimos el valor total de la suma de los precios
        total_price = sum(prices)

        #Conseguimos el promedio de la suma entre la cantidad de productos vendidos
        average_price = total_price / len(prices)

        #Mostramos los resultado por producto
        print(f'{product}: ventas totales ${total_price}0, promedio ${average_price}0')

    #Se retorna None
    return None