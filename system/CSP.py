from hospital_class import *
import copy





#Ejemplo 1 ------------------------------------------------

# doctor1=Doctor("pancrea", 10, None, "Doctor1", 1)
# doctor2=Doctor("General", 10, None, "Doctor2", 2)
# doctor3=Doctor("ovario", 10, None, "Doctor3", 3)
# doctor4=Doctor("General", 10, None, "Doctor4", 4)
# doctor5=Doctor("cerebro", 10, None, "Doctor5", 5)

# aparato1=Apparatus("pancrea", "AparatoP", 1)
# aparato2=Apparatus("X-Ray", 2)
# aparato3=Apparatus("X-Ray", 3)
# aparato4=Apparatus("ovario", "AparatoO1", 4)
# aparato5=Apparatus("ovario", "AparatoO2", 5)

# aparato1=Apparatus("AparatoP", 1)
# aparato2=Apparatus("X-Ray", 2)
# aparato3=Apparatus("X-Ray", 3)
# aparato4=Apparatus("AparatoO1", 4)
# aparato5=Apparatus("AparatoO2", 5)

# paciente1=Pacient(None, None, ["pancrea"], "1")
# paciente2=Pacient("pancrea", "X-Ray", None, "2")
# paciente3=Pacient(None, None, ["cerebro"], "3")
# paciente4=Pacient(None, None, ["ovario"],"4")
# paciente5=Pacient("ovario", "AparatoO1", None, "5")

#---------------------------------------------------------------------

#Ejemplo 2 ---------------------------------------------------

# doctor1=Doctor("pancrea", 10, None, "Doctor1", 1)
# doctor2=Doctor("pancrea", 10, None, "Doctor2", 2)
# doctor3=Doctor("pancrea", 10, None, "Doctor3", 3)
# doctor4=Doctor("cerebro", 10, None, "Doctor4", 4)
# doctor5=Doctor("General", 10, None, "Doctor5", 5)
# doctor6=Doctor("General", 10, None, "Doctor6", 6)
# doctor7=Doctor("ovario", 10, None, "Doctor7", 7)
# doctor8=Doctor("ovario", 10, None, "Doctor8", 8)
# doctor9=Doctor("ovario", 10, None, "Doctor9", 9)

# aparato1=Apparatus("AparatoP", 1)
# aparato2=Apparatus("AparatoP", 2)
# aparato3=Apparatus("X-Ray", 3)
# aparato4=Apparatus("X-Ray", 4)
# aparato5=Apparatus("X-Ray", 5)
# aparato6=Apparatus("X-Ray", 6)
# aparato9=Apparatus("X-Ray", 9)
# aparato7=Apparatus("AparatoO1", 7)
# aparato8=Apparatus("AparatoO2", 8)


# paciente1=Pacient(None, None, ["pancrea"], "1")
# # paciente2=Pacient("pancrea", "X-Ray", None, "2")
# paciente3=Pacient(None, None, ["cerebro"], "3")
# paciente4=Pacient(None, None, ["ovario"],"4")
# paciente5=Pacient("ovario", "AparatoO1", None, "5")

# paciente6=Pacient(None, None, ["pancrea"], "6")
# paciente7=Pacient("pancrea", "AparatoP", None, "7")
# paciente8=Pacient("cerebro", "X-Ray", None, "8")
# paciente9=Pacient(None, None, ["ovario"],"9")
# paciente10=Pacient("ovario", "AparatoO2", None, "10")


#---------------------------------------------------------------------

#Ejemplo 3 ---------------------------------------------------

# doctor1=Doctor("pancrea", 10, None, "Doctor1", 1)
# doctor2=Doctor("pancrea", 10, None, "Doctor2", 2)
# doctor3=Doctor("pancrea", 10, None, "Doctor3", 3)
# doctor4=Doctor("cerebro", 10, None, "Doctor4", 4)
# doctor5=Doctor("General", 10, None, "Doctor5", 5)
# doctor6=Doctor("General", 10, None, "Doctor6", 6)
# doctor7=Doctor("ovario", 10, None, "Doctor7", 7)
# doctor8=Doctor("ovario", 10, None, "Doctor8", 8)
# doctor9=Doctor("ovario", 10, None, "Doctor9", 9)


# aparato1=Apparatus("AparatoP", 1)
# aparato2=Apparatus("AparatoP", 2)
# aparato3=Apparatus("X-Ray", 3)
# aparato4=Apparatus("X-Ray", 4)
# aparato5=Apparatus("X-Ray", 5)
# aparato6=Apparatus("X-Ray", 6)
# aparato9=Apparatus("X-Ray", 9)
# aparato7=Apparatus("AparatoO1", 7)
# aparato8=Apparatus("AparatoO2", 8)


# paciente1=Pacient(None, None, ["pancrea", "ovario"], "1")
# # paciente2=Pacient("pancrea", "X-Ray", None, "2")
# paciente3=Pacient(None, None, ["cerebro"], "3")
# paciente4=Pacient(None, None, ["ovario", "cerebro"],"4")
# paciente5=Pacient("ovario", "AparatoO1", None, "5")

# paciente6=Pacient(None, None, ["pancrea"], "6")
# paciente7=Pacient("pancrea", "AparatoP", None, "7")
# paciente8=Pacient("cerebro", "X-Ray", None, "8")
# paciente9=Pacient(None, None, ["ovario"],"9")
# paciente10=Pacient("ovario", "AparatoO2", None, "10")


#---------------------------------------------------------------------

#Ejemplo 4 ---------------------------------------------------

doctor1=Doctor("pancreas", 10, None, "Doctor1", 1)
# doctor2=Doctor("pancreas", 10, None, "Doctor2", 2)
# doctor3=Doctor("pancrea", 10, None, "Doctor3", 3)
doctor4=Doctor("cerebro", 10, None, "Doctor4", 4)
# doctor5=Doctor("General", 10, None, "Doctor5", 5)
# doctor6=Doctor("General", 10, None, "Doctor6", 6)
# doctor7=Doctor("ovario", 10, None, "Doctor7", 7)
# doctor8=Doctor("ovarios", 10, None, "Doctor8", 8)
# doctor9=Doctor("ovario", 10, None, "Doctor9", 9)
# doctor10=Doctor("pancrea", 10, None, "Doctor10", 10)
# doctor11=Doctor("pancrea", 10, None, "Doctor11", 11)

# doctor11.available=False

# aparato1=Apparatus("AparatoP", 1)
# aparato2=Apparatus("AparatoP", 2)
# aparato3=Apparatus("X-Ray", 3)
# aparato4=Apparatus("X-Ray", 4)
# aparato5=Apparatus("X-Ray", 5)
# # aparato6=Apparatus("X-Ray", 6)
# aparato9=Apparatus("X-Ray", 9)
# aparato7=Apparatus("AparatoO", 7)
# aparato8=Apparatus("AparatoO2", 8)
# aparato9= Cirugia("pancrea",9,5,0)

aparato1=Apparatus("AparatoP", 1)
# aparato2=Apparatus("AparatoP", 2)
aparato3=Apparatus("X-Ray", 3)
# aparato4=Apparatus("X-Ray", 4)
# aparato5=Apparatus("X-Ray", 5)
# aparato6=Apparatus("X-Ray", 6)
# aparato9=Apparatus("X-Ray", 9)
# aparato7=Apparatus("AparatoO", 7)


# paciente1=Pacient(None, None, ["pancrea", "ovario"], "1")
# paciente2=Pacient("pancrea", "Cirugia", None, "2")
# paciente3=Pacient(None, None, ["cerebro"], "3")
# paciente4=Pacient(None, None, ["ovario", "cerebro"],"4")
# paciente5=Pacient("ovario", "AparatoO1", None, "5")

# paciente6=Pacient(None, None, ["pancrea"], "6")
# paciente7=Pacient("pancrea", "AparatoP", None, "7")
# paciente8=Pacient("cerebro", "X-Ray", None, "8")
# paciente9=Pacient(None, None, ["ovario"],"9")
# paciente10=Pacient("ovario", "AparatoO2", None, "10")


#---------------------------------------------------------------------

#-----------------------------Rellenar las listas necesarias ---------------------------------------------------------------------------------

# pacientes=[paciente1, paciente2, paciente7, paciente3, paciente4, paciente5, paciente6, paciente8, paciente9, paciente10]
# doctors=[doctor1, doctor2, doctor3, doctor4, doctor5, doctor6, doctor7, doctor8, doctor9, doctor10, doctor11]
# aparatos=[aparato1, aparato2, aparato3, aparato4, aparato5, aparato6, aparato7, aparato8, aparato9]

doctors=[doctor1, doctor4]
aparatos=[aparato1, aparato3]


rel_terapia_aparato={}
rel_terapia_aparato[("pancreas", "quimioterapia")]="AparatoP"
rel_terapia_aparato[("mama", "quimioterapia")]="AparatoM"
rel_terapia_aparato[("ovarios", "quimioterapia")]="AparatoO"
rel_terapia_aparato[(None, "suero")]="Suero"
rel_terapia_aparato[(None, "radioterapia")]="X-Ray"

number_pacients=10
number_of_doctors=10
number_of_apparatus=9


enfermedad_dicc={"pancreas":Solution(), "ovarios":Solution(), "cerebro":Solution(), "mama":Solution(), "higado":Solution(), "rinnones":Solution(), "piel":Solution(), "traquea":Solution(),
"nariz":Solution(), "esofago":Solution(), "laringe":Solution(), "tiroides":Solution(), "testiculos":Solution()}
terapias_dicc={"pancreas":Solution(), "ovarios":Solution(), "cerebro":Solution(), "mama":Solution(), "higado":Solution(), "rinnones":Solution(), "piel":Solution(), "traquea":Solution(),
"nariz":Solution(), "esofago":Solution(), "laringe":Solution(), "tiroides":Solution(), "testiculos":Solution()}

enfermedad_dicc["pancreas"].apparatus.append(aparato1)
# enfermedad_dicc["pancreas"].apparatus.append(aparato2)
# enfermedad_dicc["ovarios"].apparatus.append(aparato7)
# enfermedad_dicc["ovario"].apparatus.append(aparato8)

# terapias_dicc["ovarios"].apparatus.append(aparato7)
# terapias_dicc["ovario"].apparatus.append(aparato8)
terapias_dicc["pancreas"].apparatus.append(aparato1)
# terapias_dicc["pancreas"].apparatus.append(aparato2)

cirugias={}
cirugias["ovarios"]=9
cirugias["pancreas"]=5
cirugias["cerebro"]=12

#-----------------------------------Agregar los doctores al diccionario de enfermedades y terapias----------------------------------------------

for doctor in doctors:
    if doctor.specialty == 'General':
        for terapia in terapias_dicc.keys():
            if not doctor in terapias_dicc[terapia].doctors:
                terapias_dicc[terapia].doctors.append(doctor)
    else:
        if not doctor in terapias_dicc[doctor.specialty].doctors and not doctor in enfermedad_dicc[doctor.specialty].doctors:
            enfermedad_dicc[doctor.specialty].doctors.append(doctor)
            terapias_dicc[doctor.specialty].doctors.append(doctor)

#-------------------------------------------------------------------------------------------------------------------------------------------------

print("Despues de agregar doctores")
print(enfermedad_dicc)
print(terapias_dicc)

#--------------------------------------Agregar los aparatos al diccionario de enfermedades y terapias-----------------------------------------------
for aparato in aparatos:
    if aparato.name == "X-Ray":
        for item in enfermedad_dicc.keys():
            if not aparato in enfermedad_dicc[item].apparatus and not aparato in terapias_dicc[item].apparatus:
                enfermedad_dicc[item].apparatus.append(aparato)
                terapias_dicc[item].apparatus.append(aparato)
    elif aparato.name == "Quimioterapia" or aparato.name == "Radioterapia" or aparato.name == "Cirugia" or aparato.name == "Cuidados paliativos":
        for terapia in terapias_dicc.keys():
            if not aparato in terapias_dicc[terapia].apparatus:
                terapias_dicc[terapia].apparatus.append(aparato)
#---------------------------------------------------------------------------------------------------------------------------------------------------

print("Despues de agregar aparatos")
print(enfermedad_dicc)
print(terapias_dicc)

#-----------------------------------Llenar el diccionario pacientes_rel_doct_sala_apar-------------------------------------------
def fill_dicc(pacientes_list, pac_rel_doct_sala_apar_dicc, cirugias, aparatos):
    for paciente in pacientes_list:

        pac_rel_doct_sala_apar_dicc[paciente]=Solution()
        temp=pac_rel_doct_sala_apar_dicc[paciente]

        if not paciente.type_tumor == None:
            for doctor in terapias_dicc[paciente.type_tumor].doctors:
                if doctor.available:
                    temp.doctors.append(doctor)
            if paciente.therapies_receiving == "Cirugia":
                aparato_cir=Cirugia(paciente.type_tumor,len(aparatos)+1 ,cirugias[paciente.type_tumor],0)
                aparatos.append(aparato_cir)
                temp.apparatus.append(aparato_cir)
            else:
                for aparato in terapias_dicc[paciente.type_tumor].apparatus:
                    if aparato.available:
                        if paciente.therapies_receiving == "radioterapia" or paciente.therapies_receiving == "suero":
                            if aparato.name == rel_terapia_aparato[( None, paciente.therapies_receiving)]:
                                temp.apparatus.append(aparato)
                        elif aparato.available and aparato.name == rel_terapia_aparato[(paciente.type_tumor,paciente.therapies_receiving)]:
                            temp.apparatus.append(aparato)
        else:
            for tumor in paciente.possibles_tumors:
                if tumor in enfermedad_dicc:
                    for doctor in enfermedad_dicc[tumor].doctors:
                        if doctor.available and not doctor in temp.doctors:
                            temp.doctors.append(doctor)
                    for aparato in enfermedad_dicc[tumor].apparatus:
                        if aparato.available and not aparato in temp.apparatus:
                            temp.apparatus.append(aparato)
    return aparatos, pac_rel_doct_sala_apar_dicc

#---------------------------------------------------------------------------------------------------------------------------------------------

# print("Pacientes")
# print(pacientes)



# print(doctors_graph)
# print(aparatos_graph)

#------------------------------------Crear los grafos----------------------------------------------------------------------------------------------
def fill_graph(pacientes_list, doctores):
    doctors_graph=Graph(pacientes_list)
    aparatos_graph=Graph(pacientes_list)
    for paciente1 in pacientes_list:
        for paciente2 in pacientes_list:
            if not paciente1.name == paciente2.name:
                if not paciente1.type_tumor == None and not paciente2.type_tumor == None:

                    if paciente1.type_tumor == paciente2.type_tumor:
                        doctors_graph.insert(paciente1, paciente2)
                        # aparatos_graph.insert(paciente1, paciente2)
                    elif paciente1.therapies_receiving == paciente2.therapies_receiving:
                        aparatos_graph.insert(paciente1, paciente2)
                        doctor_general=[item for item in doctores if item.specialty == "General"]
                        if len(doctor_general) > 0:
                            doctors_graph.insert(paciente1, paciente2)
                    # else:
                    # doctors_graph.insert(paciente1, paciente2)

                elif not paciente1.type_tumor == None and not paciente2.possibles_tumors == None:
                    if paciente1.type_tumor in paciente2.possibles_tumors:
                        doctors_graph.insert(paciente1, paciente2)
                        aparatos_graph.insert(paciente1, paciente2)
                    else:
                        aparatos_graph.insert(paciente1, paciente2)

                elif not paciente1.possibles_tumors == None and not paciente2.type_tumor == None:
                    if paciente2.type_tumor in paciente1.possibles_tumors:
                        doctors_graph.insert(paciente1, paciente2)
                        aparatos_graph.insert(paciente1, paciente2)
                    else:
                        aparatos_graph.insert(paciente1, paciente2)

                elif not paciente1.possibles_tumors == None and not paciente2.possibles_tumors == None:
                    for tumor1 in  paciente1.possibles_tumors:
                        if tumor1 in paciente2.possibles_tumors:
                            doctors_graph.insert(paciente1, paciente2)
                            aparatos_graph.insert(paciente1, paciente2)
                            break
    return doctors_graph, aparatos_graph

#---------------------------------------------------------------------------------------------------------------------------------------------

# print(doctors_graph)
# print(aparatos_graph)

#-------------------------------------Ordenar las aristas por los que tienen mayor o menor dominio-----------------------------------------------

def edge_sort(grafo, tipo, rel_dicc):
    nodes_sort=grafo.nodes.copy()
    for i in range(0,len(grafo.nodes)):
        for j in range(0,len(grafo.nodes)):
            node1=nodes_sort[i]
            node2=nodes_sort[j]
            if tipo == "doctors":
                if len(rel_dicc[node1].doctors) < len(rel_dicc[node2].doctors):
                    # node=nodes_sort[i]
                    nodes_sort[i]=node2
                    nodes_sort[j]=node1
            else:
                if len(rel_dicc[node1].apparatus) < len(rel_dicc[node2].apparatus):
                    # node=nodes_sort[i]
                    nodes_sort[i]=node2
                    nodes_sort[j]=node1

    edges_sort=[]
    for node in nodes_sort:
        for edge in grafo.edges:
            if edge.node1.name == node.name and not edge in edges_sort:
                edges_sort.append(edge)
    return edges_sort

#---------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------Metodos utiles--------------------------------------------------------------------------------
def domain(x_i, domain_type="doctors"):
    if domain_type == "doctors":
        return pacientes_rel_doct_sala_apar[x_i].doctors
    elif domain_type == "aparatos":
        return pacientes_rel_doct_sala_apar[x_i].apparatus

def check_domain(pacient_dicc):
    for item in pacient_dicc.values():
        if item.doctors == []:
            return False
    return True

def delete_from_domain(x_i, x, domain_type="doctors"):
    if domain_type=="doctors":
        solution:list = pacientes_rel_doct_sala_apar[x_i].doctors
        solution.remove(x)
    elif domain_type=="aparatos":
        solution:list = pacientes_rel_doct_sala_apar[x_i].apparatus
        solution.remove(x)

def remove_inconsistent_values(x_i, x_j, domain_type="doctors"): # returns true iff succeeds
    removed = False
    dom=domain(x_i, domain_type=domain_type).copy()
    for x in dom:
        if x in domain(x_j, domain_type=domain_type):
            delete_from_domain(x_i, x, domain_type=domain_type)
            removed = True
    return removed

def neighbors(x_i, tipo, graph):
    if tipo == "doctors":
        return graph.neighbors(x_i)
    else:
        return graph.neighbors(x_i)


def actualizar_dominio(paciente1, item1, tipo, pacient_dicc):
    pacient_dicc_copy=pacient_dicc.copy()

    for paciente in pacient_dicc_copy:
        lists=[]
        lists_copy=[]

        if tipo == "doctors":
            lists=pacient_dicc_copy[paciente].doctors
        else:
            lists=pacient_dicc_copy[paciente].apparatus

        lists_copy=lists.copy()

        for item in lists_copy:
            if paciente.name == paciente1.name:
                if tipo == "doctors" and not item.id == item1.id:
                    pacient_dicc[paciente].doctors.remove(item)
                elif tipo == "aparatos" and not item.id == item1.id:
                    pacient_dicc[paciente].apparatus.remove(item)
            else:
                if tipo == "doctors" and item.id == item1.id:
                    pacient_dicc[paciente].doctors.remove(item)
                elif tipo == "aparatos" and item.id == item1.id:
                    pacient_dicc[paciente].apparatus.remove(item)

def valid_solution(pacient_dicc):
    for solution in pacient_dicc.values():
        if not len(solution.doctors) == 1 or not len(solution.apparatus) == 1:
            return False
    return True
def valid_solution_doctors(pacient_dicc, doctores):
    for doctor in doctores:
        doctor_count=0
        for solution in pacient_dicc.values():
            doctores_sol=[item for item in solution.doctors if item.id==doctor.id]
            if len(doctores_sol)>0:
                doctor_count+=1
        if doctor_count > 1:
            return False
    for solution in pacient_dicc.values():
        if not len(solution.doctors) == 1:
            return False
    return True

def valid_solution_apparatus(pacient_dicc, aparatos):
    for aparato in aparatos:
        aparato_count=0
        for solution in pacient_dicc.values():
            aparatos_sol=[item for item in solution.apparatus if item.id==aparato.id]
            if len(aparatos_sol)>0:
                aparato_count+=1
        if aparato_count > 1:
            return False
    for solution in pacient_dicc.values():
        if not len(solution.apparatus) == 1:
            return False
    return True

def doctores_aparatos_no_repetidos(lista, tipo, csp):
    for item in lista:
        count=0
        for sol in csp.values():
            if tipo == "doctors":
                if len(sol.doctors) == 1 and sol.doctors[0].id==item.id:
                    count+=1
            else:
                if len(sol.apparatus) == 1 and sol.apparatus[0].id==item.id:
                    count+=1
        if count > 1:
            return False
    return True

#-----------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------Metodo principal-----------------------------------------------------------------------------
def ac_3(csp, doctors_queue, aparatos_queue, pacient_dicc, list_marks_doctors, list_marks_aparatos, doctors_graph, aparatos_graph, doctores_list, aparatos_list): # returns the CSP, posibly with reduced domains

    
    while len(doctors_queue) > 0 or len(aparatos_queue) > 0:

        if not valid_solution_doctors(csp, doctores_list) and len(doctors_queue) > 0:
            edge = doctors_queue.pop()
            
            x_i = edge.node1
            x_j = edge.node2

            if not x_i in pacient_dicc:
                x_i=[item for item in pacient_dicc.keys() if item.name == x_i.name]
                x_i=x_i[0]
            if not x_j in pacient_dicc:
                x_j=[item for item in pacient_dicc.keys() if item.name == x_j.name]
                x_j=x_j[0]

            doctors1=pacient_dicc[x_i].doctors.copy()
            doctors2=pacient_dicc[x_j].doctors.copy()

            value1=[item for item in csp.keys() if item.name == x_i.name ]
            value2=[item for item in csp.keys() if item.name == x_j.name ]
            
            doctors1_copy=doctors1.copy()
            for doctor in doctors1_copy:
                doct=[item for item in csp[value1[0]].doctors.copy() if item.id == doctor.id]
                if len(doct) == 0:
                    doctors1.remove(doctor)

            doctors2_copy=doctors2.copy()
            for doctor in doctors2_copy:
                doct=[item for item in csp[value2[0]].doctors.copy() if item.id == doctor.id]
                if len(doct) == 0:
                    doctors2.remove(doctor)

            csp_copy=copy.deepcopy(csp)

            csp, doctors_queue=busqueda(doctors1, doctors2, x_i, x_j, doctors_queue, csp, csp_copy, list_marks_doctors, "doctors", doctors_graph)

            list_marks_doctors.append((x_i,x_j))

            if len(doctors_queue) > 0:
                for item in csp.values():
                    if len(item.doctors) == 0:
                        csp=csp_copy
                        break
                if not doctores_aparatos_no_repetidos(doctors, "doctors", csp):
                    csp=csp_copy

            pacient_dicc=csp.copy()
            

        if not valid_solution_apparatus(csp, aparatos_list) and len(aparatos_queue) > 0:
            edge = aparatos_queue.pop()
            x_i = edge.node1
            x_j = edge.node2

            if not x_i in pacient_dicc:
                x_i=[item for item in pacient_dicc.keys() if item.name == x_i.name]
                x_i=x_i[0]
            if not x_j in pacient_dicc:
                x_j=[item for item in pacient_dicc.keys() if item.name == x_j.name]
                x_j=x_j[0]

            aparatos1=pacient_dicc[x_i].apparatus.copy()
            aparatos2=pacient_dicc[x_j].apparatus.copy()

            value1=[item for item in csp.keys() if item.name == x_i.name ]
            value2=[item for item in csp.keys() if item.name == x_j.name ]
            
            aparatos1_copy=aparatos1.copy()
            for aparato in aparatos1_copy:
                apar=[item for item in csp[value1[0]].apparatus.copy() if item.id == aparato.id]
                if len(apar) == 0:
                    aparatos1.remove(aparato)

            aparatos2_copy=aparatos2.copy()
            for aparato in aparatos2_copy:
                apar=[item for item in csp[value2[0]].apparatus.copy() if item.id == aparato.id]
                if len(apar) == 0:
                    aparatos2.remove(aparato)

            csp_copy=copy.deepcopy(csp)

            csp, aparatos_queue=busqueda(aparatos1, aparatos2, x_i, x_j, aparatos_queue, csp, csp_copy, list_marks_aparatos, "aparatos", aparatos_graph)

            list_marks_aparatos.append((x_i,x_j))
            
            if len(aparatos_queue) > 0:
                for item in csp.values():
                    if len(item.apparatus) == 0:
                        csp=csp_copy
                        break
                if not doctores_aparatos_no_repetidos(aparatos, "aparatos", csp):
                    csp=csp_copy

            pacient_dicc=csp.copy()

        if valid_solution(csp):
            return csp
    return csp

#-------------------------------------------------------------------------------------------------------------------------------------------------
        
#--------------------------------------Metodo auxiliar del metodo principal-------------------------------------------------------------------------     
def busqueda(list1, list2, pac1, pac2, queue, csp, csp_copy, list_marks, tipo, graph):

    if len(list1)==1 and len(list2)==1:
        actualizar_dominio(pac1, list1[0], tipo, csp)
        return csp, queue
    else:
        for item1 in list1:
            for item2 in list2:
                if not item1 == item2:
                    if tipo == "doctors":
                        pac1.doctor=item1
                        pac2.doctor=item2
                    else:
                        pac1.apparatus=item1
                        pac2.apparatus=item2

                    actualizar_dominio(pac1, item1, tipo, csp)
                    actualizar_dominio(pac2, item2, tipo, csp)

                    if check_domain(csp):
                        for x_k in neighbors(pac1, tipo,graph):
                            if tipo=="doctors" and not arista_Existente(queue, list_marks, x_k, pac1):
                                queue.append(Edge(x_k, pac1))
                            elif tipo=="aparatos" and not arista_Existente(queue, list_marks, x_k,pac1):
                                queue.append(Edge(x_k, pac1))
                        return csp, queue
                        
                    else:
                        csp=copy.deepcopy(csp_copy)

#------------------------------------------------------------------------------------------------------------------------------------------

def arista_Existente(queue, list_marks, item1, item2):
    for item in queue:
        if item.node1.name==item1.name and item.node2.name==item2.name:
            return True
    for item in list_marks:
        if item[0].name==item1.name and item[1].name==item2.name:
            return True
    return False

 
#---------------------------------LLamada al metodo principal----------------------------------------------------------------------------------
def backtracking_search(doctors_queue, aparatos_queue, pacient_dicc, doctors_graph, aparatos_graph, doctors, aparatos): # Returns solution/failure
    csp=copy.deepcopy(pacient_dicc)
    return ac_3(csp, doctors_queue, aparatos_queue, pacient_dicc, [], [], doctors_graph, aparatos_graph, doctors, aparatos)

#----------------------------------------------------------------------------------------------------------------------------------------------

def hospital_simulation(pacientes, aparatos, cirugias, doctors):
    

    pos_inicial=0
    cant_pacientes=2

    cirugias_en_proceso=[]
    csp_list=[]


    time=0
    while(time < 10):

        pacientes_list=pacientes[pos_inicial:pos_inicial + cant_pacientes]


        pacientes_rel_doct_apar_dicc={}
        aparatos, pacientes_rel_doct_apar_dicc=fill_dicc(pacientes_list, pacientes_rel_doct_apar_dicc, cirugias, aparatos)
        doctors_graph, aparatos_graph = fill_graph(pacientes_list, doctors)


        ac_3=backtracking_search(edge_sort(doctors_graph, "doctors",pacientes_rel_doct_apar_dicc.copy()), edge_sort(aparatos_graph, "aparatos",pacientes_rel_doct_apar_dicc.copy()), pacientes_rel_doct_apar_dicc.copy(), doctors_graph, aparatos_graph, doctors, aparatos)

        csp_list.append(ac_3)
        
        for paciente_solution in ac_3.items():
            solution=paciente_solution[1]
            if len(solution.apparatus) > 0 and isinstance(solution.apparatus[0], Cirugia):
                cirugias_en_proceso.append(paciente_solution)
            elif len(solution.doctors) > 0:
                solution.doctors[0].hours_elapsed = solution.doctors[0].hours_elapsed + 2
                    # if solution.apparatus[0].hours_elapsed + 2 == solution.apparatus[0].total_hours:
                    #     pass
                    # else:
                    #     solution.apparatus[0].hours_elapsed=solution.apparatus[0].hours_elapsed + 2
                    #     solution.doctors[0].hours_elapsed=solution.doctors[0].hours_elapsed + 2
                    #     solution.doctors[0].available=False
        

        for pacient, solution in cirugias_en_proceso:
            if solution.apparatus[0].hours_elapsed + 2 >= solution.apparatus[0].total_hours:
                solution.doctors[0].hours_elapsed = solution.doctors[0].hours_elapsed + 2
                solution.doctors[0].available = True
                aparatos.remove(solution.apparatus[0])
            else:
                solution.doctors[0].hours_elapsed = solution.doctors[0].hours_elapsed + 2
                solution.apparatus[0].hours_elapsed = solution.apparatus[0].hours_elapsed + 2

        pos_inicial=pos_inicial+cant_pacientes

        # pac1=Pacient(None, None, ["pancrea"], "1")
        # pac2=Pacient("pancrea", "X-Ray", None, "2")
        # pac3=Pacient(None, None, ["cerebro"], "3")
        # pac4=Pacient(None, None, ["mama"],"4")
        # pac5=Pacient("ovario", "AparatoO1", None, "5")

        # pacientes_list=[]
        # pacientes_list.append(pac1)
        # pacientes_list.append(pac2)
        # pacientes_list.append(pac3)
        # pacientes_list.append(pac4)
        # pacientes_list.append(pac5)
        # pacientes_list=[pac1, pac2, pac3, pac4, pac5]



        time=time + 2
    


        for pacient,solution in ac_3.items():
            print("Proximo paciente")
            print(pacient.name)
            for doctor in solution.doctors:
                print(doctor.name)
            for aparato in solution.apparatus:
                print(aparato.name)

    return csp_list

paciente1=Pacient("cerebro", "radioterapia", [],1)
paciente2= Pacient("ovarios", 'quimioterapia', [], 2)
paciente3=Pacient("cerebro", "radioterapia", [],3)
paciente4= Pacient("mama", 'radioterapia', [], 4)
paciente5=Pacient("pancreas", "radioterapia", [], 5)
paciente6=Pacient("pancreas", "quimioterapia", [], 6)
# hospital_simulation([paciente1, paciente2, paciente3, paciente4,paciente5, paciente6], aparatos, cirugias, doctors)

