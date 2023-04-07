from logicpuzzles import *

# LINK del puzzle: https://logic.puzzlebaron.com/play.php?u2=ec0ee47cc5a3ced4d208c01bf8032c85

# Descripción del caso
# El conductor de la escuela del condado de alameda tiene una agenda acotada. Usando las siguientes pistas, identifique cada estudiante a su instructor o instructora y
# determinar la hora de cita y edad de cada estudiante.

#Hay 5 estudiantes:
#estudiante = (hora, nombre, edad, instructor)
estudiante1 = (9, var(), var(), var())
estudiante2 = (10, var(), var(), var())
estudiante3 = (11, var(), var(), var())
estudiante4 = (12, var(), var(), var())
estudiante5 = (1, var(), var(), var())
estudiantes = (estudiante1, estudiante2, estudiante3, estudiante4, estudiante5)

# Dominio de atributos
    # horas = (9, 10, 11, 12, 1)
    # nombre = ('Dwayne','Elmer','Harold','Isaac','Lorena')
    # edad = (17, 18, 19, 20, 21)
    # instructores = ('Mr. French','Mrs. Huff','Mrs. Ingram','Mrs. Nolan','Mr. Slate')

def schoolDriverProblem(estudiantes):
    #estudiante = (hora, nombre, edad, instructor)
    return lall(
        #1.- El estudiante de 21 años esta agendado en algun momento después de Lorena. CUMPLE
        somewhat_right_of(estudiantes, (var(), var(), 21, var()), (var(), 'Lorena', var(), var())),

        #2.- El estudiante de 17 años no es Elmer. NO CUMPLE
        neq((var(), 'Elmer', 17, var()), estudiantes),

        #3.- Harold es el aprendiz del Sr. French o es el aprendiz de 17 años. CUMPLE
        lany(
            membero((var(), 'Harold', var(), 'Mr. French'), estudiantes), 
            membero((var(), 'Harold', 17, var()),estudiantes)
        ),
        neq((var(), 'Harold', 17, 'Mr. French'), estudiantes),

        #4.- El aprendiz de la señora huff's tiene 20 años. CUMPLE
        membero((var(), var(), 20, 'Mrs. Huff'), estudiantes),

        #5.- De Isaac y el estudiante de la clase de la 1:00 pm, uno es cliente de la Sra. Ingram y el otro tiene 20 años. CUMPLE
        conde(
            ((membero((var(), 'Isaac', var(), 'Mrs. Ingram'), estudiantes)), (eq((var(), var(), 20, var()), estudiante5))),
            ((membero((var(), 'Isaac', 20, var()), estudiantes)), (eq((var(), var(), var(), 'Mrs. Ingram'), estudiante5)))
        ),

        #6.- El entrenado por la señora Nolan esta agendado en algún momento después del estudiante de 20 años. CUMPLE
        somewhat_right_of(estudiantes, (var(), var(), var(), 'Mrs. Nolan'), (var(), var(), 20, var())),

        #7.- El estudiante del Sr. Slate está programado 2 horas después de Lorena. CUMPLE
        right_of(estudiantes, (var(), var(), var(), 'Mr. Slate'), (var(), 'Lorena', var(), var()), n=2),

        #8.- El estudiante de 21 años está programado en algún momento antes que Elmer. CUMPLE
        somewhat_left_of(estudiantes, (var(), var(), 21, var()), (var(), 'Elmer', var(), var())),

        #9.- El cliente de 19 años es Harold. CUMPLE
        membero((var(), 'Harold', 19, var()), estudiantes),

        #10.- Datos no mencionados
        membero((var(), 'Dwayne', var(), var()), estudiantes),
        membero((var(), var(), 18, var()), estudiantes),
        membero((var(), var(), 17, var()), estudiantes),
        membero((var(), 'Elmer', var(), var()), estudiantes),
    )

#Ejecución
solutions = run(1, estudiantes, schoolDriverProblem(estudiantes))
print(solutions)