from logicpuzzles import *
from time import perf_counter
# Hay 4 clases con su cantidad de alumnos, número de sala, clase y profesor
clase1 = (29, var(), var(), var())
clase2 = (31, var(), var(), var())
clase3 = (33, var(), var(), var())
clase4 = (35, var(), var(), var())
clase5 = (37, var(), var(), var())
clase6 = (39, var(), var(), var())
clases = (clase1, clase2, clase3, clase4, clase5, clase6)

#numero de sala = [114, 120, 122, 125, 314, 316]
#clase = ['Art','Chemistry','French','Geometry','History','Latin']
#profesor = ['Avery','Brady','Herman','Leach','Ray','Velasquez']
#var(), var(), var(), var()

#marinero = (alumnos, sala, asignatura, profesor)
def carrera(clases):
    return lall(
        #1. The course with 37 students isn't taught by Brady.
            neq((37, var(), var(), 'Brady'), clase5),
        #2. The course with 37 students isn't taught by Herman.
            neq((37, var(), var(), 'Herman'), clase5),
        #3. Of the Art class and Mr. Velasquez's class, one has 29 students and the other is in room 120.
            conde(
                (eq((29, var(), 'Art', var()), clase1), membero((var(), 120, var(), 'Velasquez'), clases)),
                (eq((29, var(), var(), 'Velasquez'), clase1), membero((var(), 120, 'Art', var()), clases))
            ),
            neq((29, 120, 'Art', 'Velasquez'), clase1),
        #4. The class in room 125 is either the class with 37 students or the French class.
        #5. Of Mr. Brady's class and the course with 39 students, one is in room 122 and the other is in room 114.
            conde(
                (eq((39, 122, var(), var()), clase6), membero((var(), 114, var(), 'Brady'), clases)),
                (eq((39, 114, var(), var()), clase6), membero((var(), 122, var(), 'Brady'), clases))
            ),
        #6. The Chemistry class is either the course with 31 students or Mr. Velasquez's class.            
        #7. The course in room 314 has somewhat fewer students than Mr. Brady's class.
        #8. Of the class in room 114 and the History class, one has 39 students and the other is taught by Herman.
        #9. The History class, the Latin class and the course in room 318 are all different classes.
        #10. The Geometry class has 2 more students than Mr. Avery's class.
        #11. Mr. Ray's class has 2 fewer students than the History class.
        #12. Neither the class in room 314 nor the course in room 114 is the Geometry class.
    )

start = perf_counter()
solutions = run(0, clases, carrera(clases),
)

end = perf_counter()

print(solutions)

execution_time = (end - start)
print(execution_time)