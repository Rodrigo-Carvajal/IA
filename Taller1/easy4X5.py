from logicpuzzles import *

# LINK del puzzle: https://logic.puzzlebaron.com/play.php?u2=ec0ee47cc5a3ced4d208c01bf8032c85

# Descripción del caso
# El conductor de la escuela del condado de alameda tiene una agenda acotada. Usando las siguientes pistas, identifique cada estudiante a su instructor o instructora y
# determinar la hora de cita y edad de cada estudiante.

#Hay 5 estudiantes:
#estudiante = (Nombre, hora, edad, instructor)
estudiante1 = (9, var(), var(), var())
estudiante2 = (10, var(), var(), var())
estudiante3 = (11, var(), var(), var())
estudiante4 = (12, var(), var(), var())
estudiante5 = (1, var(), var(), var())
estudiantes = (estudiante1, estudiante2, estudiante3, estudiante4, estudiante5)

# Estdudiante(Instructor, edad, hora de cita)
def schoolDriverProblem(estudiantes):
    return lall(
        #1.- El estudiante de 21 años esta agendado en algun momento después de Lorena

        #2.- El estudiante de 17 años no es Elmer.

        #3.- Harold es el aprendiz del Sr. French o es el aprendiz de 17 años.

        #4.- El aprendiz de la señora huff's tiene 20 años

        #5.- De Isaac y el estudiante de la clase de la 1:00 pm, uno es cliente de la Sra. Ingram y el otro tiene 20 años.

        #6.- El entrenado por la señora Nolan esta agendado en algún momento después del estudiante de 20 años

        #7.- El estudiante del Sr. Slate está programado 2 horas después de Lorena.
            
        #8.- El estudiante de 21 años está programado en algún momento antes que Elmer.
            
        #9.- El cliente de 19 años es Harold.
    )

#Ejecución
solutions = run(0, estudiantes, schoolDriverProblem(estudiantes))
print(solutions)