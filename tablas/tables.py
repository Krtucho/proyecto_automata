import csv




def create_table(nombre_Enfermedad, sintomas):
    with open('nombre_Enfermedad.csv', 'w', newline='') as csvfile:
        fieldnames=[]
        for item in sintomas:
            fieldnames.append(item)
        fieldnames.append('fr_Enf')
        fieldnames.append('fr_no_Enf')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        #Arreglar para agregar de forma dinamica a una tabla sintomas con sus respectivos valores
        writer.writerow({'sintoma1': '0', 'sintoma2': '0','sintoma3': '0', 'fr_Enf': 'n','fr_no_Enf': 'n'})
        writer.writerow({'sintoma1': '0', 'sintoma2': '0','sintoma3': '1', 'fr_Enf': 'n','fr_no_Enf': 'n'})
        writer.writerow({'sintoma1': '0', 'sintoma2': '1','sintoma3': '0', 'fr_Enf': 'n','fr_no_Enf': 'n'})
        writer.writerow({'sintoma1': '0', 'sintoma2': '1','sintoma3': '1', 'fr_Enf': 'n','fr_no_Enf': 'n'})
        writer.writerow({'sintoma1': '1', 'sintoma2': '0','sintoma3': '0', 'fr_Enf': 'n','fr_no_Enf': 'n'})
        writer.writerow({'sintoma1': '1', 'sintoma2': '0','sintoma3': '1', 'fr_Enf': 'n','fr_no_Enf': 'n'})
        writer.writerow({'sintoma1': '1', 'sintoma2': '1','sintoma3': '0', 'fr_Enf': 'n','fr_no_Enf': 'n'})
        writer.writerow({'sintoma1': '1', 'sintoma2': '1','sintoma3': '1', 'fr_Enf': 'n','fr_no_Enf': 'n'})