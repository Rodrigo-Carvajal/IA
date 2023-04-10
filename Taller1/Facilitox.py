from logicpuzzles import *
#Precio, Clientes, Colores, Signos
tatuaje1= (35, var(), var(), var())
tatuaje2= (40, var(), var(), var())
tatuaje3= (45, var(), var(), var())
tatuaje4= (50, var(), var(), var())
tatuajes= (tatuaje1, tatuaje2, tatuaje3, tatuaje4)
#Precio[35, 40, 45, 50]
#Clientes[Eula, Janie, Oscar, Wilma]
#Colores[Negro, Rosa, Rojo, Violeta]
#Signos[Acuario, Cancer, Geminis, Libra]

def tatuajeproblem(tatuajes):
    return lall(
       # El cliente que se hizo el tatuaje rojo pagó menos que el Cáncer. 
        somewhat_left_of(tatuajes, (var(), var(), 'Rojo', var()), (var(), var(), var(), 'Cancer')),

       # De los Libra y Eula, uno pagó $45 y el otro se hizo el tatuaje negro.
        conde((eq((45, var(), var(), 'Libra'), tatuaje3), membero((var(), 'Eula', 'Negro', var()), tatuajes)),
        (eq((45, 'Eula', var(), var()), tatuaje3), membero((var(), var(), 'Negro', 'Libra'), tatuajes))),

       # Ni el Aquarius ni Wilma fueron el cliente que pagó $40.
        neq((40, 'Acuario'), (tatuaje2[0], tatuaje2[3])),
        neq((40, 'Wilma'), (tatuaje2[0], tatuaje2[1])),

       # Janie se hizo el tatuaje violeta.
        membero((var(), 'Janie', 'Violeta', var()), tatuajes),

       # La persona que se hizo el tatuaje violeta pagó 5 dólares menos que Wilma.
        left_of(tatuajes, (var(), var(), 'Violeta', var()), (var(), 'Wilma',var(), var())),

       # El cliente que se hizo el tatuaje rojo pagó más que el Acuario.
        somewhat_right_of(tatuajes, (var(), var(), 'Rojo', var()), (var(), var(), var(), 'Acuario')),

       # Ni el Aquarius ni Wilma fueron el cliente que pagó $45.      
        neq((45, 'Acuario'), (tatuaje3[0], tatuaje3[3])),
        neq((45, 'Wilma'), (tatuaje3[0], tatuaje3[1])),

       #Datos faltantes
        membero((var(), 'Oscar', var(), var()), tatuajes),
        membero((var(), var(), var(), 'Geminis'), tatuajes),
        membero((var(), var(), 'Rosa', var()), tatuajes)
    )

solucion = run(0, tatuajes, tatuajeproblem(tatuajes),)
print(solucion)