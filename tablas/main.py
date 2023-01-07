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

def buscar_tabla(pareja, dicc_enfermedad_parametro, parametro):
    if not pareja in documentation:
        lista_filas=[]
        dicc_parametro_indice=[]
        filas_filtradas=[]
        dicc={}
        frec_acum=0


        for item in dicc_enfermedad_parametro.keys():
            nombre=item+'_'+parametro
            if nombre in documentation:
                with open(documentation[nombre], newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        lista_filas.append(row)
                        print(row)
                for var in dicc_enfermedad_parametro[item]:
                    if var in lista_filas[0]:
                        dicc_parametro_indice.append(var)
                    # for var1 in range(0,lista_filas[0]):
                    #     if var ==lista_filas[0][var1]:

                print(dicc_parametro_indice)

                for row in range(0, len(lista_filas)):
                    if not row == 0:
                        for var in range(0,len(lista_filas[row])-2):
                            #si el valor del parametro en fila, columna es = 1 y ese parametro se enuentra en los parametros que me interesa entonces guardo esa fila
                            if lista_filas[row][var] == '1' and lista_filas[0][var] in dicc_parametro_indice:
                                filas_filtradas.append(lista_filas[row])
                                break

                print(filas_filtradas)

                for filter_row in filas_filtradas:
                    dicc[str(filter_row)]=[]
                    lenght=len(filter_row)

                    frec_acum+=(int)(filter_row[lenght-2])

                    for para in range(0,len(filter_row)-2):
                        if filter_row[para]=='1':
                            dicc[str(filter_row)].append(lista_filas[0][para])

                for row in filas_filtradas:
                    print(dicc[str(row)])
                    print((int)(row[len(row)-2])/frec_acum)


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

def normalize(lista_palabras):
    word_list=[]
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "nn"),
    )
    for s in lista_palabras:
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        word_list.append(s)
    return word_list



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

    lista=['¡Hólá','múndó','pequeño']
    print(normalize(lista))
    # print(normalize("¡Hólá, múndó pequeño!"))
    # print(normalize("¡HÓLÁ, MÚNDÓ!"))

    documentation['tumor_pancrea_sintomas']='tumor_pancrea_sintomas.csv'
    documentation['tumor_pancrea_tratamientos']='tumor_pancrea_tratamientos.csv'
    documentation['tumor_pancrea_etapas']='tumor_pancrea_etapas.csv'

    dicc_enfermedad_parametro={}
    dicc_enfermedad_parametro['tumor_pancrea']=['sintoma1', 'sintoma2']

    
    buscar_tabla('tumor_ovarios_sintomas', dicc_enfermedad_parametro,'sintomas')

main()