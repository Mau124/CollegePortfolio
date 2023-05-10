#------------------------------------------------------------------------------------------------------------------
#   Project
#
#   Project for Omar
#
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------

import json
from kanren import Relation, facts, run, conde, var, eq, lany, unify, lall
from kanren.core import success, fail

#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------
    
# Define relations
Symptom = Relation()
PatientHas = Relation()

# Open symptoms 
with open('relationships.json') as file_relations:
    relations = json.loads(file_relations.read())

# Set facts
for item in relations['Sintoma']:
    facts(Symptom, (list(item.keys())[0], list(item.values())[0]))

facts(PatientHas, ('Juan', 'Ansiedad'), ('Juan', 'Inquieto'))

def Enfermedad(x, symptoms):
    rel = []
    for symptom in symptoms:
        print(run(0, x, Symptom(symptom, x)))
        rel.append(Symptom(symptom, x))

    return conde(*rel)

#------------------------------------------------------------------------------------------------------------------
#   Treatments 
#------------------------------------------------------------------------------------------------------------------

# Ansiedad
clauses.append(expr("Ansiedad(x) ==> Psicoterapia(x)"))
clauses.append(expr("Ansiedad(x) ==> DejarCafe(x)"))
clauses.append(expr("Ansiedad(x) & Psicoterapia(x) & NoFunciona(x) ==> Medicamentos(x)"))

# ADHD
clauses.append(expr("ADHD(x) ==> TomarAderall(x)"))

# Depresion
clauses.append(expr("Depresion(x) ==> Psicoterapia(x)"))

# Bipolaridad
clauses.append(expr("Bipolar(x) ==> Psicoterapia(x)"))


#Con sintoma
clauses.append(expr("SinDormir(x) ==> TomarMelatonina(x)"))
clauses.append(expr("NoOptimista(x) ==> Prozac(x)"))
clauses.append(expr("ActuarSinPensar(x) ==> TomarCursoEstadistica(x)"))
clauses.append(expr("Solo(x) ==> ComprarMascota(x)"))
clauses.append(expr("Culpable(x) ==> HablarMama(x)"))
clauses.append(expr("FaltaConcentracion(x) ==> TomarAderall(x)"))
clauses.append(expr("Inquieto(x) ==> TomarTe(x)"))
clauses.append(expr("HablasRapido(x) ==> TomarTe(x)"))

#------------------------------------------------------------------------------------------------------------------
#   Main Progam
#------------------------------------------------------------------------------------------------------------------
    
import pandas as pd
questions=pd.read_csv("cuestionario.csv")
respuestas=[]
cont=0
print("###########CUESTIONARIO PACIENTE###########")
print()
print("Nombre: ")
name = input()


for index,row in questions.iterrows():
    cont=cont+1
    respuesta=input(f'{cont}.{row["Pregunta"]}, S/N? ')

    if respuesta.upper() == 'S':
          respuestas.append((name, row['Respuesta']))


# def Ansiedad(x, z):
#     return conde(Symptom(x, z)) 

#     Patient(x, y) 
x = var()
Patient2 = Relation()  
facts(Patient2, *respuestas) 
symptomsJuan = run(0, x, Patient2(name, x))
print(symptomsJuan)
print(run(0, x, Enfermedad(x, symptomsJuan)))
