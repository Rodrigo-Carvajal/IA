from logicpuzzles import *
#Times, Estudiante, Elementos, Colores
objeto1 = (10,var(), var(), var())
objeto2 = (15,var(), var(), var())
objeto3 = (20,var(), var(), var())
objeto4 = (25,var(), var(), var())
objeto5 = (30,var(), var(), var())
objetos = (objeto1, objeto2, objeto3, objeto4, objeto5)

def impresoraproblem(objetos):
    return lall(  
      #1 Color naranjo era la copa
      membero((var(), var(), 'Copa', 'Naranjo'), objetos),
      
      #2 La carcasa, la pieza azul y lo imprimido en 15min son 3 elementos diferentes
      membero((var(),var(), 'Carcasa', var()), objetos), membero((var(),var(), var(), 'Azul'), objetos), membero((15,var(), var(), var()), objetos),
      
      
      #3 Diseño se imprimio en 10min y diseño amarillo, uno era de Virgil y otro de Felicia
      conde((eq((10, 'Virgilio', var(), var()), objeto1), membero((var(), 'Felicia', var(), 'Amarillo'), objetos)),
            (membero((var(), 'Virgilio', var(), 'Amarillo'), objetos), eq((10, 'Felicia', var(), var()), objeto1))),      
      
      #4 La pieza roja era de Willis o el diseño que se imprimio en 10min
      lany(membero((var(), 'Willis', var(), 'Rojo'), objetos), eq((10, var(), var(), 'Rojo'), objeto1)),
      neq((10, 'Willis', var(), 'Rojo'), objetos),
      
      #5 El diseño azul tardo 5min más en imprimirse que el de Willis
      right_of(objetos, (var(), var(), var(), 'Azul'), (var(), 'Willis', var(), var())),
      
      #6 El diseño de Hilda tardó 5 min más en imprimirse que el casco
      right_of(objetos, (var(), 'Hilda', var(), var()), (var(), var(), 'Casco', var())),
      
      #7 La pieza de Virgil y la pieza de Hilda, una era el silbato y la otra era naranja.
      conde((membero((var(), 'Virgilio', 'Silbato', var()), objetos), membero((var(), 'Hilda', var(), 'Naranjo'), objetos)),
            (membero((var(), 'Virgilio', var(), 'Naranjo'), objetos), membero((var(), 'Hilda', 'Silbato', var()), objetos))),
      
      #8 El diseño amarillo requirio 5min menos para imprimirse que el diseño morado.
      left_of(objetos, (var(), var(), var(), 'Amarillo'), (var(), var(), var(), 'Morado')),
      
      #9 La pieza que imprimió en 20min fue amarilla.
      eq((20, var(), var(), 'Amarillo'), objeto3),
    )

solucion = run(0, objetos, impresoraproblem(objetos))
print(solucion)