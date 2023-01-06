import csv

documentation={}
#me llega un string que tiene la consulta cuando salga de este metodo lo que voy a obtener es las palabras relevantes
def exp_tokenization(expresion):
    pass

#me llegan las palabras relevantes y lo que hago es relacionarlas de izquierda a derecha
#la idea es la siguiente puedo hacer varias cosas

# 1 busco palabras principales como tumor u otra enfermedad
# si esta, busco si alguna de las otras palabras que se encuentran en la lista de la consulta forman una relacion, si es asi busco en la tabla de la base de datos y respondo,
# y despues busco las otras palabras para establecer una relacion con las que considero la palabra principal
#ejemplo: consulta: 'el tumor de pancrea que sintomas presenta y cual seria su tratamiento'
# primera relacion a buscar:tumor - organo - sintomas,
# segunda relacion a buscar: tumor - organo - tratamiento

#Algo importante en la pareja puede ser 3 cosas
# 1 Salga la palabra explicitamente es decir : 'sintomas', 'tratamiento', 'etapa'
# 2 Salga una instancia de sintoma o de tratamiento o de etapa, ejemplo: 'dolor de estomago'
# 3 Que salgan ambas cosas, ejemplo: 'sintomas como dolor de abdomen'

#busco en la tabla lo que necesito
# para el caso 1 lo que me interesa es el nombre de los sintomas que son mas frecuentes en esa enfermedad,
# es decir busco en la tabla de la enfermedad la combinacion de sintomass que tiene la mayor frecuencia relativa
# para el caso 2 lo que me interesa es devolver la probabilidad de la combinacion de los sintomas que me entraron
# caso 3 es la respuesta del caso 2

# Puede ocurrir que no exista palabras principales en la consulta como el nombre de la enfermedad
# en ese caso segun lo que me entren digase cualquier categoria solo o combinado
#solo: 'sintomas', 'tratamiento', 'etapa'
# en este caso lo que habria que buscar que enfermedad tiene estos sintomas(tratamiento o etapa) y con que probabilidad
#no es algo facil esta parte porque las tablas estan creadas a partir de las enfermedades con sus sintomas no al reves
#combinado:'sintomas-tratamiento', sintomas -etapa'
# en este caso se puede pensar tener una tabla o alguna relacion o hecho que relacione estas categorias



def exp_relacion(strings):
    pass

def buscar_tabla(pareja, dicc_enfermedad_parametro):
    if not pareja in documentation:
        pass
    else:
        #lista donde se guarda la informacion de los sintomas mas frecuentes
        lista=[]
        lista_parametro=[]
        lista_nombre_columnas=[]
        #guarda la maxima frecuencia que tiene la combinacion de sintomas
        max_frec=-1
        frec_acum=0
        nombre_doc=documentation[pareja]

        with open(nombre_doc, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                lenght=len(row)
                #if para actualizar la max_frec teniendo en cuenta que la primera fila es la que tiene los nombres de las columnas
                if not row[lenght-2] == 'fr_Enf':
                    #obtener el valor que tiene fr_Enf en esa fila
                    frec_actual=(int)(row[lenght-2])
                    # si mi max_frec es menor que la de la fila actual actualizo
                    if max_frec < frec_actual:
                        max_frec=frec_actual
                        lista=[]
                        #aqui agrego la combinacion de literales que tienen mas frecuencia relativa hasta ahora
                        for item in range(0,lenght-2):
                            lista.append(row[item])
                    #sumo todas las frecuencias para poder hallar la probabilidad al final
                    frec_acum+=frec_actual
                else:
                    #aqui agrego los nombre de los sintomas, tratamiento segun la pareja que sea
                    for item in range(0,lenght-2):
                        lista_nombre_columnas.append(row[item])
            #aqui cambio los literales que son positivos por el parametro que se esta evaluando digase sintomas, tratamiento blablabla
            for item in range(0,lenght-2):
                if lista[item] == '1':
                    lista_parametro.append(lista_nombre_columnas[item])

                    
            print(lista)
            print(lista_parametro)
            print("con probabilidad")
            print(max_frec/frec_acum)
                
    pass

def main():

    # with open('tumor_pancrea_sintomas.csv', 'w', newline='') as csvfile:
    #     fieldnames = ['sintoma1', 'sintoma2', 'sintoma3', 'fr_Enf','fr_no_Enf']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #     writer.writeheader()
    #     #Arreglar para agregar de forma dinamica a una tabla sintomas con sus respectivos valores
    #     writer.writerow({'sintoma1': '0', 'sintoma2': '0','sintoma3': '0', 'fr_Enf': 'n','fr_no_Enf': 'n'})
    #     writer.writerow({'sintoma1': '0', 'sintoma2': '0','sintoma3': '1', 'fr_Enf': 'n','fr_no_Enf': 'n'})
    #     writer.writerow({'sintoma1': '0', 'sintoma2': '1','sintoma3': '0', 'fr_Enf': 'n','fr_no_Enf': 'n'})
    #     writer.writerow({'sintoma1': '0', 'sintoma2': '1','sintoma3': '1', 'fr_Enf': 'n','fr_no_Enf': 'n'})
    #     writer.writerow({'sintoma1': '1', 'sintoma2': '0','sintoma3': '0', 'fr_Enf': 'n','fr_no_Enf': 'n'})
    #     writer.writerow({'sintoma1': '1', 'sintoma2': '0','sintoma3': '1', 'fr_Enf': 'n','fr_no_Enf': 'n'})
    #     writer.writerow({'sintoma1': '1', 'sintoma2': '1','sintoma3': '0', 'fr_Enf': 'n','fr_no_Enf': 'n'})
    #     writer.writerow({'sintoma1': '1', 'sintoma2': '1','sintoma3': '1', 'fr_Enf': 'n','fr_no_Enf': 'n'})

    documentation['tumor_pancrea_sintomas']='tumor_pancrea_sintomas.csv'
    documentation['tumor_pancrea_tratamientos']='tumor_pancrea_tratamientos.csv'
    documentation['tumor_pancrea_etapas']='tumor_pancrea_etapas.csv'
    
    buscar_tabla('tumor_pancrea_sintomas')

main()