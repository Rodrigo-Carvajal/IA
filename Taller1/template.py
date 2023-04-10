from logicpuzzles import *
# LINK del puzzle: 

# Descripción del caso
#

#objetos = var1, var2, var3, var4
objeto1 = (, var(), var(), var())
objeto2 = (, var(), var(), var())
objeto3 = (, var(), var(), var())
objeto4 = (, var(), var(), var())
objetos = (objeto1, objeto2, objeto3, objeto4)

#Dominio de atributos
    #  = , , , 
    #  = '', '', '', ''
    #  = '', '', '', ''
    #  = '', '', '', ''

def funcion():

    return lall(
        #n Datos no mencionados
    )

start = perf_counter()
solutions = run(0, objetos, funcion(objetos))
end = perf_counter()
execution_time = (end - start)
print('Soluciones:', solutions)
print('Resuelto en (segundos):', execution_time)
