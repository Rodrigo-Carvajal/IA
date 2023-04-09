from logicpuzzles import *

# Link del puzzle: https://logic.puzzlebaron.com/play.php?u2=9a1d2ad14f9714bfdc708a97f502d931

# Descripción del caso
#Curtis colecciona máquinas de pinball, ha estado pensando vender un par de maquinas.
#Ayudalo a determinar sus opciones determinando el año que fue construida, la compañia que la hizo y su precio actual.

#pin = año, precio, compañia, maquina,
pin1 = (1974, var(), var(), var())
pin2 = (1975, var(), var(), var())
pin3 = (1976, var(), var(), var())
pin4 = (1977, var(), var(), var())
pin5 = (1978, var(), var(), var())
maquinas = (pin1, pin2, pin3, pin4, pin5)

#Dominio de atributos
    # Año = 1974, 1975, 1976, 1977, 1978 
    # Precio = '$1500', '$1750', '$2000', '$52000', '$6400'
    # Compañia = 'Hayco Inc.', 'Maxigame', 'Pinnefore', 'Tarco Inc.', 'Waverly Toys'
    # Maquina = 'Aladeen', 'Bowling Alley', 'Meteor Rise', 'Voyager Hero', 'Zany Circus'

def pinball(maquinas):
    return lall(
        #1.- La máquina hecha por Hayco Inc. vale $1750. CUMPLE
        membero((var(), '$1750', 'Hayco Inc.', var()), maquinas),

        #2.- El juego hecho por Waverly Toys salió un año después que la máquina hecha por Tarco Inc. CUMPLE
        right_of(maquinas, (var(), var(), 'Waverly Toys', var()), (var(), var(), 'Tarco Inc.', var()), 1),

        #3.- De la máquina echa por Pinnefore y el juego de $1750, uno es aladeen y el otro fue lanzado en 1977. CUMPLE
        conde(
            (
            eq((1977, var(), 'Pinnefore', var()), pin4), 
            membero((var(), '$1750', var(), 'Aladeen'), maquinas)),
            (
            eq((1977, '$1750', var(), var()), pin4), 
            membero((var(), var(), 'Pinnefore', 'Aladeen'), maquinas))
        ),
        neq((1977, '$1750', 'Pinnefore', 'Aladeen'), pin4),

        #4.- Aladeen salió un año después a Meteor Rise. CUMPLE
        right_of(maquinas, (var(), var(), var(), 'Aladeen'), (var(), var(), var(), 'Meteor Rise')),

        #5.- Zany Circus salió un año después al juego hecho por Tarco Inc. CUMPLE
        right_of(maquinas, (var(), var(), var(), 'Zany Cricus'), (var(), var(), 'Tarco Inc.', var())),

        #6.- Zany Circus puede ser el juego de $6400 o de $2000. CUMPLE
        lany(membero((var(), '$2000', var(), 'Zany Cricus'), maquinas), membero((var(), '$6400', var(), 'Zany Cricus'), maquinas)),

        #7.- Bowling Alley cuesta $1500. CUMPLE
        membero((var(), '$1500', var(), 'Bowling Alley'), maquinas),

        #8.- La máquina lanzada en 1975 no cuesta $5200. CUMPLE
        neq((1975, '$5200', var(), var()), pin2),

        #9.- La máquina hecha por Tarco Inc. salió 2 años antes de la máquina de $6400. CUMPLE
        left_of(maquinas, (var(), var(), 'Tarco Inc.', var()), (var(), '$6400', var(), var()), 2),
        
        #10.- Datos no mencionados
        membero((var(), '$5200', var(), var()), maquinas),
        membero((var(), var(), 'Maxigame', var()), maquinas),
        membero((var(), var(), var(), 'Voyager Hero'), maquinas)
    )

solutions = run(0, maquinas, pinball(maquinas))
print(solutions)
