def recibir_cantidad_de_producto():
    # print('Ingrese el número de productos')
    cantidad_de_producto = int(input())
    return cantidad_de_producto


def recibir_info_producto(numero_producto):
    """Recibe los datos de un producto por teclado
    y los devuelve organizados en un diccionario
    """
    # print(f"Ingrese los datos del producto {numero_producto + 1}")

    # print("Código del producto")
    codigoProducto = str(input())

    # print("Nombre del producto")
    nombreProducto = str(input())

    # print("Cantidad comprada")
    cantidad = int(input())

    # print("Valor sin iva: ")
    valorUnitarioSinIva = float(input())

    # print("Tipo de iva: \n1: 0% \n2: 5% \n3: 19%")
    tipoDeIva = float(input())

    return {
        "codigo": codigoProducto,
        "nombre": nombreProducto,
        "cantidad": cantidad,
        "valor_sin_iva": valorUnitarioSinIva,
        "tipo_iva": tipoDeIva,
    }


def calcular_valores_asociados(info_producto):

    """Esta funcion recibe la información
    de un producto y calcula el IVA unitario,
    el valor unitario con IVA, el IVA total y
    el valor total con IVA

    La estructura del parametro de entrada es:

    info_producto = {
        "codigo": "ABCDE",
        "nombre": "Lápiz",
        "cantidad": 10,
        "valor_sin_iva": 10000,
        "tipo_iva": 1
    }

    La estructura del diccionario de salida es:

    info_producto = {
        "codigo": "ABCDE",
        "nombre": "Lápiz",
        "cantidad": 10,
        "valor_sin_iva": 10000,
        "tipo_iva": 2,
        "valor_iva_unitario": 500,
        "valor_unitario_con_iva": 10500,
        "valor_iva_total": 5000,
        "valor_total_con_iva": 105000
    }
    """
    # Extraemos los valores que necesitamos
    tipo_iva = info_producto.get("tipo_iva")
    valor_sin_iva = info_producto.get("valor_sin_iva")
    cantidad = info_producto.get("cantidad")

    # Definimos el porcentaje de IVA a aplicar, dependiendo
    # del tipo de IVA en la entrada
    if tipo_iva == 1:
        porcentaje = 0
    elif tipo_iva == 2:
        porcentaje = 0.05
    elif tipo_iva == 3:
        porcentaje = 0.19
    else:
        print("error, tipo de iva invalido")

    # Calcula valor IVA unitario
    valor_iva_unitario = valor_sin_iva * porcentaje

    # Calcula valor total producto sin IVA
    valor_producto_sin_iva = valor_sin_iva * cantidad

    # Calcula valor IVA del producto
    valor_iva_producto = valor_producto_sin_iva * porcentaje

    # valor total del producto, es decir, incluyendo el IVA y las cantidades compradas
    valor_producto_con_iva = valor_producto_sin_iva + valor_iva_producto

    # Guardamos los valores asociados como llaves del diccionario
    info_producto["valor_iva_unitario"] = valor_iva_unitario
    info_producto["valor_producto_sin_iva"] = valor_producto_sin_iva
    info_producto["valor_iva_producto"] = valor_iva_producto
    info_producto["valor_total_producto"] = valor_producto_con_iva

    # Devolvemos el diccionario con los datos obtenidos
    return info_producto


def ordenar_alfabeticamente(listaProductos, param):
    listaProductosOrdenada = sorted(
        listaProductos, key=lambda producto: producto[param]
    )
    return listaProductosOrdenada


def presenta_datos(listaProductos, valor_total, iva_acumulado):
    for producto in listaProductos:
        print(producto.get("codigo"))
        print(producto.get("valor_iva_producto"))
        print(producto.get("valor_producto_sin_iva"))
        print(producto.get("valor_total_producto"))
    print(valor_total)
    print(iva_acumulado)


if __name__ == "__main__":
    # Inicializa variables
    codigoProducto = 0
    nombreProducto = ""
    valorUnitarioSinIva = 0
    cantidad = 0
    valorTotalSinIva = 0
    valorTotalConIva = 0
    tipoDeIva = 0
    listaProductos = []
    listaFinalProductos = []
    listaCodigo = []
    listaNombre = []
    listaCantidad = []
    listaValorUnitario = []
    listaTipoDeIva = []
    iva_acumulado = 0
    valor_total_acumulado = 0

    # Recibe número de productos a procesar
    cantidad = recibir_cantidad_de_producto()

    # Recibe Informacion de cada producto
    rango_productos = range(cantidad)
    for n in rango_productos:
        info_basica = recibir_info_producto(n)
        info_completa = calcular_valores_asociados(info_basica)
        iva_acumulado = iva_acumulado + info_completa.get("valor_iva_producto")
        valor_total_acumulado = valor_total_acumulado + info_completa.get(
            "valor_total_producto"
        )
        listaProductos.append(info_completa)

    # Ordena la lista de acuerdo al parametro "codigo" de cada objecto
    listaProductosOrdenada = ordenar_alfabeticamente(listaProductos, "nombre")
    # Presenta los datos de acuerdo a los requerimientos del reto
    presenta_datos(listaProductosOrdenada, valor_total_acumulado, iva_acumulado)
