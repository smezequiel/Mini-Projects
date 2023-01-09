# Movimientos de la Torre #
start_column = int(input("Ingrese"))
end_column = int(input("Ingrese"))
start_row = int(input("Ingrese"))
end_row = int(input("Ingrese"))

if (start_column != end_column):
    if start_row == end_row:
        print("YES")
    else:
        print("NO")
else:
    if start_row == end_row:
        print("NO")
    else:
        print("YES")

# Movimientos del Alfil

start_column = int(input("Ingrese columna: "))
start_row = int(input("Ingrese fila: "))
end_column = int(input("Ingrese columna final: "))
end_row = int(input("Ingrese fila final: "))

diference = start_column - end_column

if end_row == (start_row + diference):
    print("YES")
elif end_row == (start_row - diference):
    print("YES")
else:
    print("NO")

# Movimientos del Rey

start_column = int(input("Ingrese"))
start_row = int(input("Ingrese"))
end_column = int(input("Ingrese"))
end_row = int(input("Ingrese"))

if end_column == (start_column+1) or end_column == (start_column-1) or end_column == start_column:
    if end_row == (start_row+1) or end_row == (start_row-1) or end_row == start_row:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

# Movimientos de la Reina

start_column = int(input("Ingrese columna: "))
start_row = int(input("Ingrese fila: "))
end_column = int(input("Ingrese columna final: "))
end_row = int(input("Ingrese fila final: "))

diference = start_column - end_column


if end_row == (start_row + diference) or end_row == (start_row - diference):
    print("YES")
elif (start_column != end_column and start_row == end_row) or (start_column == end_column and start_row != end_row):
    print("YES")
elif (end_column == (start_column+1) or end_column == (start_column-1) or end_column == start_column) and (end_row == (start_row+1) or end_row == (start_row-1) or end_row == start_row):
    print("YES")
else:
    print("NO")

# o sino:

start_column = int(input("Ingrese columna: "))
start_row = int(input("Ingrese fila: "))
end_column = int(input("Ingrese columna final: "))
end_row = int(input("Ingrese fila final: "))
if abs(start_column - end_column) == abs(start_row - end_row) or start_column == end_column or start_row == end_row:
    print('YES')
else:
    print('NO')


# Movimiento del Caballo

start_column = int(input("Ingrese columna: "))
start_row = int(input("Ingrese fila: "))
end_column = int(input("Ingrese columna final: "))
end_row = int(input("Ingrese fila final: "))

if end_column == (start_column + 2) or end_column == start_column - 2:
    if end_row == (start_row + 1) or end_row == (start_row - 1):
        print("YES")
    else:
        print("NO")
elif end_column == (start_column + 1) or end_column == start_column - 1:
    if end_row == start_row + 2 or end_row == start_row - 2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

# o sino:

start_column = int(input("Ingrese columna: "))
start_row = int(input("Ingrese fila: "))
end_column = int(input("Ingrese columna final: "))
end_row = int(input("Ingrese fila final: "))

dif_column = abs(start_column - end_column)
dif_row = abs(start_row - end_row)

if dif_column == 1 and dif_row == 2 or dif_column == 2 and dif_row == 1:
    print('YES')
else:
    print('NO')
