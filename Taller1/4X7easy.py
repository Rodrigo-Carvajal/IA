from logicpuzzles import *
# LINK del puzzle: https://logic.puzzlebaron.com/play.php?u2=9ac6ab228c029aad00f8d85f996319c5

# Descripción del caso
#El alcade planea arreglar las calles de la ciudad, para esto se debe determinar la calle, el presupuesto, el administrador y el mes que inicia la obra

#Obra = var1, var2, var3, var4
obra1 = ('April', var(), var(), var())
obra2 = ('May', var(), var(), var())
obra3 = ('June', var(), var(), var())
obra4 = ('July', var(), var(), var())
obra5 = ('August', var(), var(), var())
obra6 = ('September', var(), var(), var())
obra7 = ('October', var(), var(), var())
obras = (obra1, obra2, obra3, obra4, obra5, obra6, obra7)

#Dominio de atributos
    #mes = 'April', 'May', 'June', 'July', 'August', 'September', 'October'
    #calle = 'Clara street', 'Ethel street', 'Fred lane', 'Harkin drive', 'Juniper lane', 'Oak road', 'Shelly lane'
    #administrador = 'Al Anderson', 'Bill Bonner', 'Cal Craft', 'Dawn Daniels', 'Ed Erickson', 'Freda Fisher', 'Gail Garrett'
    #presupuesto = 15000, 18000, 20000, 28000, 32000, 35000 ,40000

#var(), var(), var(), var()

def funcion(obras):
    return lall(#(mes, calle administrador, presupuesto)
    #1. The Ethel Street project won't have a budget of $18,000.(mes, calle administrador, presupuesto)
        neq((var(), 'Ethel street', var(), 18000), obras),
    #2. The Shelly Lane project begins 1 month before Dawn Daniels's project.(mes, calle administrador, presupuesto)
        left_of(obras, (var(), 'Shelly lane', var(), var()), (var(), var(), 'Dawn Daniels', var())),
    #3. The Harkin Drive project will have a budget of $15,000.(mes, calle administrador, presupuesto)
        membero((var(), 'Harkin drive', var(), 15000), obras),
    #4. Of the Ethel Street project and Dawn Daniels's project, one will have a budget of $20,000 and the other starts in August.(mes, calle administrador, presupuesto)
    
    #5. Neither the job starting in July nor the Juniper Lane project is Cal Craft's project.(mes, calle administrador, presupuesto)        
        neq(('July', var(), 'Cal Craft', var()), obras),
        neq((var(), 'Juniper lane', 'Cal Craft', var()), obras),
        neq(('July', 'Juniper lane', 'Cal Craft', var()), obras),
    #6. The $40,000 project begins 1 month before the Fred Lane project.(mes, calle administrador, presupuesto)
        left_of(obras, (var(), var(), var(), 40000), (var(), 'Fred lane', var(), var())),
    #7. Of the job starting in September and the Oak Road project, one will be headed by Gail Garrett and the other will have a budget of $28,000.(mes, calle administrador, presupuesto)
    #8. The Shelly Lane project will be headed by Gail Garrett.(mes, calle administrador, presupuesto)
        membero((var(), 'Shelly lane', 'Gail Garrett', var()), obras),
    #9. The Harkin Drive project begins sometime after the Clara Street project.(mes, calle administrador, presupuesto)
        somewhat_right_of(obras, (var(), 'Harkin drive', var(), var()), (var(), 'Clara street', var(), var())),
    #10. The $32,000 project is either Ed Erickson's project or Bill Bonner's project.(mes, calle administrador, presupuesto)
        conde(
            (membero((var(), var(), 'Ed Erickson', 32000), obras), neq((var(), var(), 'Bill Bonner', var()), obras)),
            (membero((var(), var(), 'Bill Bonner', var()), obras), neq((var(), var(), 'Ed Erickson', 32000), obras))
        ),
    #11. The $32,000 project begins 2 months before the $35,000 project.(mes, calle administrador, presupuesto)
        left_of(obras, (var(), var(), var(), 32000), (var(), var(), var(), 35000), 2),
    #12. The Ethel Street project won't be managed by Al Anderson.(mes, calle administrador, presupuesto)
        neq((var(), 'Ethel street', 'Al Anderson', var()), obras),
    #13. Of the job starting in July and Ed Erickson's project, one will focus on Clara Street and the other will have a budget of $28,000.(mes, calle administrador, presupuesto)
    #14. The job starting in August won't be managed by Cal Craft.(mes, calle administrador, presupuesto)
        neq(('August', var(), 'Cal Craft', var()), obras),
    #n Datos no mencionados.(mes, calle administrador, presupuesto)
        
    )

solutions = run(0, obras, funcion(obras))
print(solutions)