from matplotlib.cbook import ls_mapper
from utils import *
from logic import *

import pandas as pd
import os

clauses=[]

#------------------------------------------------------------------------------------------------------------------
#   Knowledge base 
#------------------------------------------------------------------------------------------------------------------

# Ansiedad

clauses.append(expr("ExcesivaPreocupacion(x) ==> Enfermo(x, Ansiedad)"))
clauses.append(expr("Peligro(x) ==> Enfermo(x, Ansiedad)"))

# Instanciacion existencial

clauses.append(expr("SinDormir(M1)"))
clauses.append(expr("Enfermo(M1, Ansiedad)"))

clauses.append(expr("FaltaConcentracion(M2)"))
clauses.append(expr("Enfermo(M2, Ansiedad)"))

clauses.append(expr("Inquieto(M3)"))
clauses.append(expr("Enfermo(M3, Ansiedad)"))

# ADHD

clauses.append(expr("Olvidadizo(x) ==> Enfermo(x, ADHD)"))
clauses.append(expr("Desorganizado(x) ==> Enfermo(x, ADHD)"))
clauses.append(expr("Peligro(x) ==> Enfermo(x, ADHD)"))

# Instanciacion existencial

clauses.append(expr("Inquieto(M4)"))
clauses.append(expr("Enfermo(M4, ADHD)"))

clauses.append(expr("Culpable(M5)"))
clauses.append(expr("Enfermo(M5, ADHD)"))

clauses.append(expr("SinPensar(M6)"))
clauses.append(expr("Enfermo(M6, ADHD)"))

# Depresion

clauses.append(expr("Suicida(x) ==> Enfermo(x, Depresion)"))
clauses.append(expr("AutoestimaBaja(x) ==> Enfermo(x, Depresion)"))

# Instanciacion existencial

clauses.append(expr("NoOptimista(M7)"))
clauses.append(expr("Enfermo(M7, Depresion)"))

clauses.append(expr("Culpable(M8)"))
clauses.append(expr("Enfermo(M8, Depresion)"))

clauses.append(expr("Solo(M9)"))
clauses.append(expr("Enfermo(M9, Depresion)"))

# Bipolaridad

clauses.append(expr("Enfermo(x, Depresion) & Enfermo(x, ADHD) ==> Enfermo(x, Bipolar)"))
clauses.append(expr("CambiosRepentinosHumor(x) ==> Enfermo(x, Bipolar)"))
clauses.append(expr("Inquieto(x) & HablasRapido(x) & SinSentidoPeligro(x) ==> Sintoma(x, Episodio_Maniaco)"))
clauses.append(expr("Sintoma(x, Episodio_Maniaco) & Enfermo(x, Depresion)==> Enfermo(x, Bipolar)"))
clauses.append(expr("Sintoma(x, Hipomania) & Enfermo(x, Depresion)==> Enfermo(x, Bipolar)"))

# Instanciacion existencial

clauses.append(expr("Episodio_Maniaco(M10)"))
clauses.append(expr("Enfermo(M10, Bipolar)"))

#------------------------------------------------------------------------------------------------------------------
#   Treatments 
#------------------------------------------------------------------------------------------------------------------

# Ansiedad
clauses.append(expr("Enfermo(x,Ansiedad) ==> Tratamiento(x,Psicoterapia)"))
clauses.append(expr("Enfermo(x, Ansiedad)  ==> Tratamiento(x,DejarCafe)"))
clauses.append(expr("Enfermo(x, Ansiedad) & Psicoterapia(x) & NoFunciona(x) ==> Tratamiento(x,Medicamentos)"))

# ADHD
clauses.append(expr("Enfermo(x, ADHD) ==> Tratamiento(x,TomarAderall)"))

# Depresion
clauses.append(expr("Enfermo(x, Depresion) ==> Tratamiento(x,Psicoterapia)"))

# Bipolaridad
clauses.append(expr("Enfermo(x, Bipolar) ==> Tratamiento(x,Psicoterapia)"))


#Con sintoma
clauses.append(expr("SinDormir(x) ==> Tratamiento(x,TomarMelatonina)"))
clauses.append(expr("NoOptimista(x) ==> Tratamiento(x,TomarProzac)"))
clauses.append(expr("ActuarSinPensar(x) ==> Tratamiento(x,TomarCursoEstadistica)"))
clauses.append(expr("Solo(x) ==> Tratamiento(x,ComprarMascota)"))
clauses.append(expr("Culpable(x) ==> Tratamiento(x,HablarMama)"))
clauses.append(expr("FaltaConcentracion(x) ==> Tratamiento(x,TomarAderall)"))
clauses.append(expr("Inquieto(x) ==> Tratamiento(x,TomarTe)"))
clauses.append(expr("HablasRapido(x) ==> Tratamiento(x,TomarTe)"))



example = FolKB(clauses)


#------------------------------------------------------------------------------------------------------------------
#   Dictionary for treatments
#------------------------------------------------------------------------------------------------------------------

treatments_formated = {'Psicoterapia': 'Psicoterapia (Consultar un médico para mas información)',
                        'DejarCafe': 'Dejar de tomar cafe si lo hace ayudara con sus ataques de ansiedad',
                        'TomarAderall': 'Se le recomienda tomar el medicamento Aderall',
                        'TomarMelatonina': 'Se le recomienda tomar melatonina',
                        'TomarCursoEstadistica': 'Tome algun curso de estadistica para que ya no actue sin pensar',
                        'TomarProzac': 'Tome Prozac',
                        'ComprarMascota': 'Comprese una mascota',
                        'HablarMama': 'Hablele a su mama',
                        'TomarTe': 'Tome un te para que se relaje'}

#------------------------------------------------------------------------------------------------------------------
#   Main Progam
#------------------------------------------------------------------------------------------------------------------
    
import pandas as pd
questions=pd.read_csv("cuestionario.csv")
respuestas=[]
print('|-----------------------------------------------------------------------|')
print('|                                                                       |')
print('|                       Cuestionario paciente                           |')
print('|                                                                       |')
print('|-----------------------------------------------------------------------|')
print()
print("Nombre: ")
name = input()
name = name[0].upper()


for index,row in questions.iterrows():
    respuesta = ''

    while respuesta.upper() != 'S' and respuesta.upper() != 'N':
        os.system('cls')
        respuesta=input(f'{index+1}.{row["Pregunta"]}, S/N s/n? ')
        if respuesta.upper() == 'S':
            example.tell(expr(f'{row.iloc[-1]}({name})'))
        elif respuesta.upper() != 'N':
            print('La respuesta no esta correctamente escrita. Revise de nuevo')
            aux = input('Presione enter')

# Ask
diseases = fol_fc_ask(example, expr(f'Enfermo({name}, y)'))
treatments = fol_fc_ask(example, expr(f'Tratamiento({name}, y)'))

diseases= list(diseases)
treatments = list(treatments)

os.system('cls')

print('|-----------------------------------------------------------------------|')
print('|                                                                       |')
print('|                             Diagnosis                                 |')
print('|                                                                       |')
print('|-----------------------------------------------------------------------|')
#   Main Progam
#------------------------------------------------------------------------------------------------------------------


if len(diseases) == 0:
    print('Se necesita mas informacion para dar un diagnostico correcto')
    print()

    list_treatments = []

    for item in treatments:
        list_treatments.append(treatments_formated[f'{item.get(y)}'])

    for item in list(set(list_treatments)):
        print(item)

    if len(list_treatments)>0:
        print('\nLos tratamientos para los sintomas de esta enfermedad son:')
        print()
        
        for item in list(set(list_treatments)):
            print(item)


elif len(diseases) == 1:
    print('La enfermedad que usted presenta es: ')
    print()

    for item in diseases:
        print(item.get(y))

    list_treatments = []

    for item in treatments:
        list_treatments.append(treatments_formated[f'{item.get(y)}'])
    
    if len(list_treatments)>0:
        print('\nLos tratamientos para los sintomas de esta enfermedad son:')
    
        for item in list(set(list_treatments)):
            print(item)

else:
    print('Sus sintomas concuerdan con mas de una enfermedad ')
    print('Las posbibles enfermedades que usted presenta son:')
    print()

    list_diseases = []
    for item in diseases:
        list_diseases.append(item.get(y))

    for item in list(set(list_diseases)):
        print(item)

    print('\nSe recomienda ir con un medico para un diagnostico mas exacto')
    print()

    list_treatments = []
    for item in treatments:
       list_treatments.append(treatments_formated[f'{item.get(y)}'])
    if len(list_treatments)>0:
        print('\nLos tratamientos para los sintomas de esta enfermedad son:')
        print()
        
        for item in list(set(list_treatments)):
            print(item)