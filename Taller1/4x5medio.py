from logicpuzzles import *
from time import perf_counter
# LINK del puzzle: 

# Descripción del caso
#Se debe identificar a cada cada golista con su puntuación en el campo en cierto año que ganó

#golfistas = año, golfista, campo, puntaje
golfista1 = (1920, var(), var(), var())
golfista2 = (1921, var(), var(), var())
golfista3 = (1922, var(), var(), var())
golfista4 = (1923, var(), var(), var())
golfista5 = (1924, var(), var(), var())
golfistas = (golfista1, golfista2, golfista3, golfista4, golfista5)

#Dominio de atributos
    #año = 1920, 1921, 1922, 1923, 1924 
    #golfista = 'Alison Ames', 'Carrie Cole', 'Denise Diaz', 'Inez', 'Leslie Lane'
    #campo = 'Amble Glen', 'Cowbush Cove', 'Scotch Pines', 'Spotswood', 'Willow Grove'
    #puntaje = 59, 61, 65, 66, 67
#var(), var(), var(), var()
def golfista(golfistas):
    return lall(
        #1. Carrie Cole won her tournament 1 year after Inez. Cumple
            right_of(golfistas, (var(), 'Carrie Cole', var(), var()), (var(), 'Inez', var(), var())),        
        #4. The woman who won at Spotswood won her tournament sometime after Inez. Cumple
            somewhat_right_of(golfistas, (var(), var(), 'Spotswood', var()), (var(), 'Inez', var(), var())),
        #5. The golfer who scored a 59 won her tournament 3 years after the person who scored a 66. cumple
            right_of(golfistas, (var(), var(), var(), 59), (var(), var(), var(), 66), 3),        
        #7. Alison Ames was either the golfer who scored a 61 or the person who won at Willow Grove. Cumple
            lany(membero((var(), 'Alison Ames', var(), 61), golfistas), membero((var(), 'Alison Ames', 'Willow Grove', var()), golfistas)),
            neq((var(), 'Alison Ames', 'Willow Grove', 61), golfistas),
        #9. Leslie Lane won at Amble Glen. Cumple
            membero((var(), 'Leslie Lane', 'Amble Glen', var()), golfistas),
        #10. The golfer who won in 1923 won at Scotch Pines. Cumple
            eq((1923, var(), 'Scotch Pines', var()), golfista4),
        #n Datos no mencionados
            membero((var(), 'Denise Diaz', var(), var()), golfistas),
            membero((var(), var(), 'Cowbush Cove', var()), golfistas),
            membero((var(), var(), 'Willow Grove', var()), golfistas),
            membero((var(), var(), var(), 67), golfistas),
            membero((var(), var(), var(), 61), golfistas),
            membero((var(), var(), var(), 65), golfistas),
    )
start = perf_counter()
solutions = run(0, golfistas, golfista(golfistas),
                    #2. The person who won at Willow Grove didn't shoot a 66.
                        differents(golfistas, ((var(),), (var(),), ('Willow Grove',), (66,))),
                    #3. Leslie Lane didn't shoot a 65.
                        differents(golfistas, ((var(),), ('Leslie Lane',), (var(),), (65,))),
                    #6. The person who won in 1921 didn't win at Spotswood.
                        differents(golfistas, ((1921,), (var(),), ('Spotswood',), (var(),))),
                    #8. The five golfers were the golfer who won in 1922, Denise Detz, Carrie Cole, Leslie Lane and the person who scored a 66.
                        differents(golfistas, ((1922,), ('Denise Diaz', 'Carrie Cole', 'Leslie Lane'), (var(),), (66,)))
                )
end = perf_counter()
execution_time = (end - start)
print('Soluciones:', solutions)
print('Resuelto en (segundos):', execution_time)
