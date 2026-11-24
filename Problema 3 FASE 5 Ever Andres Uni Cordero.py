
# Problema 3: Control de inventario
# Ever Andres Uni Cordero
# Matriz con los datos de los artículos
inventario = [
    [101, "Arroz", 10, 20],
    [102, "Leche", 25, 15],
    [103, "Azucar", 5, 12],
    [104, "Aceite", 8, 10],
    [105, "Harina", 30, 20]
]

# Funcion para calcular la cantidad que se debe pedir
def calcular_reabastecimiento(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Mostrar el informe de reabastecimiento
print("REPORTE DE INVENTARIO")
print("-----------------------------")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_reabastecimiento(
        stock_actual, stock_minimo
    )

    print("Articulo:", nombre)
    print("Codigo:", codigo)
    print("Cantidad a solicitar:", cantidad_pedir)
    print("-----------------------------")
