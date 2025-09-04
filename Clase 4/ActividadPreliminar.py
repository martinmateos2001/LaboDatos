empleado_01 = [ #dni, edad, hijos, salario
                [20222333, 45, 2, 20000],
                [33456234, 40, 0, 25000],
                [45432345, 41, 1, 10000]]

def superanSalario(empleado, salario):
    res = []
    for e in empleado:
        if (e[3]> salario):
            res.append(e)
    return res

print(superanSalario(empleado_01, 15000))

empleado_02 = [ [20222333, 45, 2, 20000],
                [33456234, 40, 0, 25000],
                [45432345, 41, 1, 10000],
                [43967304, 37, 0, 12000],
                [42236276, 36, 0, 18000]]

print(superanSalario(empleado_02, 15000))

#Si se modifica el orden de las columnas ya no funciona

"""Respuestas Finales
1· 
    a· Funcionó
    b· No funcionó

2· Al cambiar la representacion del empleado tampoco funcionó

3· La ventaja de disponer de una funcion en lugar de escribir codigo el ahorro de tiempo.
"""