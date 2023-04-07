from logicpuzzles import *

# LINK del puzzle: https://logic.puzzlebaron.com/play.php?u2=2b92ca1acc4a20ad14a5fd80eaf18efb

# Descripción del caso
#

#caja = dia, lat, lon, item
caja1 = (3, var(), var(), var())
caja2 = (6, var(), var(), var())
caja3 = (9, var(), var(), var())
caja4 = (12, var(), var(), var())
cajas = (caja1, caja2, caja3, caja4)

#Dominio de atributos
    #  = , , , 
    #  = '', '', '', ''
    #  = '', '', '', ''
    #  = '', '', '', ''

def geocaches():

    return lall(
        #1.- 

        #2.- 

        #3.-

        #4.-

        #5.-

        #6.-

        #7.- Datos no mencionados
    )

solutions = run(0, cajas, geocaches(cajas))
print(solutions)