import pandas as pd
questions=pd.read_csv("cuestionario.csv")
respuestas=[]
cont=0
print("###########CUESTIONARIO PACIENTE###########")
print()

for index,row in questions.iterrows():
    cont=cont+1
    respuesta=input(f'{cont}.{row["Pregunta"]}, S/N? ')
    respuestas.append(respuesta)
