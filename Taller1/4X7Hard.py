from logicpuzzles import *
#link: https://logic.puzzlebaron.com/play.php?u2=34df7d74038a4529bd3b62c583104ed4

# Hay 4 marineros que compitieron en dar una vuelta al mundo en la menor cantidad de días
marinero1 = (270, var(), var(), var())
marinero2 = (274, var(), var(), var())
marinero3 = (278, var(), var(), var())
marinero4 = (282, var(), var(), var())
marinero5 = (286, var(), var(), var())
marinero6 = (290, var(), var(), var())
marinero7 = (294, var(), var(), var())
marineros = (marinero1, marinero2, marinero3, marinero4, marinero5, marinero6, marinero7)

#nombre marinero = ['Debra Decker','Ed alexander','Gil Baxter','Neal Bundt','Tara Carroll','Vicky Estes','Wendell Orr']
#nombre de bote = ['Alpha one','Bay hawk','Confluence','Dream walker','Quick silver','Sea dart','Shady lady']
#tipo de bote = ['Catamaran','Gaff cutter','Ketch','Pilot cutter','Schooner','Sloop','Trimaran']

#var(), var(), var(), var()

#marinero = (dias, nombre marinero, nombre bote, tipo de bote)
def carrera(marineros):
  return lall(
    #1. The owner of the Dream Walker didn't use the pilot cutter.
    neq((var(), var(), 'Dream walker', 'Pilot cutter'), marineros),
    #2. The person who finished in 282 days sailed the Confluence.
    eq((282, var(), 'Confluence', var()), marinero4),
    #3. The competitor in the sloop took 4 fewer days to finish than Neal Bundt.
    left_of(marineros, (var(), var(), var(), 'Sloop'), ('Neal Bundt', var(), var(), var())),
    #4. The owner of the Quick Silver was either the sailor in the sloop or the competitor who finished in 282 days.
    lany(membero((var(), var(), 'Quick silver', 'Sloop'), marineros), eq((282, var(), 'Quick silver', var()), marinero4)),
    neq((282, var(), 'Quick silver', 'Sloop'), marineros),
    #5. Gil Baxter took 4 fewer days to finish than Debra Decker.
    left_of(marineros, (var(), 'Gil Baxter', var(), var()), (var(), 'Debra Decker', var(), var())),
    #6. Gil Baxter didn't sail the Bay Hawk.
    neq((var(), 'Gil Baxter', 'Bay hawk', var()), marineros),
    #7. Vicky Estes took 8 more days to finish than the owner of the Dream Walker.
    right_of(marineros, (var(), 'Vicky Estes', var(), var()), (var(), var(), 'Dream walker', var()), 2),
    #8. Ed Alexander was either the sailor in the gaff cutter or the owner of the Dream Walker.
    lany(membero((var(), 'Ed Alexander', var(), 'Gaff cutter'), marineros),membero((var(), 'Ed Alexander', 'Dream walker', var()), marineros)),
    neq((var(), 'Ed Alexander', 'Dream walker', 'Gaff cutter'), marineros),
    #9. Vicky Estes took 4 fewer days to finish than the sailor in the gaff cutter.
    left_of(marineros, (var(), 'Vicky Estes', var(), var()), (var(), var(), var(), 'Gaff cutter')),
    #11. The owner of the Shady Lady took 4 more days to finish than the person in the schooner.
    right_of(marineros, (var(), var(), 'Shady lady', var()), (var(), var(), var(), 'Schooner')),
    #12. The competitor who finished in 286 days sailed the Quick Silver.
    eq((286, var(), 'Quick silver', var()), marinero5),
    #13. Of the owner of the Confluence and the competitor who finished in 294 days, one used the ketch and the other was Wendell Orr.
    conde((eq((294, var(), var(), 'Ketch'),marinero7), membero((var(), 'Wendell Orr', 'Confluence', var()),marineros)), (eq((294, 'Wendell Orr', var(), var()),marinero7), membero((var(), var(), 'Confluence', 'Ketch'),marineros))),
    neq((294, 'Wendell Orr', 'Confluence', 'Ketch'), marineros),
    #14. Ed Alexander took somewhat more days to finish than the owner of the Shady Lady.
    somewhat_right_of(marineros, (var(), 'Ed Alexander', var(), var()), (var(), var(), 'Shady lady', var())),
    #15. Datos no mencionados
    membero((var(), 'Tara Carrol', var(), var()), marineros),
    membero((var(), var(), 'Alpha one', var()), marineros),
    membero((var(), var(), var(), 'Catamaran'), marineros),
  )
solutions = run(0, marineros, carrera(marineros),
                    #10. The competitor in the trimaran, the sailor who finished in 290 days, the competitor who finished in 274 days, the owner of the Sea Dart, the owner of the Dream Walker and Gil Baxter were all different people.
                    differents(marineros, ((274, 290,), ('Gil Baxter',), ('Sea dart', 'Dream walker',), ('Trimaran',)))
                )
print(solutions)
