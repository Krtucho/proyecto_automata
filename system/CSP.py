from hospital_class import *
import copy



pacientes_rel_doct_sala_apar={}

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

doctor1=Doctor("pancrea", 10, None, "Doctor1", 1)
doctor2=Doctor("pancrea", 10, None, "Doctor2", 2)
doctor3=Doctor("pancrea", 10, None, "Doctor3", 3)
doctor4=Doctor("cerebro", 10, None, "Doctor4", 4)
doctor5=Doctor("General", 10, None, "Doctor5", 5)
doctor6=Doctor("General", 10, None, "Doctor6", 6)
doctor7=Doctor("ovario", 10, None, "Doctor7", 7)
doctor8=Doctor("ovario", 10, None, "Doctor8", 8)
doctor9=Doctor("ovario", 10, None, "Doctor9", 9)

aparato1=Apparatus("AparatoP", 1)
aparato2=Apparatus("AparatoP", 2)
aparato3=Apparatus("X-Ray", 3)
aparato4=Apparatus("X-Ray", 4)
aparato5=Apparatus("X-Ray", 5)
aparato6=Apparatus("X-Ray", 6)
aparato9=Apparatus("X-Ray", 9)
aparato7=Apparatus("AparatoO1", 7)
aparato8=Apparatus("AparatoO2", 8)


paciente1=Pacient(None, None, ["pancrea"], "1")
paciente2=Pacient("pancrea", "X-Ray", None, "2")
paciente3=Pacient(None, None, ["cerebro"], "3")
paciente4=Pacient(None, None, ["ovario"],"4")
paciente5=Pacient("ovario", "AparatoO1", None, "5")

paciente6=Pacient(None, None, ["pancrea"], "6")
# paciente7=Pacient("pancrea", "AparatoP", "7")
paciente8=Pacient("cerebro", "X-Ray", None, "8")
paciente9=Pacient(None, None, ["ovario"],"9")
paciente10=Pacient("ovario", "AparatoO2", None, "10")




#---------------------------------------------------------------------

pacientes=[paciente1, paciente2, paciente3, paciente4, paciente5, paciente6, paciente8, paciente9, paciente10]
doctors=[doctor1, doctor2, doctor3, doctor4, doctor5, doctor6, doctor7, doctor8, doctor9]
aparatos=[aparato1, aparato2, aparato3, aparato4, aparato5, aparato6, aparato7, aparato8, aparato9]

enfermedad_dicc={"pancrea":Solution(), "ovario":Solution(), "cerebro":Solution()}
terapias_dicc={"pancrea":Solution(), "ovario":Solution(), "cerebro":Solution()}

enfermedad_dicc["pancrea"].apparatus.append(aparato1)
enfermedad_dicc["pancrea"].apparatus.append(aparato2)
enfermedad_dicc["ovario"].apparatus.append(aparato7)
enfermedad_dicc["ovario"].apparatus.append(aparato8)

terapias_dicc["ovario"].apparatus.append(aparato7)
terapias_dicc["ovario"].apparatus.append(aparato8)

for doctor in doctors:
    if doctor.specialty == 'General':
        for terapia in terapias_dicc.keys():
            if not doctor in terapias_dicc[terapia].doctors:
                terapias_dicc[terapia].doctors.append(doctor)
    else:
        if not doctor in terapias_dicc[doctor.specialty].doctors and not doctor in enfermedad_dicc[doctor.specialty].doctors:
            enfermedad_dicc[doctor.specialty].doctors.append(doctor)
            terapias_dicc[doctor.specialty].doctors.append(doctor)

print("Despues de agregar doctores")
print(enfermedad_dicc)
print(terapias_dicc)

for aparato in aparatos:
    if aparato.name == "X-Ray":
        for item in enfermedad_dicc.keys():
            if not aparato in enfermedad_dicc[item].apparatus and not aparato in terapias_dicc[item].apparatus:
                enfermedad_dicc[item].apparatus.append(aparato)
                terapias_dicc[item].apparatus.append(aparato)
    # else:
    #     if not aparato in terapias_dicc[aparato.type_of_therapy].apparatus and not aparato in enfermedad_dicc[aparato.type_of_therapy].apparatus:

    #     for terapia in terapias_dicc.keys():
    #         if not aparato in terapias_dicc[terapia].apparatus:
    #             terapias_dicc[terapia].apparatus.append(aparato)
    elif aparato.name == "Quimioterapia" or aparato.name == "Radioterapia" or aparato.name == "Cirugia" or aparato.name == "Cuidados paliativos":
        for terapia in terapias_dicc.keys():
            if not aparato in terapias_dicc[terapia].apparatus:
                terapias_dicc[terapia].apparatus.append(aparato)

print("Despues de agregar aparatos")
print(enfermedad_dicc)
print(terapias_dicc)


for paciente in pacientes:
    pacientes_rel_doct_sala_apar[paciente]=Solution()
    temp=pacientes_rel_doct_sala_apar[paciente]
    if not paciente.type_tumor == None:
        for doctor in terapias_dicc[paciente.type_tumor].doctors:
            if doctor.available:
                temp.doctors.append(doctor)
        for aparato in terapias_dicc[paciente.type_tumor].apparatus:
            if aparato.available and aparato.name == paciente.therapies_receiving:
                temp.apparatus.append(aparato)
    else:
        for tumor in paciente.possibles_tumors:
            for doctor in enfermedad_dicc[tumor].doctors:
                if doctor.available:
                    temp.doctors.append(doctor)
            for aparato in enfermedad_dicc[tumor].apparatus:
                if aparato.available:
                    temp.apparatus.append(aparato)

print("Pacientes")
print(pacientes)

doctors_graph=Graph(pacientes)
aparatos_graph=Graph(pacientes)

print(doctors_graph)
print(aparatos_graph)

for paciente1 in pacientes:
    for paciente2 in pacientes:
        if not paciente1.name == paciente2.name:
            if not paciente1.type_tumor == None and not paciente2.type_tumor == None:

                if paciente1.type_tumor == paciente2.type_tumor:
                    # doctors_graph.insert(paciente1, paciente2)
                    aparatos_graph.insert(paciente1, paciente2)
                elif paciente1.therapies_receiving == paciente2.therapies_receiving:
                    aparatos_graph.insert(paciente1, paciente2)
                # else:
                doctors_graph.insert(paciente1, paciente2)

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

print(doctors_graph)
print(aparatos_graph)

def edge_sort():
    nodes_sort=doctors_graph.nodes.copy()
    for i in range(0,len(doctors_graph.nodes)):
        for j in range(0,len(doctors_graph.nodes)):
            node1=nodes_sort[i]
            node2=nodes_sort[j]
            if len(pacientes_rel_doct_sala_apar[node1].doctors) < len(pacientes_rel_doct_sala_apar[node2].doctors):
                # node=nodes_sort[i]
                nodes_sort[i]=node2
                nodes_sort[j]=node1

    edges_sort=[]
    for node in nodes_sort:
        for edge in doctors_graph.edges:
            if edge.node1.name == node.name and not edge in edges_sort:
                edges_sort.append(edge)
    return edges_sort

def edge_sort_aparatos():
    nodes_sort=aparatos_graph.nodes.copy()
    for i in range(0,len(aparatos_graph.nodes)):
        for j in range(0,len(aparatos_graph.nodes)):
            node1=nodes_sort[i]
            node2=nodes_sort[j]
            if len(pacientes_rel_doct_sala_apar[node1].apparatus) < len(pacientes_rel_doct_sala_apar[node2].apparatus):
                # node=nodes_sort[i]
                nodes_sort[i]=node2
                nodes_sort[j]=node1

    edges_sort=[]
    for node in nodes_sort:
        for edge in doctors_graph.edges:
            if edge.node1.name == node.name and not edge in edges_sort:
                edges_sort.append(edge)
    return edges_sort






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

def neighbors(x_i, tipo):
    if tipo == "doctors":
        return doctors_graph.neighbors(x_i)
    else:
        return aparatos_graph.neighbors(x_i)


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


# def actualizar_dominio(paciente1, item1, tipo, pacient_dicc):
#     pacient_dicc_copy=pacient_dicc.copy()
#     for paciente in pacient_dicc_copy:
#         lists=[]
#         lists_copy=[]
#         if tipo == "doctors":
#             lists=pacient_dicc_copy[paciente].doctors
#             lists_copy=doctors_temp.copy()
#         for item in lists_copy:
#             if paciente.name == paciente1.name:
#                 if not doctor.name == item1.name:
#                     pacient_dicc[paciente].doctors.remove(doctor)
#             else:
#                 if doctor.name == item1.name:
#                     pacient_dicc[paciente].doctors.remove(doctor)

def valid_solution(pacient_dicc):
    for solution in pacient_dicc.values():
        if not len(solution.doctors) == 1 or not len(solution.apparatus) == 1:
            return False
    return True
def valid_solution_doctors(pacient_dicc):
    for solution in pacient_dicc.values():
        if not len(solution.doctors) == 1:
            return False
    return True
def valid_solution_apparatus(pacient_dicc):
    for solution in pacient_dicc.values():
        if not len(solution.apparatus) == 1:
            return False
    return True


def ac_3(csp, doctors_queue, aparatos_queue, pacient_dicc, list_marks_doctors, list_marks_aparatos): # returns the CSP, posibly with reduced domains

    # if valid_solution(csp) or len(doctors_queue) == 0:
    #     return csp
    # else:
    # doctors_queue
    while len(doctors_queue) > 0 and len(aparatos_queue) > 0:

        if not valid_solution_doctors(csp) and len(doctors_queue) > 0:
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

            csp, doctors_queue=busqueda(doctors1, doctors2, x_i, x_j, doctors_queue, csp, csp_copy, list_marks_doctors, "doctors")

            list_marks_doctors.append((x_i,x_j))

            for item in csp.values():
                if len(item.doctors) == 0:
                    csp=csp_copy
                    break

            pacient_dicc=csp.copy()
            

            # if check_domain(csp):
            #     for x_k in neighbors(x_i):
            #         doctors_queue.append(Edge(x_k, x_i))

        if not valid_solution_apparatus(csp) and len(aparatos_queue) > 0:
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

            # for item in csp.keys():
            #     if item.name==x_i.name:
            #         for aparato in 
            csp_copy=copy.deepcopy(csp)

            csp, aparatos_queue=busqueda(aparatos1, aparatos2, x_i, x_j, aparatos_queue, csp, csp_copy, list_marks_aparatos, "aparatos")

            list_marks_aparatos.append((x_i,x_j))

            for item in csp.values():
                if len(item.apparatus) == 0:
                    csp=csp_copy
                    break

            pacient_dicc=csp.copy()

        if valid_solution(csp):
            return csp


        # if check_domain(csp):
        #     for x_k in neighbors(x_i):
        #         doctors_queue.append(Edge(x_k, x_i))
        #             if valid_solution(csp):
        #                 return csp
        #         else:
        #             csp=copy.deepcopy(csp_copy)


                            # aparatos_queue
                        # while len(aparatos_queue) > 0:
                        #     edge = aparatos_queue.pop()
                        #     x_i = edge.node1
                        #     x_j = edge.node2
                        #     if remove_inconsistent_values(x_i, x_j, domain_type="aparatos"):
                        #         for x_k in neighbors(x_i):
                        #             aparatos_queue.append(Edge(x_k, x_j))
                        #         ac_3(csp, doctors_queue, pacient_dicc)


        # if valid_solution(csp):
        #     return csp

        
def busqueda(list1, list2, pac1, pac2, queue, csp, csp_copy, list_marks, tipo):

    for item1 in list1:
        for item2 in list2:
            if not item1 == item2:
                if tipo == "doctors":
                    pac1.doctor=item1
                    pac2.doctor=item2
                else:
                    pac1.apparatus=item1
                    pac2.apparatus=item2
                    # if remove_inconsistent_values(x_i, x_j, domain_type="doctors"):
                # print("doctors_graph.neighbors(x_i)")
                # print(doctors_graph.neighbors(x_i))

                actualizar_dominio(pac1, item1, tipo, csp)
                actualizar_dominio(pac2, item2, tipo, csp)

                if check_domain(csp):
                    for x_k in neighbors(pac1, tipo):
                        if tipo=="doctors" and not arista_Existente(queue, list_marks, x_k, pac1):
                            queue.append(Edge(x_k, pac1))
                        elif tipo=="aparatos" and not arista_Existente(queue, list_marks, x_k,pac1):
                            queue.append(Edge(x_k, pac1))
                    return csp, queue
                    
                else:
                    csp=copy.deepcopy(csp_copy)

def arista_Existente(queue, list_marks, item1, item2):
    for item in queue:
        if item.node1.name==item1.name and item.node2.name==item2.name:
            return True
    for item in list_marks:
        if item[0].name==item1.name and item[1].name==item2.name:
            return True
    return False

 
# def backtracking_search(csp, doctors_queue=doctors_graph.edges, aparatos_queue=aparatos_graph.edges): # Returns solution/failure
#     return ac_3(csp, doctors_queue, aparatos_queue)

def backtracking_search(doctors_queue=edge_sort(), aparatos_queue=edge_sort_aparatos(), pacient_dicc=pacientes_rel_doct_sala_apar.copy()): # Returns solution/failure
    csp=copy.deepcopy(pacientes_rel_doct_sala_apar)
    return ac_3(csp, doctors_queue, aparatos_queue, pacient_dicc, [], [])

for pacient,solution in backtracking_search().items():
    print("Proximo paciente")
    print(pacient.name)
    for doctor in solution.doctors:
        print(doctor.name)
    for aparato in solution.apparatus:
        print(aparato.name)
    # print("aparatos")
    # for aparat in solution.apparatus:
    #     print(aparat.id)
# for edge in edge_sort():
#     print("Aristas")
#     print(edge.node1.name)
#     print(edge.node2.name)

# for item in doctors_graph.nodes:
#     print(item.name)
#     print("Vecinos")
#     for vecino in doctors_graph.neighbors(item):
#         print(vecino.name)
#     print("termine")


# print(backtracking_search(pacientes_rel_doct_sala_apar))
